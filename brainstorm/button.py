from brainstorm.constants import FONTS
import pygame


class Button:
    def __init__(self, text, center, backgroundColor, textColor, padding=10) -> None:
        self.text = FONTS["SemiBold"].render(text, 1, textColor)
        self.centerX, self.centerY = center
        self.padding = 10
        self.backgroundColor = backgroundColor
        self.width = self.text.get_width() + self.padding * 2
        self.height = self.text.get_height() + self.padding * 2
        self.x = self.centerX - self.width / 2
        self.y = self.centerY - self.height / 2

    def draw(self, surface):
        pygame.draw.rect(
            surface, self.backgroundColor, (self.x, self.y, self.width, self.height)
        )
        surface.blit(self.text, (self.x + self.padding, self.y + self.padding))

    def isHovering(self):
        mousex, mousey = pygame.mouse.get_pos()
        if (
            mousex > self.x
            and mousex < self.x + self.width
            and mousey > self.y
            and mousey < self.y + self.height
        ):
            return True
        return False
