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
        player_dir = []
        for i in range(bird_number):
            player_dir.append(Player(Bird(300,300)))

        #bird = Bird(300,300)
        #player = Player(bird)

        pipes = []

        # opens screen
        screen = pygame.display.set_mode((x, y))

        score = Score(600, 100, screen)

        framecount = 0

        initial_weights_hidden = player_dir[i].fit.first_weights_hid()
        initial_weights_out = player_dir[i].fit.first_weights_out()


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
                        game_run = True

            for i in player_dir:
                i.bird.show(screen)
            #player.bird.show(screen)
            score.score_up(scores)
            pygame.display.flip()

            #for every bird weights, that are passed here, calc new weights


            while game_run:

                #Needed to end pygame
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            game_run = False
                        else:
                            for i in player_dir:
                                player_dir[i].bird.jump()
                            #player.bird.jump()

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
                delete_list = []
                for i, playbird in enumerate(player_dir):
                    playbird.bird.calcNewPos()
                #player.bird.calcNewPos()
                    (pipecollision, scored) = i.bird.checkCollision(pipes)
                    if not pipecollision:
                        break
                    if scored:
                        scores += 1

                for i in player_dir:
                    curr_coords = player_dir[i.fit.read_out_coords(pipes, player_dir[i].bird.get_coordinates())
                    jump_y_n = i.fit.calc_lay(curr_coords ,initial_weights_hidden, initial_weights_out)
                    if jump_y_n == 1:
                        player_dir.bird.jump()
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