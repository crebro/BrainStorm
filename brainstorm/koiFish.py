import pygame
import random
import math
from brainstorm.constants import COLORS, IMAGES, KOISIZE, KOI_ANIMATION


class KoiFish:
    def __init__(self, gameAreaSize) -> None:
        self.gameAreaWidth, self.gameAreaHeight = gameAreaSize
        self.currentImageIndex = 0
        self.image = KOI_ANIMATION[self.currentImageIndex]
        self.drawingImage = self.image
        self.rotation = 0
        self.animationFrequencyTime = 200
        self.start_time = pygame.time.get_ticks()
        self.targetX, self.targetY = random.randint(
            0, self.gameAreaWidth
        ), random.randint(0, self.gameAreaHeight)
        self.x, self.y = self.gameAreaWidth / 2, self.gameAreaHeight / 2
        self.isFed = False
        self.showBeingFed = False
        self.showAlreadyFed = False
        self.showBeingFedDuration = 1500
        self.showFullSizedImageDuration = 200
        self.showBeingFedStartTime = 0

    def draw(self, surface, moveSpeed, stayInCenter=False):
        if self.showBeingFed:
            self.drawBeingFed(surface)
        surface.blit(self.drawingImage, (self.x, self.y))
        self.manageFishMoving(moveSpeed, stayInCenter)
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

    def manageFishMoving(self, moveSpeed, stayInTarget):
        directionx = (1 if (self.targetX - self.x) > 0 else -1) * moveSpeed
        directiony = (1 if (self.targetY - self.y) > 0 else -1) * moveSpeed
        self.x += directionx
        self.y += directiony

        pointDistance = self.getDistance(self.x, self.y, self.targetX, self.targetY)
        if pointDistance < 25 and not (stayInTarget):
            self.targetX, self.targetY = random.randint(
                0, self.gameAreaWidth
            ), random.randint(0, self.gameAreaHeight)

    def manageAnimation(self):
        timeElapsed = pygame.time.get_ticks() - self.start_time
        if self.currentImageIndex < 8 and timeElapsed > self.animationFrequencyTime:
            self.currentImageIndex += 1
            self.image = KOI_ANIMATION[self.currentImageIndex]

            if self.currentImageIndex == 7:
                self.currentImageIndex = 0
            self.start_time = pygame.time.get_ticks()

    def isHovering(self):
        mousex, mousey = pygame.mouse.get_pos()
        koi_width, koi_height = KOISIZE
        if (
            mousex > self.x
            and mousex < self.x + koi_width
            and mousey > self.y
            and mousey < self.y + koi_height
        ):
            return True
        return False

    def tryToFeedFish(self):
        if not (self.isFed):
            self.isFed = True
        else:
            self.showAlreadyFed = True
        self.showBeingFed = True
        self.showBeingFedStartTime = pygame.time.get_ticks()
        self.shrinkingTimeStart = pygame.time.get_ticks() + (
            self.showBeingFedDuration - self.showFullSizedImageDuration
        )

    def drawBeingFed(self, surface):
        tickTime = pygame.time.get_ticks() - self.showBeingFedStartTime
        imageSize = 50
        if (tickTime) >= self.showBeingFedDuration:
            self.showBeingFed = False
        if (tickTime) <= self.showFullSizedImageDuration:
            imageSize = int((tickTime / self.showFullSizedImageDuration) * 50)
        if (tickTime) >= self.showBeingFedDuration - self.showFullSizedImageDuration:
            shrinkingTicks = pygame.time.get_ticks() - self.shrinkingTimeStart
            imageSize = imageSize - int(
                (
                    shrinkingTicks
                    / (self.showBeingFedDuration - self.showFullSizedImageDuration)
                )
                * 50
            )

        iconImage = pygame.transform.scale(
            IMAGES["wrong"] if self.showAlreadyFed else IMAGES["tick"],
            (imageSize, imageSize),
        )
        surface.blit(
            iconImage,
            (
                (self.x + self.drawingImage.get_width() // 2)
                - iconImage.get_width() // 2,
                self.y - iconImage.get_height(),
            ),
        )
