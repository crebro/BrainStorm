import pygame


class BrainstormApplication:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.win = pygame.display.set_mode((self.width, self.height))
        self.running = True
        pygame.display.set_caption("Brain Storm")

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
