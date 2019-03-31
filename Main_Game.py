import sys, pygame
from Pipe import *
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
        pipe_speed = 20


        #Bird
        #Loading and sizing
        bird = pygame.image.load("Graphics/Bird.png")
        bird = pygame.transform.scale(bird, (100, 100))
        #Positioning
        birdrect = bird.get_rect()
        birdrect = birdrect.move((0, 0))


        pipes = [PipePair(500, 500)]

        #opens screen
        screen = pygame.display.set_mode((x, y))
        clock = pygame.time.Clock()
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
                if pipePair.top.xpos <= 0:
                    print(pygame.time.get_ticks())

            for p in pipes:
                p.show(screen)

            screen.blit(bird, birdrect)
            pygame.display.flip()
            clock.tick(80)



#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()
