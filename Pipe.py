import pygame

class PipePair:

    space = 280

    def __init__(self, xpos, ypos):
        self.bot = Pipe(xpos, ypos, False)
        self.top = Pipe(xpos, ypos - PipePair.space - Pipe.grafic_height, True)
        self.scored = False

    def show(self, screen):
        self.top.show(screen)
        self.bot.show(screen)

    def move_x(self, offset):
        self.top.move_x(offset)
        self.bot.move_x(offset)

    #returns (x, y) with x = False if rect hit one of the pipes and y = true when the bird scored from this pipe
    def check_collision(self, rect):
        score = False
        if rect.x > self.top.xpos and not self.scored:
            score = self.scored = True
        if rect.y > 540:
            return (self.bot.check_collision(rect), score)
        else:
            return (self.top.check_collision(rect), score)

    def get_x(self):
        return self.top.xpos

    def get_coordinates(self):
        return self.top.xpos,self.top.ypos, self.bot.xpos, self.bot.ypos

class Pipe:

    #ignore hits on the curved x pixels
    hitbox_border = 40

    grafic_width = 197
    grafic_height = 820

    def __init__(self, xpos, ypos, rev):
        self.xpos = xpos
        self.ypos = ypos
        self.rev = rev

        self.surface = pygame.transform.scale(pygame.image.load("Graphics/pipes.png"), (Pipe.grafic_width, Pipe.grafic_height))
        if self.rev:
            self.surface = pygame.transform.rotate(self.surface, 180)
        self.rect = self.surface.get_rect().move((self.xpos, self.ypos))

    def show(self, screen):
        screen.blit(self.surface, self.rect)

    def move_x(self, offset):
        self.rect = self.rect.move((offset, 0))
        self.xpos += offset

    def getHitbox(self):
        if self.rev:
            hitbox = self.rect.move((0, 0))
        else:
            hitbox = self.rect.move((0, Pipe.hitbox_border))
        hitbox.h -= Pipe.hitbox_border
        return hitbox

    #False if hit by an other Rectangle
    def check_collision(self, rect):
        return not self.getHitbox().colliderect(rect)