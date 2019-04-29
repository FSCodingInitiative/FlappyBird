import pygame

class Score:

    def __init__(self, xpos, ypos, screen):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (255, 255, 255)
        self.color2 = (0, 0, 0)
        self.screen = screen


    def score_up(self, text):
        try:
            text = str(text)
            text2 = text
            font = pygame.font.Font("font/04B_19__.TTF", 90)  # use default system font, size 10
            font2 = pygame.font.Font("font/04B_19__.TTF", 110)
            text = font.render(text, True, self.color)
            text2 = font2.render(text2, True, self.color2)
            self.screen.blit(text2, (self.xpos, self.ypos))
            self.screen.blit(text, (self.xpos + 5, self.ypos + 8))
        except Exception as e:
            print('Font Error, saw it coming')
            raise e