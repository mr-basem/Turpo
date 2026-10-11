import pygame
from pgzero.actor import Actor

logo = Actor("icons/logo_game", (400, 270))
logo.scale = 0.4

home_button = Actor("icons/home", (50, 50))
home_button.scale = 0.1
makers_button = Actor("icons/makers", (170, 45))
makers_button.scale = 0.18


def draw(screen):
    """Draw the start screen."""
    logo.draw()
    draw_home_button(screen)
    draw_makers_button(screen)
    screen.draw.text("Press SPACE to Start", center=(400, 540), fontsize=50, color="white")


def draw_home_button(screen=None):
    home_button.draw()


def draw_makers_button(screen=None):
    makers_button.draw()


def is_home_clicked(pos):
    return home_button.collidepoint(pos)


def is_makers_clicked(pos):
    return makers_button.collidepoint(pos)
