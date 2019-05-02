from Bird import *

class collider:

    def check_collision(self, direction):
        x, y = Bird.get_coordinates()
        if direction == 0:
            while not pg.Rect.collidepoint(x,y):
                y -= 5

        elif direction == 1:
            while not pg.Rect.collidepoint(x,y):
                y -= 2.5
                x += 2.5

        elif: direction


