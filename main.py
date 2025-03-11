import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shots


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shots.containers = (shots, updatable, drawable)

    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x, y)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()