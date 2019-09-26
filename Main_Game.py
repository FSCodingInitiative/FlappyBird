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
                                i.bird.jump()
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
                    (pipecollision, scored) = playbird.bird.checkCollision(pipes)
                    if not pipecollision:
                        delete_list.append(i)
                    if scored:
                        scores += 1

                    curr_coords = playbird.fit.read_out_coords(pipes, playbird.bird.get_coordinates())
                    jump_y_n = playbird.fit.calc_lay(curr_coords, playbird.initial_weights_hidden, playbird.initial_weights_out)
                    playbird.bird.distance_travelled += pipe_speed
                    if jump_y_n == 1:
                        playbird.bird.jump()
                    else:
                        pass
                    playbird.bird.show(screen)

                player_dir = [i for j, i in enumerate(player_dir) if j not in delete_list]



                score.score_up(scores)

                pygame.display.flip()


#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()