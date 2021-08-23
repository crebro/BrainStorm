from brainstorm.mainmenu import MainMenu
from brainstorm.constants import COLORS, FONTS
import pygame


class BrainstormApplication:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.mainMenu = MainMenu(self.win)
        self.showingMainMenu = True
        pygame.display.set_caption("Brain Storm")

    def run(self):
        while self.running:
            self.clock.tick(40)
            self.win.fill(COLORS['black_background'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if (self.showingMainMenu):
                self.mainMenu.draw()

            pygame.display.update()
