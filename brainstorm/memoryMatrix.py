from brainstorm.memoryMatrixItem import MemoryMatrixItem
from pygame.event import post
from brainstorm.menuButton import MenuButton
from brainstorm.constants import COLORS, FONTS, HEIGHT, IMAGES, SOUNDS, WIDTH
import pygame

pygame.mixer.init()
import sys
import random

MATRIX_SQUARE_WIDTH = 80


class MemoryMatrix:
    def __init__(self, surface) -> None:
        self.surface = surface
        self.width, self.height = self.surface.get_width(), self.surface.get_height()
        self.drawing = True
        self.topText = FONTS["Bold"].render(
            "Memory Matrix", 1, COLORS["white_foreground"]
        )
        self.backButton = MenuButton(
            IMAGES["back"], "Back", IMAGES["back"].get_width() / 2 + 20, 20, padding=20
        )
        self.topPadding = 20
        self.numberOfRows = 6
        self.numberOfCols = 6
        self.numberOfBlueSquares = 5
        self.borderWidth = 20
        self.matrixItemBorderWidth = 10
        self.start_time = pygame.time.get_ticks()
        self.revealing = True
        self.revealingTime = 3000
        self.waitingTime = 2000
        self.waiting = False
        self.score = 0
        self.allRightThisMatch = True
        self.showingAfterGuesses = False
        self.matrixSurface = pygame.Surface(
            (
                self.numberOfRows * MATRIX_SQUARE_WIDTH,
                self.numberOfRows * MATRIX_SQUARE_WIDTH,
            )
        )
        self.matrix = []
        self.matrixX, self.matrixY = (
            self.width / 2 - (self.matrixSurface.get_width() / 2),
            self.topPadding + self.topText.get_height() + self.topPadding,
        )
        self.guessesLeft = self.numberOfBlueSquares
        self.generateMatrix()

    def draw(self):
        while self.drawing:
            self.surface.fill(COLORS["matrix_background"])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    b1, b2, b3 = pygame.mouse.get_pressed()
                    if b1 and self.backButton.isHovering():
                        self.drawing = False
                    position = self.isHoveringOnMatrix()
                    if b1 and position and not (self.revealing) and not (self.waiting):
                        px, py = position
                        row, col = py // MATRIX_SQUARE_WIDTH, px // MATRIX_SQUARE_WIDTH
                        matrixItem = self.matrix[int(row)][int(col)]
                        if not (matrixItem.isSelected):
                            self.matrix[int(row)][int(col)].isSelected = True
                            self.guessesLeft -= 1

                            if matrixItem.value == True:
                                self.score += 250
                            else:
                                self.allRightThisMatch = False

                            if self.guessesLeft <= 0:
                                self.waiting = True
                                self.waiting_start_time = pygame.time.get_ticks()
                                self.showingAfterGuesses = True

            if (
                self.revealing
                and pygame.time.get_ticks() - self.start_time > self.revealingTime
            ):
                self.revealing = False

            if (
                self.waiting
                and pygame.time.get_ticks() - self.waiting_start_time > self.waitingTime
            ):
                self.waiting = False
                self.revealing = True
                self.showingAfterGuesses = False
                self.allRightThisMatch = True
                self.numberOfBlueSquares += 1
                self.guessesLeft = self.numberOfBlueSquares
                self.start_time = pygame.time.get_ticks()
                self.generateMatrix()

            self.update()
            pygame.display.update()

    def update(self):
        self.backButton.draw(self.surface)
        self.surface.blit(
            self.topText,
            (self.width / 2 - (self.topText.get_width() / 2), self.topPadding),
        )
        self.drawBorder()
        self.showTimer()

        for row in range(self.numberOfRows):
            for col in range(self.numberOfCols):
                position = self.matrix[col][row]
                position.draw(
                    self.matrixSurface, self.revealing, self.showingAfterGuesses
                )

        self.surface.blit(
            self.matrixSurface,
            (self.matrixX, self.matrixY),
        )

        self.showGuessesLeft()
        self.showScore()
        self.showAllRightThisMatch()

    def generateMatrix(self):
        newMatrix = []
        for row in range(self.numberOfRows):
            newMatrix.append([])
            for col in range(self.numberOfCols):
                newMatrix[row].append(
                    MemoryMatrixItem(
                        col * MATRIX_SQUARE_WIDTH,
                        row * MATRIX_SQUARE_WIDTH,
                        MATRIX_SQUARE_WIDTH,
                        MATRIX_SQUARE_WIDTH,
                        False,
                        self.matrixItemBorderWidth,
                    )
                )

        for _ in range(self.numberOfBlueSquares):
            randomRow, randomCol = random.randint(
                0, self.numberOfRows - 1
            ), random.randint(0, self.numberOfCols - 1)
            position = newMatrix[randomRow][randomCol]
            while position.value:
                randomRow, randomCol = random.randint(
                    0, self.numberOfRows - 1
                ), random.randint(0, self.numberOfCols - 1)
                position = newMatrix[randomRow][randomCol]

            newMatrix[randomRow][randomCol].value = True

        self.matrix = newMatrix

    def drawBorder(self):
        pygame.draw.rect(
            self.surface,
            COLORS["matrix_border"],
            (
                self.matrixX - self.borderWidth,
                self.matrixY - self.borderWidth,
                self.matrixSurface.get_width() + self.borderWidth * 2,
                self.matrixSurface.get_height() + self.borderWidth * 2,
            ),
        )

    def showTimer(self):
        if self.revealing:
            pygame.draw.circle(
                self.surface,
                COLORS["white_foreground"],
                (WIDTH // 2 // 2 // 2, HEIGHT // 2),
                50,
            )
            renderingText = FONTS["Bold"].render(
                str(
                    (4000 - (pygame.time.get_ticks() - self.start_time)) // 1000,
                ),
                1,
                COLORS["black_background"],
            )
            self.surface.blit(
                renderingText,
                (
                    (WIDTH // 2 // 2 // 2) - renderingText.get_width() // 2,
                    (HEIGHT // 2) - renderingText.get_height() // 2,
                ),
            )

    def showAllRightThisMatch(self):
        if self.allRightThisMatch and self.waiting:
            tickImage = IMAGES["matrix_all_right"]
            self.surface.blit(
                tickImage,
                (
                    (WIDTH // 2)
                    + (WIDTH // 2 // 2)
                    + (WIDTH // 2 // 2 // 2)
                    - tickImage.get_width() // 2,
                    (HEIGHT // 2) - tickImage.get_height() // 2,
                ),
            )

    def isHoveringOnMatrix(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        if (
            mouseX > self.matrixX
            and mouseX < self.matrixX + self.matrixSurface.get_width()
            and mouseY > self.matrixY
            and mouseY < self.matrixY + self.matrixSurface.get_width()
        ):
            return (mouseX - self.matrixX, mouseY - self.matrixY)
        return False

    def showGuessesLeft(self):
        guessesLeftText = FONTS["Bold"].render(
            f"Guesses: {self.guessesLeft}", 1, COLORS["white_foreground"]
        )
        self.surface.blit(
            guessesLeftText,
            (
                self.width - guessesLeftText.get_width() - self.topPadding,
                self.height - guessesLeftText.get_height() - self.topPadding,
            ),
        )

    def showScore(self):
        scoreText = FONTS["Bold"].render(
            f"Score: {self.score}", 1, COLORS["white_foreground"]
        )
        self.surface.blit(
            scoreText,
            (
                self.topPadding,
                self.height - scoreText.get_height() - self.topPadding,
            ),
        )
