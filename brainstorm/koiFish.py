import pygame
import random
import math
from brainstorm.constants import KOI_ANIMATION


class KoiFish:
    def __init__(self, gameAreaSize) -> None:
        self.gameAreaWidth, self.gameAreaHeight = gameAreaSize
        self.currentImageIndex = 0
        self.image = KOI_ANIMATION[self.currentImageIndex]
        self.drawingImage = self.image
        self.rotation = 0
        self.animationFrequencyTime = 200
        self.start_time = pygame.time.get_ticks()
        self.targetX, self.targetY = random.randint(0, self.gameAreaWidth), random.randint(0, self.gameAreaHeight)
        self.x, self.y = self.gameAreaWidth / 2, self.gameAreaHeight / 2
        self.moveSpeed = 1

    def draw(self, surface):
        surface.blit(self.drawingImage, (self.x, self.y))
        self.manageFishMoving()
        self.manageFishRotation(surface)

        self.manageAnimation()

    def getDistance(self, x1, y1, x2, y2):
        return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    def getPointQuad(self, px, py, ownX, ownY):

        if px < ownX and py < ownY:
            return 2
        elif px > ownX and py < ownY:
            return 1
        elif px < ownX and py > ownY:
            return 3
        else:
            return 4

    def manageFishRotation(self, surface):
        ownX = self.x + self.drawingImage.get_width() / 2
        ownY = self.y + self.drawingImage.get_height() / 2
        h = self.getDistance(self.targetX, self.targetY, ownX, ownY)
        p = self.getDistance(ownX, ownY, self.targetX, ownY)
        rotation = (math.acos(p / h) * 180) / (22 / 7)
        pointQuad = self.getPointQuad(self.targetX, self.targetY, ownX, ownY)

        # pygame.draw.line(
        #     surface,
        #     COLORS["white_foreground"],
        #     (self.targetX, self.targetY),
        #     (ownX, ownY),
        # )
        # pygame.draw.line(
        #     surface, COLORS["white_foreground"], (ownX, ownY), (self.targetX, ownY)
        # )

        if pointQuad == 1:
            self.drawingImage = pygame.transform.rotate(self.image, rotation - 90)
        elif pointQuad == 4:
            self.drawingImage = pygame.transform.rotate(self.image, -rotation - 90)
        elif pointQuad == 2:
            self.drawingImage = pygame.transform.rotate(self.image, (-rotation) + 90)
        elif pointQuad == 3:
            self.drawingImage = pygame.transform.rotate(self.image, (rotation) + 90)

    def manageFishMoving(
        self,
    ):
        directionx = (1 if (self.targetX - self.x) > 0 else -1) * self.moveSpeed
        directiony = (1 if (self.targetY - self.y) > 0 else -1) * self.moveSpeed
        self.x += directionx
        self.y += directiony

        pointDistance = self.getDistance(self.x, self.y, self.targetX, self.targetY)
        if pointDistance < 25:
            self.targetX, self.targetY = random.randint(0, self.gameAreaWidth), random.randint(
                0, self.gameAreaHeight
            )

    def manageAnimation(self):
        timeElapsed = pygame.time.get_ticks() - self.start_time
        if self.currentImageIndex < 8 and timeElapsed > self.animationFrequencyTime:
            self.currentImageIndex += 1
            self.image = KOI_ANIMATION[self.currentImageIndex]

            if self.currentImageIndex == 7:
                self.currentImageIndex = 0
            self.start_time = pygame.time.get_ticks()
