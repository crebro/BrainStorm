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
        self.topPadding = 20
        self.topText = FONTS["Bold"].render(
            "Feeding Koi", 1, COLORS["white_foreground"]
        )
        self.backButton = MenuButton(
            IMAGES["back"], "Back", IMAGES["back"].get_width() / 2 + 20, 20, padding=20
        )
        self.clock = pygame.time.Clock()
        self.hudHeight = 60
        self.hudPadding = 10
        self.hudBarHeight = self.hudHeight - (self.hudPadding * 2)
        self.counterStartTime = pygame.time.get_ticks()
        self.waitingTime = 1000
        self.canFeedFish = False
        self.fishesFed = 0
        self.fishSpeed = 1
        self.loadingStart = pygame.time.get_ticks()
        self.loadingNextRound = True
        self.loadingTime = 3000
        # self.generateFishes()

    def generateFishes(self):
        self.fishes = []
        for _ in range(self.numberOfFishes):
            self.fishes.append(
                KoiFish(
                    (self.width - KOISIZE[0], self.height - KOISIZE[1] - self.hudHeight)
                )
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
                        return
                    if self.canFeedFish:
                        for fish in self.fishes:
                            if fish.isHovering():
                                fish.tryToFeedFish()
                                self.counterStartTime = pygame.time.get_ticks()
                                self.canFeedFish = False
                                self.fishesFed += 1
                                break

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
            fish.draw(self.surface, self.fishSpeed, stayInCenter=self.loadingNextRound)

        if (
            self.loadingNextRound
            and pygame.time.get_ticks() - self.loadingStart > self.loadingTime
        ):
            self.loadingNextRound = False
            self.fishSpeed = 1
            self.generateFishes()

        if self.fishesFed == self.numberOfFishes:
            self.loadingNextRound = True
            self.numberOfFishes += 1
            self.fishesFed = 0
            self.loadingStart = pygame.time.get_ticks()
            self.fishSpeed = 3
            for fish in self.fishes:
                fish.targetX, fish.targetY = self.width / 2, self.height / 2

        self.drawBar()
        self.drawTimer()

    def drawBar(self):
        time = (
            pygame.time.get_ticks() - self.counterStartTime
            if not (self.canFeedFish)
            else self.waitingTime
        )
        maxWidth = WIDTH // 2 // 2 - (self.hudPadding * 2)
        pygame.draw.rect(
            self.surface,
            COLORS["good_green"] if self.canFeedFish else COLORS["white_foreground"],
            (
                self.hudPadding,
                HEIGHT - (self.hudBarHeight - self.hudPadding * 2),
                (time / self.waitingTime) * maxWidth,
                self.hudBarHeight,
            ),
        )
        if not (self.canFeedFish) and time >= self.waitingTime:
            self.canFeedFish = True

    def drawTimer(self):
        if self.loadingNextRound:
            time = (4000 - (pygame.time.get_ticks() - self.loadingStart)) // 1000
            renderingText = FONTS["Bold"].render(
                str(
                    time,
                ),
                1,
                COLORS["black_background"],
            )
            pygame.draw.circle(
                self.surface,
                COLORS["white_foreground"],
                (self.width / 2, self.height / 2),
                100,
            )
            self.surface.blit(
                renderingText,
                (
                    (WIDTH // 2) - renderingText.get_width() // 2,
                    (HEIGHT // 2) - renderingText.get_height() // 2,
                ),
            )
