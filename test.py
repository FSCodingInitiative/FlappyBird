import sys, pygame
pygame.init()

class FlappyBird:

    def run(self):


        bird =  pygame.image.load("Graphics/Bird.png")
        bird = pygame.transform.scale(bird, (100, 100))

        #Position bird
        birdrect = bird.get_rect()
        birdrect = birdrect.move((170, 310))

        #opens screen
        screen = pygame.display.set_mode((414, 736))
        background = 99, 209, 62

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                screen.fill(background)
                screen.blit(bird, birdrect)
                #updates background
                pygame.display.flip()


if __name__ == "__main__":
    FlappyBird().run()

