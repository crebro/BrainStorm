import pygame
import os

pygame.mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 1280, 720
KOISIZE = (100, 100)
COLORS = {
    "black_background": (30, 30, 30),
    "hovering_color": (50, 50, 50),
    "white_foreground": (255, 255, 255),
    "matrix_border": (54, 38, 35),
    "matrix_background": (113, 82, 72),
    "matrix_none_box": (93, 68, 61),
    "matrix_coloured_box": (77, 188, 182),
    "matrix_coloured_failed_box": (65, 110, 107),
    "koi_pond_color": (0, 167, 144),
    "good_green": (98, 222, 53),
    "odd_blue": (77, 79, 136),
    "color_match_background": (123, 97, 78),
    "colorMatch": {
        "blue": (0, 0, 255),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "black": (0, 0, 0),
    },
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
        pygame.image.load("assets/images/games/memorymatrix.JPG"), (200, 200)
    ),
    "ebbandflow": pygame.transform.scale(
        pygame.image.load("assets/images/games/ebbandflow.JPG"), (200, 200)
    ),
    "koi": pygame.transform.scale(
        pygame.image.load("assets/images/games/koi.jpg"), (200, 200)
    ),
    "colormatch": pygame.transform.scale(
        pygame.image.load("assets/images/games/colormatch.JPG"), (200, 200)
    ),
    "matrix_wrong": pygame.transform.scale(
        pygame.image.load("assets/images/wrong matrix.png"), (80, 80)
    ),
    "matrix_all_right": pygame.transform.scale(
        pygame.image.load("assets/images/tick.png"), (100, 100)
    ),
    "tick": pygame.transform.scale(
        pygame.image.load("assets/images/tick.png"), (100, 100)
    ),
    "wrong": pygame.transform.scale(
        pygame.image.load("assets/images/wrong.png"), (100, 100)
    ),
    "minus": pygame.transform.scale(
        pygame.image.load("assets/images/minus.png"), (100, 100)
    ),
    "question": pygame.transform.scale(
        pygame.image.load("assets/images/question.png"), (50, 50)
    ),
    "rightarrow": pygame.transform.scale(
        pygame.image.load("assets/images/rightarrow.png"), (50, 50)
    ),
    "leftarrow": pygame.transform.scale(
        pygame.image.load("assets/images/leftarrow.png"), (50, 50)
    ),
}

SOUNDS = {
    "tick": pygame.mixer.Sound("assets/sounds/timersound.wav"),
    "correct": pygame.mixer.Sound("assets/sounds/correct.wav"),
    "wrong": pygame.mixer.Sound("assets/sounds/wrong.mp3"),
    "flip": pygame.mixer.Sound("assets/sounds/flip.wav"),
}
KOI_ANIMATION = [
    pygame.transform.scale(pygame.image.load(f"assets/images/Kois/{image}"), KOISIZE)
    for image in os.listdir("assets/images/Kois")
]

DOCUMENTATION = """
    How to Play Tutorial
    
    ------------- Playing Koi ------------- Skill: Divied Attention
    You are given the task of feeding all the poor koi fishes,
    but you only have a limited number of koi food, every level, 
    that is the number of kois in the pond,
    your task is to feed each fish only once,
    with every level you pass the number of koi fishes increase
    
    ------------- Memory Matrix ------------- Skill: Working Memory
    This game is to increase your skill to memorize things,
    There are blue squares shown to you on each level,
    and you have to memorize their location,
    you have to get all of them without getting a single one wrong,
    Three wrongs in Three rounds, then you're out

    ------------- Color Match ------------- Responsive Inhibition
    This is a game to test your responsiveness, 
    you have to be quick and play against the time,
    if the name of the color matches on the left matches with the 
    actual color on the right press right to indicite that they match
    if not press the left arrow key to indicate that they don't match 

"""
