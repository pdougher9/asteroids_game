from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, ROCKET_RADIUS


class Shots(CircleShape):
    def __init__(self, x , y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, color="blue", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt


class Rockets(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, ROCKET_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, color="red", center=self.position, radius=self.radius, width=3)

    def update(self, dt):
        self.position += self.velocity * dt * 1.5