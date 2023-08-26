import  pygame
import time
import random

width= 750 
height =  600
win = pygame.display.set_mode( (width, height))
pygame.display.set_caption("My game")

BG = pygame.transform.scale(pygame.image.load("image.jpeg"), (width, height))
player_width = 40
player_height =  60
player_vel = 5

def draw(player):
    win.blit(BG, (0, 0))
    pygame.draw.rect(win, "red", player)
    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, height - player_height, player_width, player_height)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT]:
            player.x  -=  player_vel

        elif keys [pygame.K_RIGHT]:
            player.x += player_vel

        elif keys [pygame.K_UP]:
            player.y -= player_vel

        elif keys [pygame.K_DOWN]:
            player.y += player_vel
            
        draw(player)


    pygame.quit()
if __name__ == "__main__":
    main()



