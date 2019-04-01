import sys, pygame
from Pipe import *
from Bird import *
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
        pipe_speed = 1

        bird = Bird(300,300)

        pipes = []

        for i in range(40):
            pipes.append(PipePair(i*800, 500))

        #opens screen
        screen = pygame.display.set_mode((x, y))

        while 1:
            #Needed to end pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Creates background
            screen.fill(background)

            #define new position of pipe
            for pipePair in pipes:
                pipePair.move_x(-pipe_speed)

            for p in pipes:
                p.show(screen)

            bird.show(screen)
            pygame.display.flip()



#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()
