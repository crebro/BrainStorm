from brainstorm.mainMenubutton import MainMenuButton
from brainstorm.constants import COLORS, FONTS, IMAGES
import pygame


class MainMenu:
    def __init__(self, surface) -> None:
        self.topPadding = 50
        self.surface = surface
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.mainMenuHeadline = FONTS['Bold'].render(
            "BrainStorm", 1, (COLORS['white_foreground']))
        self.mainMenuByline = FONTS['Regular'].render(
            "The all in one solution to Health Problems and Goals", 1, (COLORS['white_foreground']))
        self.gamesOption = MainMenuButton(
            IMAGES["console"], "Brain Games", self.width / 2 - (IMAGES["console"].get_width()),  self.height / 2 - (IMAGES["console"].get_height() / 2))
        self.newsOption = MainMenuButton(IMAGES['news'], "Health News", self.width / 2 + (IMAGES["console"].get_width()),  self.height / 2 - (IMAGES["console"].get_height() / 2))

    def draw(self,):

        # Blitting the Headline and the Byline of the Application on to the Screen
        self.surface.blit(self.mainMenuHeadline, (self.width / 2 -
                                                  (self.mainMenuHeadline.get_width() / 2), self.topPadding),)
        self.surface.blit(self.mainMenuByline, (self.width / 2 -
                                                (self.mainMenuByline.get_width() / 2),  self.mainMenuHeadline.get_height() + self.topPadding))

        # Blitting the image and Text of the Console Image
        self.gamesOption.draw(self.surface)
        self.newsOption.draw(self.surface)
        # imageX, imageY = , windowHeight / 2 - \
        #     (self.image.get_height() / 2)
