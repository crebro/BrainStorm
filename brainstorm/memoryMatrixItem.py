from brainstorm.constants import COLORS, IMAGES, WIDTH
import pygame


class MemoryMatrixItem:
    def __init__(self, x, y, width, height, value, borderWidth) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = value
        self.isSelected = False
        self.borderWidth = borderWidth

    def draw(self, surface, revealing, showingAfterGuesses):
        pygame.draw.rect(
            surface,
            COLORS["matrix_border"],
            (
                self.x - self.borderWidth,
                self.y - self.borderWidth,
                self.width + (self.borderWidth * 2),
                self.width + (self.borderWidth * 2),
            ),
        )
        if revealing and self.value == True:
            self.showMatrixColoured(surface)
        else:
            if self.isSelected:
                if self.value:
                    self.showMatrixColoured(surface)
                else:
                    self.showMatrixNone(surface)
                    self.showMatrixWrong(surface)
            else:
                if showingAfterGuesses and self.value:
                    self.showMatrixColouredFailed(surface)
                    return
                self.showMatrixNone(surface)

    def showMatrixNone(self, surface):
        pygame.draw.rect(
            surface,
            COLORS["matrix_none_box"],
            (
                self.x,
                self.y,
                self.width,
                self.height,
            ),
        )

    def showMatrixColouredFailed(self, surface):
        pygame.draw.rect(
            surface,
            COLORS["matrix_coloured_failed_box"],
            (
                self.x,
                self.y,
                self.width,
                self.height,
            ),
        )

    def showMatrixWrong(self, surface):
        surface.blit(
            IMAGES["matrix_wrong"],
            (
                self.x - self.borderWidth // 2,
                self.y - self.borderWidth // 2,
            ),
        )

    def showMatrixColoured(self, surface):
        pygame.draw.rect(
            surface,
            COLORS["matrix_coloured_box"],
            (
                self.x,
                self.y,
                self.width,
                self.height,
            ),
        )
