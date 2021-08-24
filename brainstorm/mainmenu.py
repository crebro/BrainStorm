from brainstorm.newsScreen import NewsScreen
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
        self.clock = pygame.time.Clock()
        self.running = True

    def draw(self,):
        while self.running:
            self.clock.tick(40)
            self.surface.fill(COLORS['black_background'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    if b1 and self.newsOption.isHovering():
                        # self.running = False
                        newsScreen = NewsScreen(self.surface)
                        newsScreen.draw()
                        

            self.update()
            pygame.display.update()


    def update(self):

        # Blitting the Headline and the Byline of the Application on to the Screen
        self.surface.blit(self.mainMenuHeadline, (self.width / 2 -
                                                  (self.mainMenuHeadline.get_width() / 2), self.topPadding),)
        self.surface.blit(self.mainMenuByline, (self.width / 2 -
                                                (self.mainMenuByline.get_width() / 2),  self.mainMenuHeadline.get_height() + self.topPadding))

        # Blitting the image and Text of the Console Image
        self.gamesOption.draw(self.surface)
        self.newsOption.draw(self.surface)
