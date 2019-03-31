import pygame

class Bird:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.bird = pygame.transform.scale(pygame.image.load("Graphics/Bird.png"), (100, 100))
        self.rect = self.bird.get_rect().move((self.xpos, self.ypos))

    def show(self, screen):
        screen.blit(self.bird, self.rect)