import pygame

pygame.mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 1280, 720
COLORS = {
    "black_background": (30, 30, 30),
    "hovering_color": (50, 50, 50),
    "white_foreground": (255, 255, 255),
    "matrix_border": (54, 38, 35),
    "matrix_background": (113, 82, 72),
    "matrix_none_box": (93, 68, 61),
    "matrix_coloured_box": (77, 188, 182),
    "matrix_coloured_failed_box": (65, 110, 107),
}

FONTS = {
    "Regular": pygame.font.Font("assets/fonts/NunitoSans-Regular.ttf", 20),
    "RegularSmall": pygame.font.Font("assets/fonts/NunitoSans-Regular.ttf", 15),
    "SemiBold": pygame.font.Font("assets/fonts/NunitoSans-SemiBold.ttf", 40),
    "Bold": pygame.font.Font("assets/fonts/NunitoSans-Bold.ttf", 50),
}

IMAGES = {
    "console": pygame.transform.scale(
        pygame.image.load("assets/images/console.png"), (200, 200)
    ),
    "news": pygame.transform.scale(
        pygame.image.load("assets/images/news.png"), (200, 200)
    ),
    "na": pygame.transform.scale(
        pygame.image.load("assets/images/not available.png"), (260, 150)
    ),
    "back": pygame.transform.scale(
        pygame.image.load("assets/images/backbutton.png"), (50, 50)
    ),
    "memorymatrix": pygame.transform.scale(
        pygame.image.load("assets/images/memorymatrix.JPG"), (200, 200)
    ),
    "ebbandflow": pygame.transform.scale(
        pygame.image.load("assets/images/ebbandflow.JPG"), (200, 200)
    ),
    "matrix_wrong": pygame.transform.scale(
        pygame.image.load("assets/images/wrong matrix.png"), (80, 80)
    ),
    "matrix_all_right": pygame.transform.scale(
        pygame.image.load("assets/images/tick.png"), (100, 100)
    ),
}

SOUNDS = {
    "tick": pygame.mixer.Sound("assets/sounds/timersound.wav"),
    "correct": pygame.mixer.Sound("assets/sounds/correct.wav"),
    "wrong": pygame.mixer.Sound("assets/sounds/wrong.mp3"),
    "flip": pygame.mixer.Sound("assets/sounds/flip.wav"),
}
