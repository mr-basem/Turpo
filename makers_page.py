import os
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Default makers list: (filename, person_name)
DEFAULT_MAKERS = [
    ("Yousef Hussein.jpg", "Yousef Hussein"),
    ("Ali Mahrous.jpeg", "Ali Mahrous"),
    ("Yousef Sheta.jpeg", "Yousef Sheta"),
    ("Jomana Ahmad.png", "Jomana Ahmad"),
]

maker_images = [img for img, _ in DEFAULT_MAKERS]

_loaded_makers = None


def get_makers():
    global _loaded_makers
    if _loaded_makers is None:
        _loaded_makers = []
        makers_dir = os.path.join(BASE_DIR, "images", "makers")

        existing_files = {}
        if os.path.isdir(makers_dir):
            for f in os.listdir(makers_dir):
                if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".webp")):
                    existing_files[f.lower()] = f

        chosen_makers = []
        used_files = set()
        for filename, name in DEFAULT_MAKERS:
            matched = existing_files.get(filename.lower())
            if matched:
                chosen_makers.append((matched, name))
                used_files.add(matched.lower())

        for lower_f, actual_f in existing_files.items():
            if lower_f not in used_files:
                name = os.path.splitext(actual_f)[0]
                chosen_makers.append((actual_f, name))

        if not chosen_makers:
            chosen_makers = list(DEFAULT_MAKERS)

        for img_name, name in chosen_makers:
            path = os.path.join(makers_dir, img_name)
            try:
                photo = pygame.image.load(path).convert()
                photo = pygame.transform.smoothscale(photo, (164, 134))
            except Exception:
                fallback = pygame.Surface((164, 134))
                fallback.fill((40, 40, 40))
                photo = fallback
            _loaded_makers.append((photo, name))

    return _loaded_makers


def get_maker_photos():
    return [photo for photo, _ in get_makers()]


def draw(screen):
    screen.draw.filled_rect(pygame.Rect(0, 0, 800, 600), "black")
    screen.draw.text("GAME MAKERS", center=(400, 60), fontsize=42, color="gold")
    screen.draw.line((120, 95), (680, 95), "gold")

    cards = [
        (130, 118),
        (490, 118),
        (130, 318),
        (490, 318),
    ]

    makers = get_makers()
    for (x, y), (photo, name) in zip(cards, makers):
        rect = pygame.Rect(x, y, 180, 150)
        screen.draw.rect(rect, "white")
        screen.draw.filled_rect(pygame.Rect(x + 10, y + 10, 164, 134), (20, 20, 20))
        screen.surface.blit(photo, (x + 8, y + 8))
        screen.draw.text(name, center=(x + 90, y + 168), fontsize=24, color="yellow")

    screen.draw.line((120, 520), (680, 520), "gold")
    screen.draw.text("Thanks for playing!", center=(400, 555), fontsize=26, color="white")
