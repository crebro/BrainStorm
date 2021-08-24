from brainstorm.mainmenu import MainMenu
from brainstorm.constants import COLORS, FONTS
import pygame


class BrainstormApplication:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.mainMenu = MainMenu(self.win)
        self.showingMainMenu = True
        pygame.display.set_caption("Brain Storm")

    def run(self):
        self.mainMenu.draw()
