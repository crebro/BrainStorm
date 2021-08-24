from brainstorm.utils import renderTextCenteredAt
from brainstorm.constants import COLORS, FONTS, IMAGES, WIDTH
from brainstorm.api import getImage, getJsonRequest
import pygame
import sys
import threading
import urllib.request
import string
import random
import os

class NewsScreen:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.news = []
        self.newsApiRequestLocation = "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=1a327762034a49188731ed54d5cd459b&pageSize=5"
        self.drawing = True
        self.topText = FONTS["Bold"].render("Latest Health News", 1, COLORS['white_foreground'])
        self.topPadding = 20
        self.singleNewsHeight = 150
        self.numberOfNews = 5
        self.allowedWidthForNews = 900
        self.newsSurfaceHeight = self.singleNewsHeight * self.numberOfNews
        self.newsSurface = pygame.Surface( ( self.width,  self.newsSurfaceHeight) )
        self.imageWidth = 200
        self.newsSurface.fill(COLORS['black_background'])
        self.initialSurfaceYPos = self.topPadding + self.topText.get_height() + self.topPadding
        self.surfaceYPos = self.topPadding + self.topText.get_height() + self.topPadding

        getNewsThread = threading.Thread(target=self.getNewsWithRequest)
        getNewsThread.start()

    def draw(self):
        while self.drawing:
            self.surface.fill(COLORS['black_background'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEWHEEL:
                    self.on_scroll( event.y > 0 )

            self.update()
            pygame.display.update()

    def update(self):
        self.surface.blit(self.topText, (self.width / 2 -
                                                  (self.topText.get_width() / 2), self.topPadding),)
        self.surface.blit(self.newsSurface, ( 0, self.surfaceYPos ))

    def on_news_get(self):
        currentHeight = 0
        for news_item in self.news:
            # renderedText = FONTS['Regular'].render(news_item['title'], 1, COLORS['white_foreground'] )
            onlineImageLocation = news_item['urlToImage']
            randomStorageLocation = f"temp/{self.randomStringGenerator()}.png"

            image = IMAGES['na']
            try:
                urllib.request.urlretrieve(onlineImageLocation, randomStorageLocation)

                image = pygame.transform.scale( pygame.image.load(randomStorageLocation) , ( self.imageWidth, self.singleNewsHeight ) )

                os.remove(randomStorageLocation)
            except Exception as e:
                print(e)

            self.newsSurface.blit( image, ( self.width / 2 - (self.allowedWidthForNews / 2), currentHeight  ) )
            remainingWidth = self.allowedWidthForNews - image.get_width() + 20
            renderTextCenteredAt(news_item['title'], FONTS['Regular'], COLORS['white_foreground'], ( ((self.width / 2 - (self.allowedWidthForNews / 2)) +  image.get_width())) + (remainingWidth / 2)   , currentHeight , self.newsSurface, remainingWidth )
            
            # self.newsSurface.blit( renderedText , ( self.width / 2 - (renderedText.get_width() / 2), currentHeight) )
            currentHeight += self.singleNewsHeight
            

    def getNewsWithRequest(self):
        response = getJsonRequest(self.newsApiRequestLocation)
        self.news = response['articles']
        self.on_news_get()

    def randomStringGenerator(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))

    def on_scroll(self, up):
        if up  and self.surfaceYPos < self.initialSurfaceYPos:
            self.surfaceYPos += 10
        elif not(up)  and self.surfaceYPos  + self.initialSurfaceYPos > ( self.newsSurfaceHeight - self.height ):
            self.surfaceYPos -= 10

    # def listenToScrolling(self):
    #     listener = mouse.Listener(
    #         on_scroll=self.on_scroll)
    #     listener.start()

