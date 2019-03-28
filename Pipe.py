import pygame

class Pipe(pygame.Surface):
    game_speed = 3
    def __init__(self, xpos, ypos, rev):
        super().__init__((197,400))
        self.xpos = xpos
        self.ypos = ypos
        self.reversed = rev

    def show_pipe(self):
        image = pygame.image.load("Graphics/pipes.png")
        image = pygame.transform.scale(image, (197, 400))


