import random
from pgzero.actor import Actor
from pgzero.builtins import sounds
import store

# --- GAME VARIABLES ---
score = 0
level = 1
health = 3
speed = 3
timer = 0
spawn_timer = 0
spawn_delay = 120
is_safe = False
safe_timer = 0

# Six lane centers between the road shoulders in the 800px road texture.
lanes = [160, 250, 350, 450, 550, 640]
ROAD_LEFT = 145
ROAD_RIGHT = 655
BACKGROUNDS = {
    1: "roads/road_egypt_level5",
    2: "roads/road_forest_level6",
    3: "roads/road_snow_level3",
    4: "roads/road_night_level4",
    5: "roads/road_normal_level1",
    6: "roads/road_desert_level2"

}
current_bg = 1
ROAD_TILE_HEIGHT = 800
ROAD_VIEW_HEIGHT = 600

# --- ACTORS ---
road1 = Actor(BACKGROUNDS[1], (400, ROAD_TILE_HEIGHT // 2))
road2 = Actor(BACKGROUNDS[1], (400, -ROAD_TILE_HEIGHT // 2))
road_fade_actors = []
road_fade_remaining = 0
ROAD_FADE_DURATION = 0.75
hero = Actor("cars/car_red", (400, 500))
hero.scale = 0.5

# Coins & Traffic
coins = 0
coin_timer = 0
coins_list = []
coin_icon = Actor("icons/dollar", (710, 565))
coin_icon.scale = 0.08

enemy_cars = []
CAR_IMAGES = ["cars/car_blue", "cars/car_green", "cars/car4", "cars/car5", "cars/car6"]
heart = Actor("icons/health")
heart.scale = 1.5


def reset():
    """Reset the game back to the start."""
    global score, level, health, speed, timer, is_safe, safe_timer
    global spawn_timer, spawn_delay, enemy_cars, coins, coin_timer, coins_list, current_bg
    global road_fade_actors, road_fade_remaining

    score, level, health, speed, timer = 0, 1, 3, 3, 0
    is_safe, safe_timer = False, 0
    spawn_timer, spawn_delay = 0, 120
    coin_timer = 0
    current_bg = 1
    road_fade_actors = []
    road_fade_remaining = 0
    coins_list.clear()
    enemy_cars.clear()

    hero.pos = (400, 500)
    hero.image = store.selected_skin
    road1.image, road1.pos = BACKGROUNDS[1], (400, ROAD_TILE_HEIGHT // 2)
    road2.image, road2.pos = BACKGROUNDS[1], (400, -ROAD_TILE_HEIGHT // 2)


def add_coin():
    lane = random.choice(lanes)
    if any(abs(c.x - lane) < 40 and c.y < 150 for c in enemy_cars + coins_list):
        return
    c = Actor("icons/dollar", (lane, -50))
    c.scale = 0.08
    coins_list.append(c)


def add_enemy():
    lane = random.choice(lanes)
    if any(c.x == lane and c.y < 200 for c in enemy_cars):
        return
    car = Actor(random.choice(CAR_IMAGES), (lane, -80))
    car.scale, car.angle = 0.4, 180
    enemy_cars.append(car)


def update(keyboard, dt):
    global score, level, speed, timer, spawn_delay, is_safe, safe_timer, current_bg
    global spawn_timer, coin_timer, health, coins, road_fade_actors, road_fade_remaining

    # Keep movement stable across frame rates and limit jumps after a slow frame.
    frame_scale = min(dt * 60, 2)

    # 1. Road scrolling & background update
    road1.y += speed * frame_scale
    road2.y += speed * frame_scale
    recycle_y = ROAD_VIEW_HEIGHT + ROAD_TILE_HEIGHT // 2
    if road1.y >= recycle_y:
        road1.y = road2.y - ROAD_TILE_HEIGHT
    if road2.y >= recycle_y:
        road2.y = road1.y - ROAD_TILE_HEIGHT

    for faded_road in road_fade_actors:
        faded_road.y += speed * frame_scale
    if road_fade_actors:
        if road_fade_actors[0].y >= recycle_y:
            road_fade_actors[0].y = road_fade_actors[1].y - ROAD_TILE_HEIGHT
        if road_fade_actors[1].y >= recycle_y:
            road_fade_actors[1].y = road_fade_actors[0].y - ROAD_TILE_HEIGHT
        road_fade_remaining = max(0, road_fade_remaining - frame_scale / 60)
        if road_fade_remaining == 0:
            road_fade_actors = []

    bg = min(level, 6)
    if bg != current_bg:
        road_fade_actors = [
            Actor(BACKGROUNDS[current_bg], road1.pos),
            Actor(BACKGROUNDS[current_bg], road2.pos),
        ]
        for faded_road in road_fade_actors:
            faded_road._surf = faded_road._surf.copy()
        road_fade_remaining = ROAD_FADE_DURATION
        current_bg = bg
        road1.image = BACKGROUNDS[bg]
        road2.image = BACKGROUNDS[bg]

    # 2. Hero movement
    if keyboard.left and hero.x > ROAD_LEFT:
        hero.x -= 6 * frame_scale
    if keyboard.right and hero.x < ROAD_RIGHT:
        hero.x += 6 * frame_scale

    # 3. Score & Level progress
    timer += frame_scale
    if timer >= 30:
        score += 1
        timer = 0
        level = min((score // 30) + 1, 6)
        if score % 10 == 0:
            max_spd = {1: 7, 2: 7, 3: 7, 4: 9, 5: 12, 6: 15}.get(level, 7)
            if speed < max_spd:
                speed += 0.3
            if spawn_delay > 40:
                spawn_delay -= 10

    # 4. Safe mode timer
    if is_safe:
        safe_timer += frame_scale
        if safe_timer >= 60:
            is_safe = False
            safe_timer = 0

    # 5. Coins
    for coin in coins_list[:]:
        coin.y += speed * frame_scale
        if coin.colliderect(hero):
            coins += 1
            coins_list.remove(coin)
            sounds.coin_collect.play()
        elif coin.y > 700:
            coins_list.remove(coin)

    coin_timer += frame_scale
    if coin_timer >= 140:
        coin_timer = 0
        add_coin()

    # 6. Enemy traffic
    for car in enemy_cars[:]:
        car.y += speed * 0.5 * frame_scale
        if not is_safe and car.colliderect(hero):
            health -= 1
            enemy_cars.remove(car)
            is_safe = True
            safe_timer = 0
        elif car.y > 700:
            enemy_cars.remove(car)

    spawn_timer += frame_scale
    if spawn_timer >= spawn_delay:
        spawn_timer = 0
        add_enemy()


def draw_road(screen=None):
    road1.draw()
    road2.draw()
    if road_fade_remaining > 0:
        alpha = int(255 * road_fade_remaining / ROAD_FADE_DURATION)
        for faded_road in road_fade_actors:
            faded_road._surf.set_alpha(alpha)
            faded_road.draw()


def draw_game(screen, high_score):
    for coin in coins_list:
        coin.draw()
    for car in enemy_cars:
        car.draw()
    if not is_safe or timer % 6 < 3:
        hero.draw()

    # HUD (Score, Level, Best, Hearts, Coins)
    screen.draw.text(str(score), center=(400, 50), fontsize=80, color="white")
    screen.draw.text(f"Level {level}", topleft=(110, 15), fontsize=40, color="yellow")
    screen.draw.text(f"Best : {high_score}", topleft=(555, 15), fontsize=40, color="lime")

    for i in range(health):
        heart.pos = (40 + i * 40, 570)
        heart.draw()

    coin_icon.draw()
    screen.draw.text(str(coins), midleft=(735, 565), fontsize=40, color="gold")
