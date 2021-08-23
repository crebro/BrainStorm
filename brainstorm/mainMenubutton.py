from brainstorm.constants import COLORS, FONTS
import pygame

class MainMenuButton:
    def __init__(self, image, text, centerX, y, padding=30) -> None:
        self.image = image
        self.text = FONTS["Regular"].render(
            text, 1, (COLORS['white_foreground']))
        self.centerX = centerX
        self.y = y
        self.imageTextOffset = 20
        self.padding = padding
        self.width = (self.image.get_width() if self.image.get_width() > self.text.get_width() else self.text.get_width()) + padding * 2
        self.height = self.image.get_height() + self.imageTextOffset + self.text.get_height() +  self.padding * 2 
        self.leftX = (self.centerX - (self.image.get_width() / 2) if self.image.get_width() > self.text.get_width() else self.centerX -(self.text.get_width() / 2)) - self.padding

    def draw(self, surface):
        if self.isHovering():
            pygame.draw.rect(surface, COLORS['hovering_color'], (self.leftX, self.y - self.padding, self.width, self.height ) )

        surface.blit(self.image, (self.centerX -
                                  (self.image.get_width() / 2), self.y))
        surface.blit(self.text, (self.centerX -
                                 (self.text.get_width() / 2), self.y + self.image.get_height() + self.imageTextOffset))

    def isHovering(self):
        mousex, mousey = pygame.mouse.get_pos()
        if mousex > self.leftX and mousex < self.leftX + self.width  and mousey > self.y  and mousey < self.y + self.height:
            return True
        return False

