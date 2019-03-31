import pygame

class PipePair:

    space = 750

    def __init__(self, xpos, ypos):
        self.bot = Pipe(xpos, ypos, False)
        self.top = Pipe(xpos, ypos - PipePair.space, True)

    def show(self, screen):
        self.top.show(screen)
        self.bot.show(screen)

    def move_x(self, offset):
        self.top.move_x(offset)
        self.bot.move_x(offset)

class Pipe:

    def __init__(self, xpos, ypos, rev):
        self.xpos = xpos
        self.ypos = ypos
        self.rev = rev

        self.surface = pygame.transform.scale(pygame.image.load("Graphics/pipes.png"), (197, 400))
        if self.rev:
            self.surface = pygame.transform.rotate(self.surface, 180)
        self.rect = self.surface.get_rect().move((self.xpos, self.ypos))

    def show(self, screen):
        screen.blit(self.surface, self.rect)

    def move_x(self, offset):
        self.rect = self.rect.move((offset, 0))
        self.xpos += offset

