import pygame

class Pipe:
    def __init__(self, xpos, ypos, rev):
        self.xpos = xpos
        self.ypos = ypos
        self.rev = rev

        self.surface = pygame.image.load("Graphics/pipes.png")
        self.surface = pygame.transform.scale(self.surface, (197, 400))
        if self.rev:
            self.surface = pygame.transform.rotate(self.surface, 180)
        self.rect = self.surface.get_rect().move((self.xpos, self.ypos))