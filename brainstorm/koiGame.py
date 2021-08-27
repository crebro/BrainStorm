from brainstorm.koiFish import KoiFish
from brainstorm.menuButton import MenuButton
import pygame
import sys
from brainstorm.constants import COLORS, FONTS, HEIGHT, IMAGES, KOISIZE, WIDTH


class KoiGame:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.numberOfFishes = 5
        self.drawing = True
        self.fishes = []
        self.generateFishes()
        self.topPadding = 20
        self.topText = FONTS["Bold"].render(
            "Feeding Koi", 1, COLORS["white_foreground"]
        )
        self.backButton = MenuButton(
            IMAGES["back"], "Back", IMAGES["back"].get_width() / 2 + 20, 20, padding=20
        )
        self.clock = pygame.time.Clock()

    def generateFishes(self):
        for _ in range(self.numberOfFishes):
            self.fishes.append(
                KoiFish((self.width - KOISIZE[0], self.height - KOISIZE[1]))
            )

    def draw(
        self,
    ):
        while self.drawing:
            self.clock.tick(60)
            self.surface.fill(COLORS["koi_pond_color"])
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    if b1 and self.backButton.isHovering():
                        self.drawing = False
                if event.type == pygame.QUIT:
                    sys.exit()

            self.update()
            pygame.display.update()

    def update(self):
        self.backButton.draw(self.surface)
        self.surface.blit(
            self.topText,
            (self.width / 2 - (self.topText.get_width() / 2), self.topPadding),
        )

        for fish in self.fishes:
            fish.draw(self.surface)
