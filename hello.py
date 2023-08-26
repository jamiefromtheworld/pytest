import  pygame
import time
import random

width= 750 
height =  600
win = pygame.display.set_mode( (width, height))
pygame.display.set_caption("My game")

BG = pygame.transform.scale(pygame.image.load("image.jpeg"), (width, height))

def draw():
    win.blit(BG, (0, 0))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()


    pygame.quit()
if __name__ == "__main__":
    main()



