import sys, pygame
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
        pipe_speed = 3


        #Bird
        #Loading and sizing
        bird =  pygame.image.load("Graphics/Bird.png")
        bird = pygame.transform.scale(bird, (100, 100))
        #Positioning
        birdrect = bird.get_rect()
        birdrect = birdrect.move((0, 0))

        def create_pipe(xpos, ypos):
            rev_pipe_ypos = ypos - 500
            pipes = pygame.image.load("Graphics/pipes.png")
            pipes = pygame.transform.scale(pipes, (197, 400))
            pipes_rev = pygame.transform.rotate(pipes, 180)
            pipes_rect = pipes.get_rect()
            pipes_rect = pipes_rect.move((xpos, ypos))
            pipes_rev_rect = pipes_rev.get_rect()
            pipes_rev_rect = pipes_rev_rect.move((xpos, rev_pipe_ypos))

            return pipes, pipes_rev, pipes_rect, pipes_rev_rect

        pipes, pipes_rev, pipes_rect, pipes_rev_rect = create_pipe(500, 300)
        #opens screen
        screen = pygame.display.set_mode((x, y))

        """"#create additional pipes
        pipes_2 = pipes_1.move((197, 0))
        pipes_r2 = pipes_r1.move((197, y_ax_init_r))
        init_pos2 = init_pos

        pipes_3 = pipes_1.move((197*2, 0))
        pipes_r3 = pipes_r1.move((197*2, y_ax_init_r))
        init_pos3 = init_pos




        #list with positions of every pipe
        pipe_pos = [init_pos,init_pos2,init_pos3]

        #list of pipes
        pipe_list = [pipes_1, pipes_2, pipes_3]

        #list of reversed pipes
        pipe_r_list = [pipes_r1, pipes_r2, pipes_r3]"""



        while 1:
            #Needed to end pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Creates background
            screen.fill(background)

            #define new position of pipe
            """for index, val in enumerate(pipe_pos):
                if (val -index*197) <= -197*2:
                    pipe_pos[index] = 1200-197
                    print("now", index)
                else:
                    pipe_pos[index] -= pipe_speed
                    print("index", index, "val", val)
            #delete old pipes on screen
            screen.fill(background)
            #create new moved pipe

            for i in range(0,len(pipe_list)):
                screen.blit(pipes, pipe_list[i].move((pipe_pos[i], y_ax_init)))
                screen.blit(pipes_rev, pipe_r_list[i].move((pipe_pos[i], y_ax_init_r)))"""

            screen.blit(pipes_rev,pipes_rev_rect)
            screen.blit(pipes,pipes_rect)

            screen.blit(bird, birdrect)
            pygame.display.update()



#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()
