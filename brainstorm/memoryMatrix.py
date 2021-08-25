from pygame.event import post
from brainstorm.menuButton import MenuButton
from brainstorm.constants import COLORS, FONTS, IMAGES, WIDTH
import pygame
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
        self.matrixSurface = pygame.Surface(
            (
                self.numberOfRows * MATRIX_SQUARE_WIDTH,
                self.numberOfRows * MATRIX_SQUARE_WIDTH,
            )
        )
        self.matrix = []
        self.generateMatrix()
        print(self.matrix)

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

            self.update()
            pygame.display.update()

    def update(self):
        self.backButton.draw(self.surface)
        self.surface.blit(
            self.topText,
            (self.width / 2 - (self.topText.get_width() / 2), self.topPadding),
        )
        self.drawBorder()

        for row in range(self.numberOfRows):
            for col in range(self.numberOfCols):
                position = self.matrix[col][row]
                pygame.draw.rect(
                    self.matrixSurface,
                    COLORS["matrix_border"],
                    (
                        (row) * MATRIX_SQUARE_WIDTH - self.matrixItemBorderWidth,
                        (col) * MATRIX_SQUARE_WIDTH - self.matrixItemBorderWidth,
                        MATRIX_SQUARE_WIDTH + (self.matrixItemBorderWidth * 2),
                        MATRIX_SQUARE_WIDTH + (self.matrixItemBorderWidth * 2),
                    ),
                )
                if position == True:
                    pygame.draw.rect(
                        self.matrixSurface,
                        COLORS["matrix_coloured_box"],
                        (
                            (row) * MATRIX_SQUARE_WIDTH,
                            (col) * MATRIX_SQUARE_WIDTH,
                            MATRIX_SQUARE_WIDTH,
                            MATRIX_SQUARE_WIDTH,
                        ),
                    )
                else:
                    pygame.draw.rect(
                        self.matrixSurface,
                        COLORS["matrix_none_box"],
                        (
                            (row) * MATRIX_SQUARE_WIDTH,
                            (col) * MATRIX_SQUARE_WIDTH,
                            MATRIX_SQUARE_WIDTH,
                            MATRIX_SQUARE_WIDTH,
                        ),
                    )
        self.surface.blit(
            self.matrixSurface,
            (
                self.width / 2 - (self.matrixSurface.get_width() / 2),
                self.topPadding + self.topText.get_height() + self.topPadding,
            ),
        )

    def generateMatrix(self):
        newMatrix = []
        for row in range(self.numberOfRows):
            newMatrix.append([])
            for _ in range(self.numberOfCols):
                newMatrix[row].append(False)

        for _ in range(self.numberOfBlueSquares):
            randomRow, randomCol = random.randint(
                0, self.numberOfRows - 1
            ), random.randint(0, self.numberOfCols - 1)
            position = newMatrix[randomRow][randomCol]
            while position:
                randomRow, randomCol = random.randint(
                    0, self.numberOfRows - 1
                ), random.randint(0, self.numberOfCols - 1)
                position = newMatrix[randomRow][randomCol]
            newMatrix[randomRow][randomCol] = True

        self.matrix = newMatrix

    def drawBorder(self):
        matrixPosX, matrixPosY = (
            self.width / 2 - (self.matrixSurface.get_width() / 2),
            self.topPadding + self.topText.get_height() + self.topPadding,
        )
        pygame.draw.rect(
            self.surface,
            COLORS["matrix_border"],
            (
                matrixPosX - self.borderWidth,
                matrixPosY - self.borderWidth,
                self.matrixSurface.get_width() + self.borderWidth * 2,
                self.matrixSurface.get_height() + self.borderWidth * 2,
            ),
        )
