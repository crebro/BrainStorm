import pygame
pygame.font.init()

WIDTH, HEIGHT = 1280, 720
COLORS = {
    "black_background": (30, 30, 30),
    "hovering_color": (50, 50, 50),
    "white_foreground": (255, 255, 255)
}

FONTS = {
    "Regular": pygame.font.Font("assets/fonts/NunitoSans-Regular.ttf", 20),
    "RegularSmall": pygame.font.Font("assets/fonts/NunitoSans-Regular.ttf", 15),
    "SemiBold": pygame.font.Font("assets/fonts/NunitoSans-SemiBold.ttf", 40),
    "Bold": pygame.font.Font("assets/fonts/NunitoSans-Bold.ttf", 50),
}

IMAGES = {
    "console": pygame.transform.scale(pygame.image.load("assets/images/console.png"), (200, 200)),
    "news": pygame.transform.scale(pygame.image.load("assets/images/news.png"), (200, 200)),
    "na": pygame.transform.scale(pygame.image.load("assets/images/not available.png"), (260, 150)),
}
