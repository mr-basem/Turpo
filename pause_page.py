import pygame
from pgzero.actor import Actor
BOX = pygame.Rect(175, 210, 450, 180)

volume_button = Actor("icons/volume", (370, 145))
mute_button = Actor("icons/mute", (370, 145))
volume_button.scale = 0.8
mute_button.scale = 0.8
volume_button_rect = pygame.Rect(335, 110, 70, 70)


def draw(screen, muted=False):
    screen.draw.filled_rect(BOX, (0, 0, 0))
    screen.draw.rect(BOX, (255, 220, 0))
    screen.draw.text("PAUSED", center=(400, 265), fontsize=90, color="yellow")
    screen.draw.text("Press P to Resume", center=(400, 360), fontsize=40, color="white")
    (mute_button if muted else volume_button).draw()
    screen.draw.text(
        "OFF" if muted else "ON",
        center=(425, 145),
        fontsize=28,
        color="red" if muted else "green",
    )


def is_volume_clicked(pos):
    return volume_button_rect.collidepoint(pos)
