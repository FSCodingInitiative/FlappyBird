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

        #Bird
        #Loading and sizing
        bird =  pygame.image.load("Graphics/Bird.png")
        bird = pygame.transform.scale(bird, (100, 100))
        #Positioning
        birdrect = bird.get_rect()
        birdrect = birdrect.move((170, 310))

        #pipes
        pipes = pygame.image.load("Graphics/pipes.png")
        pipes = pygame.transform.scale(pipes, (150, 250))
        pipesdrect = pipes.get_rect()
        pipesdrect = pipesdrect.move((200, 400))

        #Reversed pipes
        #Rotates normal pipes and creates reversed as new variable
        pipes_rev = pygame.transform.rotate(pipes, 180)
        pipesrevrect = pipes_rev.get_rect()
        pipesrevrect = pipesrevrect.move((200, 0))

        #opens screen
        screen = pygame.display.set_mode((x, y))


        while 1:
            #Needed to end pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                #Creates background
                screen.fill(background)
                #Load objects in screen
                screen.blit(pipes, pipesdrect)
                screen.blit(pipes_rev, pipesrevrect)
                screen.blit(bird, birdrect)
                #updates background
                pygame.display.flip()

#Makes it possible to run code with terminal and without creating new objects
if __name__ == "__main__":
    FlappyBird().run()

