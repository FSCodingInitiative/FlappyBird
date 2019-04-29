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
        score = 0

        #define pipe speed
        pipe_speed = 5

        bird = Bird(300,300)

        pipes = []

        # opens screen
        screen = pygame.display.set_mode((x, y))

        for i in range(1,4):
            ypos = random.randint(400, 610)
            pipes.append(PipePair(i*1200, ypos, screen))


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
                pipePair.move_x(-pipe_speed,screen)

                if pipePair.get_x() <= -190:
                    ypos = random.randint(320,900)
                    pipes.pop(i)
                    pipes.insert(i,PipePair(3790,ypos, screen))

            for p in pipes:
                p.show(screen)

            bird.calcNewPos()
            (pipecollision, scored) = bird.checkCollision(pipes)
            if not pipecollision:
                sys.exit()
            if scored:
                score += 1

            self.text_to_screen(screen, score, 100, 100)

            bird.show(screen)
            pygame.display.flip()

    def text_to_screen(self, screen, text, x, y, size=50,
                       color=(200, 000, 000)):
        try:
            text = str(text)
            font = pygame.font.SysFont(None, size)  # use default system font, size 10
            text = font.render(text, True, color)
            screen.blit(text, (x, y))

        except Exception as e:
            print('Font Error, saw it coming')
            raise e


#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()