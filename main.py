import pygame 
from constants import *
from player import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

def main():
    print("Starting Asteroids!")
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)  # instantiate first
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        player.update(dt)
        player.draw(screen)  # draw player after clearing screen
        pygame.display.flip()

        res = clock.tick(60)
        dt = res / 1000

def WidthHeight():
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

WidthHeight()















if __name__ == "__main__":
    main()