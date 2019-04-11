import pygame as pg

class Bird:

    aY = 4.6 * 0.0001

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.bird = pg.transform.scale(pg.image.load("Graphics/Bird.png"), (100, 100))
        self.rect = self.bird.get_rect().move((self.xpos, self.ypos))
        self.jump_timestamp = 0
        self.velY = 0

    def show(self, screen):
        screen.blit(self.bird, self.rect)

    def calcNewPos(self):
        self.velY += Bird.aY * ((pg.time.get_ticks() - self.jump_timestamp))
        self.setY(self.ypos + self.velY)

    def jump(self):
        self.jump_timestamp = pg.time.get_ticks()
        self.velY = -8

    def setY(self, ypos):
        self.rect = self.rect.move((0, ypos - self.ypos))
        self.ypos = ypos