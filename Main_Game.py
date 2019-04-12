import sys, pygame
from Pipe import *
from Bird import *
import random

#Init pygame runs seperately
pygame.init()

class FlappyBird:

    def run(self):
        #screen size
        x = 1200
        y = 800
        #background RGB
        background = 135, 206, 235

        #define pipe speed
        pipe_speed = 5

        bird = Bird(300,300)

        pipes = []

        for i in range(1,4):
            ypos = random.randint(320, 900)
            pipes.append(PipePair(i*1200, ypos))

        #opens screen
        screen = pygame.display.set_mode((x,y))

        while 1:
            #Needed to end pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    else:
                        bird.jump()

            #Creates background
            screen.fill(background)

            #define new position of pipe
            for i, pipePair in enumerate(pipes):
                pipePair.move_x(-pipe_speed)

                if pipePair.get_x() <= -190:
                    ypos = random.randint(320,900)
                    pipes.pop(i)
                    pipes.insert(i,PipePair(3790,ypos))

            for p in pipes:
                p.show(screen)

            bird.calcNewPos()

            bird.show(screen)
            pygame.display.flip()



#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()
