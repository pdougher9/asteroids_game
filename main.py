import sys
import pygame
import random
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shots, Rockets
from upgrades import Upgrade


def main():
    pygame.init()
    pygame.font.init()

    font = pygame.font.Font(None, 36)

    score = 0
    score_increment = 10

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    rockets = pygame.sprite.Group()
    upgrades = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shots.containers = (shots, updatable, drawable)
    Rockets.containers = (rockets, updatable, drawable)
    Upgrade.containers = (upgrades, updatable, drawable)


    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    upgrade_spawned = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print(f"Score: {score}")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += score_increment

        for asteroid in asteroids:
            for rocket in rockets:
                if rocket.collision(asteroid):
                    rocket.kill()
                    asteroid.split()
                    score += score_increment


        for shot in shots:
            for upgrade in upgrades:
                if shot.collision(upgrade):
                    upgrade.kill()
                    player.weapon = 1

        if score >= 100 and not upgrade_spawned:
        # Create an Upgrade instance.
        # If your Upgrade class requires coordinates, pass them in (here using random positions)
            Upgrade(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            upgrade_spawned = True


        screen.fill("black")

        for drawing in drawable:
            drawing.draw(screen)

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()