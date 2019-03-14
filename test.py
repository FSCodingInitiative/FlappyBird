import sys, pygame
#Init pygame runs seperately
pygame.init()

class FlappyBird:

    def run(self):
        #screen size
        x = 414
        y = 736
        #background RGB
        background = 135, 206, 235

        #define pipe speed
        pipe_speed = 0.6


        #Bird
        #Loading and sizing
        bird =  pygame.image.load("Graphics/Bird.png")
        bird = pygame.transform.scale(bird, (100, 100))
        #Positioning
        birdrect = bird.get_rect()
        birdrect = birdrect.move((170, 310))

        #pipes
        init_pos = 200
        pipes = pygame.image.load("Graphics/pipes.png")
        pipes = pygame.transform.scale(pipes, (150, 400))
        pipesdrect = pipes.get_rect()
        pipesdrect = pipesdrect.move((init_pos, 520))

        #Reversed pipes
        #Rotates normal pipes and creates reversed as new variable
        pipes_rev = pygame.transform.rotate(pipes, 180)
        pipesrevrect = pipes_rev.get_rect()
        pipesrevrect = pipesrevrect.move((init_pos, 0))

        #opens screen
        screen = pygame.display.set_mode((x, y))


        while 1:
            #Needed to end pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Creates background
            screen.fill(background)
            #Load objects in screen

            #updates background
            pygame.display.flip()

            for i in range(10000):
                #define new position of pipe
                init_pos -= pipe_speed
                #delete old pipes on screen
                screen.fill(background)
                #create new moved pipe
                screen.blit(pipes, pipesdrect.move((init_pos, 0)))
                screen.blit(pipes_rev, pipesrevrect.move((init_pos, 0)))
                screen.blit(bird, birdrect)
                pygame.display.update()



                pygame.time.delay(2)


#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()

