import os
import random
import pygame
from pgzero.builtins import sounds
import start_page
import questions
import answers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 4 answer buttons
btn1 = pygame.Rect(90, 260, 620, 50)
btn2 = pygame.Rect(90, 320, 620, 50)
btn3 = pygame.Rect(90, 380, 620, 50)
btn4 = pygame.Rect(90, 440, 620, 50)
buttons = [btn1, btn2, btn3, btn4]
labels = ["A", "B", "C", "D"]

# Game state
sign_images = {}
current_q = {}
choices = []
answered = False
selected = -1
is_correct = False
coins = 0


def load_sign(name):
    if name not in sign_images:
        path = os.path.join(BASE_DIR, "images", name + ".png")
        img = pygame.image.load(path).convert_alpha()
        sign_images[name] = pygame.transform.smoothscale(img, (130, 130))
    return sign_images[name]


def pick_question():
    global current_q, choices, answered, selected, is_correct
    current_q = random.choice(questions.QUESTIONS)
    choices = list(current_q["choices"])
    random.shuffle(choices)
    answered = False
    selected = -1
    is_correct = False


pick_question()


def update(dt):
    pass


def handle_click(pos):
    global answered, selected, is_correct, coins
    if start_page.is_home_clicked(pos):
        return {"action": "home"}
    if answered:
        pick_question()
        return
    for i in range(4):
        if buttons[i].collidepoint(pos):
            answered = True
            selected = i
            is_correct = answers.check_answer(current_q["id"], choices[i])
            if is_correct:
                coins = coins + 1
                sounds.coin_collect.play()
            return {"action": "answered", "correct": is_correct}


def on_key_down(key):
    from pgzero.builtins import keys
    if key == keys.H:
        return "home"
    if key in (keys.SPACE, keys.N) and answered:
        pick_question()


def draw(screen):
    # Background
    screen.draw.filled_rect(pygame.Rect(0, 0, 800, 600), (30, 30, 50))

    # Title
    screen.draw.text("TRAFFIC QUIZ", center=(400, 30), fontsize=42, color="gold")

    # Home button
    start_page.draw_home_button(screen)

    # Sign image
    screen.surface.blit(load_sign(current_q["image"]), (335, 55))

    # Question
    screen.draw.text(current_q["question"], center=(400, 225), fontsize=22, color="white")

    # Draw 4 answer buttons
    for i in range(4):
        rect = buttons[i]
        bg = (50, 60, 90)
        border = (100, 140, 255)

        if answered:
            if i == selected:
                if is_correct:
                    bg = (0, 255, 0)
                else:
                    bg = (255, 0, 0 )
                border = "white"
            elif answers.check_answer(current_q["id"], choices[i]) and not is_correct:
                bg = (0, 255, 0)
                border = "white"

        screen.draw.filled_rect(rect, bg)
        screen.draw.rect(rect, border)
        text = labels[i] + ")  " + choices[i]
        screen.draw.text(text, midleft=(rect.left + 15, rect.centery), fontsize=17, color="white")

    # Coins
    screen.draw.text("Coins: " + str(coins), center=(400, 520), fontsize=30, color="gold")

    # Feedback
    if answered:
        if is_correct:
            screen.draw.text("Correct! +1 Coin!", center=(400, 560), fontsize=28, color=(50, 205, 50))
        else:
            screen.draw.text("Wrong! Try next one!", center=(400, 560), fontsize=28, color=(255, 80, 80))
    else:
        screen.draw.text("Pick the right answer!", center=(400, 560), fontsize=20, color=(150, 150, 200))
