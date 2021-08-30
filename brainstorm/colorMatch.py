from brainstorm.button import Button
from brainstorm.menuButton import MenuButton
import pygame
from brainstorm.constants import COLORS, FONTS, HEIGHT, IMAGES, SOUNDS, WIDTH
import sys
import random


class ColorMatch:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.drawing = True
        self.topPadding = 20
        self.topText = FONTS["Bold"].render(
            "Color Match", 1, COLORS["white_foreground"]
        )
        self.backButton = MenuButton(
            IMAGES["back"], "Back", IMAGES["back"].get_width() / 2 + 20, 20, padding=20
        )
        self.texts = ["Blue", "Red", "Black", "Green"]
        self.colors = [
            {"color": COLORS["colorMatch"]["green"], "value": "Green"},
            {"color": COLORS["colorMatch"]["blue"], "value": "Blue"},
            {"color": COLORS["colorMatch"]["red"], "value": "Red"},
            {"color": COLORS["colorMatch"]["black"], "value": "Black"},
        ]
        self.textPadding = 20
        self.totalTime = 60
        self.leftArrowButton = MenuButton(
            IMAGES["leftarrow"],
            "Don't Match",
            WIDTH // 2 - (IMAGES["leftarrow"].get_width()) - self.topPadding,
            HEIGHT - (IMAGES["leftarrow"].get_height() // 2 + 100),
        )
        self.rightArrowButton = MenuButton(
            IMAGES["rightarrow"],
            "Do Match",
            WIDTH // 2 + (IMAGES["leftarrow"].get_width()) + self.topPadding,
            HEIGHT - (IMAGES["leftarrow"].get_height() // 2 + 100),
        )

        self.reset()

    def reset(self):
        self.reInitColors()
        self.gameOver = False
        self.gameBeginningTime = pygame.time.get_ticks()
        self.score = 0

    def reInitColors(self):
        self.meaningText = random.choice(self.texts)
        self.meaningColor = random.choice(self.colors)
        self.valueText = random.choice(self.texts)
        self.valueColor = random.choice(self.colors)

    def draw(self):
        while self.drawing:
            self.surface.fill(COLORS["color_match_background"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    if b1 and self.backButton.isHovering():
                        self.drawing = False
                    if self.gameOver:
                        try:
                            if self.retryButton.isHovering():
                                self.reset()
                        except Exception as e:
                            print(e)
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    keys = pygame.key.get_pressed()
                    if (b1 and self.rightArrowButton.isHovering()) or keys[
                        pygame.K_RIGHT
                    ]:
                        if self.meaningText == self.valueColor["value"]:
                            self.score += 250
                            pygame.mixer.Sound.play(SOUNDS["correct"])

                        else:
                            self.score -= 50
                            pygame.mixer.Sound.play(SOUNDS["wrong"])
                        self.reInitColors()

                    if (b1 and self.leftArrowButton.isHovering()) or keys[
                        pygame.K_LEFT
                    ]:
                        if self.meaningText != self.valueColor["value"]:
                            pygame.mixer.Sound.play(SOUNDS["correct"])
                            self.score += 250
                        else:
                            pygame.mixer.Sound.play(SOUNDS["wrong"])
                            self.score -= 50
                        self.reInitColors()

            self.update()
            pygame.display.update()

    def update(self):
        self.backButton.draw(self.surface)
        self.rightArrowButton.draw(self.surface)
        self.leftArrowButton.draw(self.surface)
        self.surface.blit(
            self.topText,
            (self.width / 2 - (self.topText.get_width() / 2), self.topPadding),
        )

        if not (self.gameOver):
            self.drawGameColors()
            self.drawAllTimeTimer()
            self.drawScore()
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

    def drawGameColors(self):
        drawingMeaningText = FONTS["Bold"].render(
            self.meaningText,
            1,
            self.meaningColor["color"],
        )
        drawingMeaningTextWidth = (
            self.textPadding * 2
        ) + drawingMeaningText.get_width()
        drawingMeaningTextHeight = (
            self.textPadding * 2
        ) + drawingMeaningText.get_height()

        drawingValueText = FONTS["Bold"].render(
            self.valueText, 1, self.valueColor["color"]
        )
        drawingValueTextWidth = (self.textPadding * 2) + drawingValueText.get_width()
        drawingValueTextHeight = (self.textPadding * 2) + drawingValueText.get_height()

        pygame.draw.rect(
            self.surface,
            COLORS["white_foreground"],
            (
                WIDTH // 2 - drawingMeaningTextWidth - self.textPadding,
                HEIGHT // 2 - drawingMeaningTextHeight,
                drawingMeaningTextWidth,
                drawingMeaningTextHeight,
            ),
            border_radius=10,
        )
        self.surface.blit(
            drawingMeaningText,
            (
                WIDTH // 2
                - drawingMeaningTextWidth
                - self.textPadding
                + self.textPadding,
                HEIGHT // 2 - drawingMeaningTextHeight + self.textPadding,
            ),
        )

        pygame.draw.rect(
            self.surface,
            COLORS["white_foreground"],
            (
                WIDTH // 2 + self.textPadding,
                HEIGHT // 2 - drawingMeaningTextHeight,
                drawingValueTextWidth,
                drawingValueTextHeight,
            ),
            border_radius=10,
        )

        self.surface.blit(
            drawingValueText,
            (
                WIDTH // 2 + self.textPadding + self.textPadding,
                HEIGHT // 2 - drawingMeaningTextHeight + self.textPadding,
            ),
        )

        meaningHint = FONTS["Regular"].render(
            "Color Word", 1, COLORS["white_foreground"]
        )
        valueHint = FONTS["Regular"].render(
            "Color Value", 1, COLORS["white_foreground"]
        )

        self.surface.blit(
            meaningHint,
            (WIDTH // 2 - self.textPadding - meaningHint.get_width(), HEIGHT / 2),
        )
        self.surface.blit(
            valueHint,
            (WIDTH // 2 + self.textPadding, HEIGHT / 2),
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
                self.topPadding,
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
