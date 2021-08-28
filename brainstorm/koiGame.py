from brainstorm.button import Button
from brainstorm.koiFish import KoiFish
from brainstorm.menuButton import MenuButton
import pygame
import sys
from brainstorm.constants import COLORS, FONTS, HEIGHT, IMAGES, KOISIZE, WIDTH


class KoiGame:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.drawing = True
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
        self.waitingTime = 1000
        self.loadingTime = 3000
        self.waitingNextLevelTime = 3000
        self.totalTime = 120
        self.wrongsAllowed = 3
        self.scoreOnCorrectFish = 250
        self.reset()

    def reset(self):
        self.numberOfFishes = 5
        self.fishes = []
        self.counterStartTime = pygame.time.get_ticks()
        self.canFeedFish = False
        self.fishesFed = 0
        self.loadingStart = pygame.time.get_ticks()
        self.loadingNextRound = True
        self.waitingForNextLoad = False
        self.gameOver = False
        self.allRightThisMatch = True
        self.numberOfWrongs = 0
        self.score = 0
        self.gameBeginningTime = pygame.time.get_ticks()

    def generateFishes(self):
        self.fishes = []
        for _ in range(self.numberOfFishes):
            self.fishes.append(
                KoiFish(
                    (
                        self.width - KOISIZE[0],
                        self.height - KOISIZE[1] - self.hudHeight,
                    )
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
                    if self.canFeedFish and not (
                        self.waitingForNextLoad or self.loadingNextRound
                    ):
                        for fish in self.fishes:
                            if fish.isHovering():
                                if fish.isFed and self.allRightThisMatch:
                                    self.numberOfWrongs += 1
                                    self.allRightThisMatch = False
                                elif not (fish.isFed):
                                    self.score += self.scoreOnCorrectFish

                                fish.tryToFeedFish()
                                self.counterStartTime = pygame.time.get_ticks()
                                self.canFeedFish = False
                                self.fishesFed += 1
                                break
                    if self.gameOver:
                        try:
                            if self.retryButton.isHovering():
                                self.reset()
                        except Exception as e:
                            print(e)

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

        if not (self.gameOver):
            for fish in self.fishes:
                fish.draw(self.surface)

            if (
                self.loadingNextRound
                and pygame.time.get_ticks() - self.loadingStart > self.loadingTime
            ):
                self.loadingNextRound = False
                self.generateFishes()

            if (self.fishesFed == self.numberOfFishes) and not (
                self.waitingForNextLoad
            ):
                self.waitingForNextLoad = True
                self.waitingForNextLoadStartTime = pygame.time.get_ticks()
                for fish in self.fishes:
                    fish.revealFishStatus()

            if (
                self.waitingForNextLoad
                and pygame.time.get_ticks() - self.waitingForNextLoadStartTime
                > self.waitingNextLevelTime
            ):
                if self.numberOfWrongs >= self.wrongsAllowed:
                    self.gameOver = True
                    return
                self.waitingForNextLoad = False
                self.loadingNextRound = True
                self.numberOfFishes += 1
                self.fishesFed = 0
                self.allRightThisMatch = True
                self.loadingStart = pygame.time.get_ticks()
                for fish in self.fishes:
                    fish.moveEverything()

            self.drawAllTimeTimer()
            self.drawScore()
            self.drawBar()
            self.showWrongs()
            self.drawTimer()
        else:
            gameOverText = FONTS["Bold"].render(
                f"Score: { self.score }", 1, COLORS["white_foreground"]
            )
            gameOverTextX, gameOverTextY = (
                self.width / 2 - (gameOverText.get_width() / 2),
                (self.height / 2 - (gameOverText.get_height() / 2)),
            )
            self.retryButton = Button(
                "Retry",
                (WIDTH / 2, gameOverTextY + gameOverText.get_height() * 2),
                COLORS["odd_blue"],
                COLORS["white_foreground"],
            )
            self.surface.blit(gameOverText, (gameOverTextX, gameOverTextY))
            self.retryButton.draw(self.surface)

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
                50,
            )
            self.surface.blit(
                renderingText,
                (
                    (WIDTH // 2) - renderingText.get_width() // 2,
                    (HEIGHT // 2) - renderingText.get_height() // 2,
                ),
            )

    def drawAllTimeTimer(
        self,
    ):
        time = (
            (self.totalTime * 1000) - (pygame.time.get_ticks() - self.gameBeginningTime)
        ) // 1000
        if time <= 0:
            self.gameOver = True

        timeMinutes = int(time // 60)
        timeSeconds = int(time % 60)
        timeText = FONTS["Bold"].render(
            f"Time: {timeMinutes } : {  timeSeconds }",
            1,
            COLORS["white_foreground"],
        )
        self.surface.blit(
            timeText,
            (
                self.width / 2 - (timeText.get_width() / 2),
                self.height - timeText.get_height() - self.topPadding,
            ),
        )

    def drawScore(self):
        scoreText = FONTS["Bold"].render(
            f"Score: {self.score}", 1, COLORS["white_foreground"]
        )
        self.surface.blit(
            scoreText,
            (
                WIDTH - self.topPadding - scoreText.get_width(),
                self.height - scoreText.get_height() - self.topPadding,
            ),
        )

    def showWrongs(self):
        for x in range(self.numberOfWrongs):
            self.surface.blit(
                IMAGES["matrix_wrong"],
                (
                    WIDTH - IMAGES["matrix_wrong"].get_width() - self.topPadding,
                    x * IMAGES["matrix_wrong"].get_height() + self.topPadding,
                ),
            )
