from brainstorm.utils import renderTextCenteredAt
from brainstorm.constants import COLORS, FONTS
import pygame


class NewsItem:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        imageX,
        imageY,
        image,
        textX,
        textY,
        text,
        rowIteration,
        redirectLocation,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.imageX, self.imageY = imageX, imageY
        self.image = image
        self.textX, self.textY = textX, textY
        self.text = text
        self.redirectLocation = redirectLocation
        self.rowIteration = rowIteration

    def draw(self, surface, newsSurfacePosition):
        if self.isHovering(newsSurfacePosition):
            pygame.draw.rect(
                surface,
                COLORS["hovering_color"],
                (self.x, self.y, self.width, self.height),
            )
        surface.blit(self.image, (self.imageX, self.imageY))
        renderTextCenteredAt(
            self.text,
            FONTS["RegularSmall"],
            COLORS["white_foreground"],
            self.textX,
            self.textY,
            surface,
            self.image.get_width(),
        )

    def isHovering(self, newsSurfacePosition):
        mousex, mousey = pygame.mouse.get_pos()
        if (
            mousex > self.x
            and mousex < (self.x + self.width)
            and mousey > (self.y + newsSurfacePosition)
            and mousey < (self.y + self.height + newsSurfacePosition)
        ):
            return True
        return False
