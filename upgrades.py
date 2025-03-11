import pygame
import random
from circleshape import CircleShape
from constants import UPGRADE_RADIUS

class Upgrade(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, UPGRADE_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, color="green", center=self.position, radius=self.radius, width=4)

    def update(self, dt):
        self.position += self.velocity * dt * 0.5