from Bird import *

class collider:

    def check_collision(self, pipes,xpos,ypos):
        parameters = []
        #directions: 0: straight up, 1: diagonally up, 2: straight forward, 3: diagonally down, 4: down
        for direction in range(0,5):
            x,y = xpos, ypos
            if direction == 0:
                a = 0
                for p in pipes:
                    while not (p.top.rect.collidepoint(x,y) or p.bot.rect.collidepoint(x,y) or (y < -500)):
                        y -= 5
                        a += 1
                    else:
                        parameters.append(a)

            elif direction == 1:
                a = 0
                for p in pipes:
                    while not (p.top.rect.collidepoint(x,y) or p.bot.rect.collidepoint(x,y) or (y < -500)):
                        y -= 2.5
                        x += 2.5
                        a += 1
                    else:
                        parameters.append(a)

            elif direction == 2:
                a = 0
                for p in pipes:
                    while not (p.top.rect.collidepoint(x,y) or p.bot.rect.collidepoint(x,y)):
                        x += 5
                        a += 1
                    else:
                        parameters.append(a)

            elif direction == 3:
                a = 0
                for p in pipes:
                    while not (p.top.rect.collidepoint(x,y) or p.bot.rect.collidepoint(x,y) or (y > 1080)):
                        y += 2.5
                        x += 2.5
                        a += 1
                    else:
                        parameters.append(a)

            elif direction == 4:
                a = 0
                for p in pipes:
                    while not (p.top.rect.collidepoint(x,y) or p.bot.rect.collidepoint(x,y) or (y > 1080)):
                        y += 5
                        a += 1
                    else:
                        parameters.append(a)

        return parameters


