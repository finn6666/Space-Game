import pygame 
from asteroid import *
from constants import *
from asteroidfield import *
from player import *
from circleshape import *
import sys

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
splits = pygame.sprite.Group()
bullets = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Shot.containers = (shots,updatable, drawable)
Asteroid.containers = (asteroids, splits,updatable, drawable) 

clock = pygame.time.Clock()

def main():
    print("Starting Asteroids!")
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    AsteroidField.containers = (updatable,)
    asteroidField = AsteroidField()# instantiate first
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        updatable.update(dt)
        for a in asteroids:
            if a.coll_detect(player):
                    print('Game over!')
                    sys.exit()
        for b in asteroids:
            for a in shots:
                if b.coll_detect(a):
                    b.split(asteroids)
                    a.kill()
        for k in drawable:
            k.draw(screen)
        pygame.display.flip()
        

        res = clock.tick(60)
        dt = res / 1000

def WidthHeight():
    print(f'Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}')

WidthHeight()


if __name__ == "__main__":
    main()