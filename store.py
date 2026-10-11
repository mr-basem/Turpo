import pygame
from pgzero.actor import Actor
from pgzero.builtins import sounds

SKINS = [
    ("cars/car_red", "Red Racer", 0),
    ("skins/beachbugyy", "Beach Buggy", 5),
    ("skins/ferrari", "Super Ferrari", 10),
    ("skins/formula1", "Formula 1", 15),
    ("skins/pickup", "Tough Pickup", 20),
    ("skins/motocycle", "Speed Moto", 25),
    ("skins/glassycar", "Glassy Car", 30),
    ("skins/diamound", "Diamond Car", 40),
    ("skins/golden_car", "Golden Car", 50),
]

is_open = False
selected_skin = "cars/car_red"
owned_skins = ["cars/car_red"]

store_button = Actor("icons/store", (110, 50))
store_button.scale = 0.18
close_rect = pygame.Rect(740, 20, 40, 40)

# Build card UI (id, name, price, rect, preview_actor)
cards = []
for i, (sid, name, price) in enumerate(SKINS):
    col = i % 3
    row = i // 3
    x = 55 + col * 240
    y = 120 + row * 135
    rect = pygame.Rect(x, y, 210, 115)
    actor = Actor(sid, (x + 45, y + 57))
    cards.append((sid, name, price, rect, actor))

def toggle():
    global is_open
    is_open = not is_open

def close():
    global is_open
    is_open = False

def draw_button(screen=None):
    store_button.draw()

def draw(screen, coins):
    if not is_open:
        return

    screen.draw.filled_rect(pygame.Rect(0, 0, 800, 600),"#00034D")

    pygame.draw.circle(screen.surface, "red", (760, 40),20)
    screen.draw.text("X", center=(760, 40), fontsize=24, color="white")
    
    screen.draw.text("CAR SHOP", center=(400, 45), fontsize=50, color="gold")
    screen.draw.text(f"Coins: {coins}", center=(400, 85), fontsize=30, color="yellow")

    for sid, name, price, rect, actor in cards:
        if sid == selected_skin:
            tag, color, bg, border = "EQUIPPED", "lime", (35, 75, 45), (90, 240, 120)
        elif sid in owned_skins:
            tag, color, bg, border = "SELECT", "cyan", (30, 45, 70), (90, 90, 110)
        else:
            tag = f"{price} Coins"
            color = "gold" if coins >= price else "gray"
            bg, border = (35, 35, 45), (90, 90, 110)

        screen.draw.filled_rect(rect, bg)
        screen.draw.rect(rect, border)
        actor.draw()

        screen.draw.text(name, topleft=(rect.x + 85, rect.y + 18), fontsize=20, color="white")
        screen.draw.text(tag, topleft=(rect.x + 85, rect.y + 60), fontsize=20, color=color)

def is_button_clicked(pos):
    return store_button.collidepoint(pos)

def handle_click(pos, coins):
    global selected_skin
    if not is_open:
        return coins
    if close_rect.collidepoint(pos):
        close()
        return coins

    for sid, _, price, rect, _ in cards:
        if rect.collidepoint(pos):
            if sid in owned_skins:
                selected_skin = sid
                sounds.coin_collect.play()
            elif coins >= price:
                coins -= price
                owned_skins.append(sid)
                selected_skin = sid
                sounds.coin_collect.play()
            return coins
    return coins
 