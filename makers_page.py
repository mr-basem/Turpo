import pygame

maker_images = [
    "83996070-b74d-4d19-94be-fb1d5b302ebf.jpg",
    "WhatsApp Image 2026-09-19 at 12.19.30 AM.jpeg",
    "WhatsApp Image 2026-09-19 at 12.22.14 AM.jpeg",
    "F1 Ferrari Portrait at Sunset.png",
]


def draw(screen):
    screen.draw.filled_rect(pygame.Rect(0, 0, 800, 600), "black")
    screen.draw.text("GAME MAKERS", center=(400, 70), fontsize=42, color="gold")
    screen.draw.line((120, 110), (680, 110), "gold")
    screen.draw.line((120, 490), (680, 490), "gold")

    cards = [
        (130, 150),
        (490, 150),
        (130, 330),
        (490, 330),
    ]

    for (x, y), image_name in zip(cards, maker_images):
        rect = pygame.Rect(x, y, 180, 150)
        screen.draw.rect(rect, "white")
        screen.draw.filled_rect(pygame.Rect(x + 10, y + 10, 164, 134), (20, 20, 20))

        photo = pygame.image.load("images/makers/" + image_name).convert()
        photo = pygame.transform.smoothscale(photo, (164, 134))
        screen.surface.blit(photo, (x + 8, y + 8))

    screen.draw.text("Thanks for playing!", center=(400, 545), fontsize=28, color="white")
