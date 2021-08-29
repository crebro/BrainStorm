from pygame.constants import SCRAP_SELECTION
from brainstorm.utils import renderTextCenteredAt
from brainstorm.menuButton import MenuButton
import pygame
import sys
from brainstorm.constants import (
    COLORS,
    DOCUMENTATION,
    FONTS,
    HEIGHT,
    IMAGES,
    WIDTH,
)
import brainstorm.txtlib as txtlib


class HowToPlay:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.drawing = True
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.topPadding = 20
        self.topText = FONTS["Bold"].render(
            "How To Play", 1, COLORS["white_foreground"]
        )
        self.backButton = MenuButton(
            IMAGES["back"], "Back", IMAGES["back"].get_width() / 2 + 20, 20, padding=20
        )
        self.windowPadding = 100
        self.docsWidth = WIDTH - (self.windowPadding * 2)
        self.text = txtlib.Text(
            (
                self.docsWidth,
                HEIGHT,
            ),
            "assets/fonts/NunitoSans-Regular.ttf",
            font_size=15,
        )
        self.text.text = DOCUMENTATION
        self.text.update()

    def draw(
        self,
    ):
        while self.drawing:
            self.surface.fill(COLORS["black_background"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    if b1 and self.backButton.isHovering():
                        self.drawing = False

            self.update()
            pygame.display.update()

    def update(self):
        self.backButton.draw(self.surface)
        self.surface.blit(
            self.topText,
            (self.width / 2 - (self.topText.get_width() / 2), self.topPadding),
        )

        self.surface.blit(
            self.text.area,
            (
                WIDTH // 2 - (self.docsWidth // 2),
                self.topText.get_height() + self.topPadding,
            ),
        )

        # renderTextCenteredAt(
        #     DOCUMENTATION,
        #     FONTS["Regular"],
        #     COLORS["white_foreground"],
        #     WIDTH / 2,
        #     self.topPadding + self.topText.get_height() + self.topPadding,
        #     self.surface,
        #     WIDTH,
        # )
