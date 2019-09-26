import sys
from Bird import *
from Pipe import *
from Score import *
from Collider import *
import random
from NeuralNetwork import *
from Player import *

#Init pygame runs seperately
pygame.init()
fit = fitness()
class FlappyBird:

    def run(self):
        #screen size
        x = 1200
        y = 800
        #background RGB
        background = 135, 206, 235
        scores = 0

        #define pipe speed
        pipe_speed = 5
        bird_number = 200

        for i in range(bird_number):
        bird = Bird(300,300)
        player = Player(bird)

        pipes = []

        # opens screen
        screen = pygame.display.set_mode((x, y))

        score = Score(600, 100, screen)

        framecount = 0

        initial_weights_hidden = fit.first_weights_hid()
        initial_weights_out = fit.first_weights_out()


        for i in range(1,4):
            ypos = random.randint(400, 610)
            pipes.append(PipePair(i*1200, ypos))

        while 1:
            game_run = False
            screen.fill(background)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    else:
                        player.bird.jump()
                        game_run = True

            player.bird.show(screen)
            score.score_up(scores)
            pygame.display.flip()

            #for every bird weights, that are passed here, calc new weights


            while game_run:

                #random jump
                """if framecount > 40:
                    framecount = 0
                else:
                    framecount += 1"""

                jump = random.randint(0,1)
                #Needed to end pygame
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_run = False
                        else:
                            player.bird.jump()

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

                player.bird.calcNewPos()
                (pipecollision, scored) = player.bird.checkCollision(pipes)
                if not pipecollision:
                    break
                if scored:
                    scores += 1
                curr_coords = fit.read_out_coords(pipes, bird.get_coordinates())

                jump_y_n = fit.calc_lay(curr_coords ,initial_weights_hidden, initial_weights_out)
                print(jump_y_n)
                if jump_y_n == 1:
                    player.bird.jump()
                else:
                    pass

                player.do_i_jump(bird, pipes)
                bird.distance_travelled += pipe_speed


                score.score_up(scores)
                bird.show(screen)

                pygame.display.flip()


#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()