import pygame
import pgzero.game
import pgzero.runner

pgzero.game.DISPLAY_FLAGS = pygame.SCALED
pgzero.runner.DISPLAY_FLAGS = pygame.SCALED

import pgzrun
from pgzero.builtins import keys, music, keyboard

import start_page
import play_page
import pause_page
import game_over_page
import store
import makers_page

# Window size
WIDTH, HEIGHT = 800, 600

# Game state
high_score = 0
game_started = False
paused = False
game_over = False
makers_open = False
music_muted = False


def reset_game(to_home=False):
    global game_started, paused, game_over, makers_open
    play_page.reset()
    game_over_page.reset()
    store.close()
    paused, game_over, makers_open = False, False, False
    if to_home:
        game_started = False
    music.stop()


def draw():
    # 1. Road background
    play_page.draw_road(screen)

    # 2. Screens
    if not game_started:
        if makers_open:
            makers_page.draw(screen)
            start_page.draw_home_button(screen)
        else:
            start_page.draw(screen)
            store.draw_button(screen)
    elif paused:
        play_page.draw_game(screen, high_score)
        start_page.draw_home_button(screen)
        pause_page.draw(screen, music_muted)
    elif play_page.health > 0:
        play_page.draw_game(screen, high_score)
        screen.draw.text("P = Pause | F = Fullscreen", center=(400, 590), fontsize=24, color=(150, 150, 150))
    else:
        game_over_page.draw(screen, play_page.score, play_page.coins)
        start_page.draw_home_button(screen)
        store.draw_button(screen)

    # 3. Store overlay
    store.draw(screen, play_page.coins)


def update(dt):
    global high_score, game_over
    if not game_started or paused:
        return

    if play_page.health <= 0:
        if not game_over:
            high_score = max(high_score, play_page.score)
            game_over = True
            music.stop()
            music.play_once("game_over")
            game_over_page.pick_random_sign()
        return

    play_page.update(keyboard, dt)


def on_key_down(key):
    global game_started, paused

    if key == keys.F:
        pygame.display.toggle_fullscreen()
    elif key == keys.H:
        reset_game(to_home=True)
    elif not game_started and key == keys.SPACE:
        game_started = True
        music.play("game_music")
    elif key in (keys.P, keys.ESCAPE) and play_page.health > 0:
        paused = not paused
        if paused:
            music.pause()
        else:
            music.unpause()
    elif key == keys.R and play_page.health <= 0:
        reset_game()


def on_mouse_down(pos):
    global makers_open, music_muted

    if store.is_open:
        play_page.coins = store.handle_click(pos, play_page.coins)
        play_page.hero.image = store.selected_skin
    elif not game_started:
        if makers_open:
            if start_page.is_home_clicked(pos):
                makers_open = False
            return
        if start_page.is_home_clicked(pos):
            reset_game(to_home=True)
        elif start_page.is_makers_clicked(pos):
            makers_open = True
        elif store.is_button_clicked(pos):
            store.toggle()
    elif paused and pause_page.is_volume_clicked(pos):
        music_muted = not music_muted
        music.set_volume(0 if music_muted else 1)
    elif start_page.is_home_clicked(pos):
        reset_game(to_home=True)
    elif store.is_button_clicked(pos):
        store.toggle()


pgzrun.go()
