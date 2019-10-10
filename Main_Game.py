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
    rounds_per_gen = 7 #actual rounds are equal to n-1

    def __init__(self):
        self.round_per_gen = 1
        self.gen = 1
        self.bird_number = 20
        self.scores = 0
        self.pic = pg.transform.scale(pg.image.load("Graphics/Bird.png"), (100, 100))

    def run(self):
        #screen size
        x = 1200
        y = 800
        #background RGB
        background = 135, 206, 235

        #define pipe speed
        pipe_speed = 5
        player_dir = self.reset()

        #bird = Bird(300,300)
        #player = Player(bird)

        # opens screen
        screen = pygame.display.set_mode((x, y))

        score = Score(600, 100, screen)

        framecount = 0

        pipes = self.reset_pipes()

        while 1:
            game_run = True
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
            score.score_up(self.scores)
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

                #Creates background
                screen.fill(background)

                #define new position of pipe
                pipe_pop = -1
                ypos = random.randint(320, 900)
                for i, pipePair in enumerate(pipes):
                    pipePair.move_x(-pipe_speed)

                    if pipePair.get_x() <= -190:
                        pipe_pop = i
                if pipe_pop > -1:
                    pipes.pop(pipe_pop)
                    pipes.append(PipePair(3790, ypos))

                for p in pipes:
                    p.show(screen)
                delete_list = []
                for i, playbird in enumerate(player_dir):
                    playbird.bird.calcNewPos()
                    (pipecollision, scored) = playbird.bird.checkCollision(pipes)
                    if not pipecollision:
                        delete_list.append(i)
                    if scored:
                        self.scores += 1

                    curr_coords = playbird.fit.read_out_coords(pipes, playbird.bird.get_coordinates())
                    jump_y_n = playbird.fit.calc_lay(curr_coords, playbird.fit.hidden_weights, playbird.fit.out_weights)
                    playbird.bird.distance_travelled += pipe_speed
                    if jump_y_n == 1:
                        playbird.bird.jump()
                    else:
                        pass
                    playbird.bird.show(screen)


                if len(player_dir) == len(delete_list):
                    adjust_list = [p for p in player_dir]
                player_dir = [i for j, i in enumerate(player_dir) if j not in delete_list]
                if len(player_dir) == 0:
                    game_run = False
                    self.round_per_gen += 1
                    if self.round_per_gen == FlappyBird.rounds_per_gen:
                        self.gen += 1
                        self.round_per_gen = 1
                    player_dir = self.reset(adjust_list)
                    pipes = self.reset_pipes()

                score.score_up(self.scores)

                pygame.display.flip()

    def reset(self, adjust_list = []):
        print("Generation:", self.gen)
        print("Round:", self.round_per_gen)
        player_dir = []
        self.scores = 0
        if len(adjust_list) > 0:
            for i, adjuster in enumerate(adjust_list):
                adjuster.fit.print()
                for j in range(int(self.bird_number / len(adjust_list))) :
                    player_dir.append(Player(Bird(300, 300,self.pic), self.gen, adjuster.fit.hidden_weights, adjuster.fit.out_weights))
            for i in range(self.bird_number - len(player_dir)):
                player_dir.append(Player(Bird(300, 300,self.pic)))
        else:
            for i in range(self.bird_number):
                player_dir.append(Player(Bird(300, 300,self.pic)))
        return player_dir
    def reset_pipes(self):
        pipes = []
        for i in range(1,4):
            ypos = np.random.randint(400, 610, [1,1])[0][0]
            pipes.append(PipePair(i*1200, ypos))
        return pipes

#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    game = FlappyBird()
    game.run()