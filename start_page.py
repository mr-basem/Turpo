import pygame
from pgzero.actor import Actor

# Styling for navigation button borders
BORDER_COLOR = (255, 215, 0)          # Warm yellow-gold ("أصفر مدي على دهبي")
BORDER_HOVER_COLOR = (255, 240, 100)  # Slightly brighter on hover
BORDER_WIDTH = 2
BORDER_RADIUS = 9
BUTTON_SIZE = 54


def make_button_rect(center_x, center_y=50, size=BUTTON_SIZE):
    return pygame.Rect(center_x - size // 2, center_y - size // 2, size, size)


HOME_RECT = make_button_rect(50)
MAKERS_RECT = make_button_rect(170)
QUIZ_RECT = make_button_rect(230)

logo = Actor("icons/logo_game", (400, 270))
logo.scale = 0.4

home_button = Actor("icons/home", (50, 50))
makers_button = Actor("icons/makers", (170, 50))
quiz_button = Actor("icons/quiz", (230, 50))


def draw_border(screen, rect):
    if screen is not None:
        mouse_pos = pygame.mouse.get_pos()
        color = BORDER_HOVER_COLOR if rect.collidepoint(mouse_pos) else BORDER_COLOR
        # Border only - strictly no background fill as requested
        pygame.draw.rect(screen.surface, color, rect, width=BORDER_WIDTH, border_radius=BORDER_RADIUS)


def draw(screen):
    """Draw the start screen."""
    logo.draw()
    draw_home_button(screen)
    draw_makers_button(screen)
    draw_quiz_button(screen)
    screen.draw.text("Press SPACE to Start", center=(400, 525), fontsize=48, color="white")
    screen.draw.text("Press Q or Click Quiz for Traffic Signs Quiz", center=(400, 565), fontsize=22, color="cyan")


def draw_home_button(screen=None):
    draw_border(screen, HOME_RECT)
    home_button.draw()


def draw_makers_button(screen=None):
    draw_border(screen, MAKERS_RECT)
    makers_button.draw()


def draw_quiz_button(screen=None):
    draw_border(screen, QUIZ_RECT)
    quiz_button.draw()


def is_home_clicked(pos):
    return HOME_RECT.collidepoint(pos) or home_button.collidepoint(pos)


def is_makers_clicked(pos):
    return MAKERS_RECT.collidepoint(pos) or makers_button.collidepoint(pos)


def is_quiz_clicked(pos):
    return QUIZ_RECT.collidepoint(pos) or quiz_button.collidepoint(pos)


