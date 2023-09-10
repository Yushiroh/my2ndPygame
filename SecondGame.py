import pygame
import sys
import random

gameWidth, gameHeight = 600, 300
gameWindow = pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption("Dice and Coins")
gameFPS = 60
pygame.init()

#Colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)

#game Assets
gameFont = pygame.font.SysFont('arial', 30)



def drawWindow(diceRolled, coinState):
    gameWindow.fill(BLACK)
    pygame.draw.circle(gameWindow, WHITE, (gameWidth/4, gameHeight/2), 50)
    pygame.draw.rect(gameWindow, WHITE, (365, 100, 100, 100))
    rollForDice = gameFont.render("'D' to roll Dice and  'C' to flip Coin", 1, WHITE)
    gameWindow.blit(rollForDice, (50, 250, 100, 100))
    diceVal = gameFont.render( str(diceRolled) , 1, BLACK)
    gameWindow.blit(diceVal, (400,130,0,0))
    coinVal = gameFont.render(coinState, 1, BLACK)
    gameWindow.blit(coinVal, (115,130,0,0))

    pygame.display.update()


def main():  
    diceRolled = 0
    coinState = "Heads"
    coin = ["Heads", "Tails"]

    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(gameFPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:
                    diceRolled = random.randint(1,6)
                    print(diceRolled)

                if event.key == pygame.K_c:
                    flip = random.randint(0,1)
                    coinState = coin[flip]
                    print(coin[flip])
                    

        drawWindow(diceRolled, coinState)
        print(pygame.mouse.get_pos())
    main()

if __name__ == "__main__":
    main()
