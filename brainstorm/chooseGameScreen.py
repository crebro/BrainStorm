from brainstorm.colorMatch import ColorMatch
from brainstorm.koiGame import KoiGame
from brainstorm.memoryMatrix import MemoryMatrix
from brainstorm.menuButton import MenuButton
from pygame.event import Event
from brainstorm.constants import COLORS, FONTS, IMAGES, WIDTH
import pygame
import sys


class ChooseGameScreen:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.drawing = True
        self.topText = FONTS["Bold"].render(
            "Choose a Game to Play", 1, COLORS["white_foreground"]
        )
        self.topPadding = 20
        self.optionsDrwaingY = (
            self.topPadding + self.topText.get_height() + (self.topPadding * 2)
        )
        self.backButton = MenuButton(
            IMAGES["back"], "Back", IMAGES["back"].get_width() / 2 + 20, 20, padding=20
        )
        self.memoryMatrixOption = MenuButton(
            IMAGES["memorymatrix"],
            "Memory Matrix",
            WIDTH // 2,
            self.optionsDrwaingY,
        )
        self.koiOption = MenuButton(
            IMAGES["koi"],
            "Feeding Koi",
            WIDTH // 2 - self.memoryMatrixOption.width,
            self.optionsDrwaingY,
        )
        self.colorMatchOption = MenuButton(
            IMAGES["colormatch"],
            "Color Match",
            WIDTH // 2 + self.memoryMatrixOption.width,
            self.optionsDrwaingY,
        )

    def draw(self):
        while self.drawing:
            self.surface.fill(COLORS["black_background"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    if b1 and self.backButton.isHovering():
                        self.drawing = False
                    if b1 and self.memoryMatrixOption.isHovering():
                        memoryMatrix = MemoryMatrix(self.surface)
                        memoryMatrix.draw()
                    if b1 and self.koiOption.isHovering():
                        koiGame = KoiGame(self.surface)
                        koiGame.draw()
                    if b1 and self.colorMatchOption.isHovering():
                        colorMatchgame = ColorMatch(self.surface)
                        colorMatchgame.draw()

            self.update()
            pygame.display.update()

    def update(
        self,
    ):
        self.surface.blit(
            self.topText,
            (self.width / 2 - (self.topText.get_width() / 2), self.topPadding),
        )
        self.backButton.draw(self.surface)
        self.memoryMatrixOption.draw(self.surface)
        self.koiOption.draw(self.surface)
        self.colorMatchOption.draw(self.surface)
