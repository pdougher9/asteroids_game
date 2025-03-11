import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from shots import Shots, Rockets

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.weapon = 0 #! 0 = normal shots, 1 = rockets

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, color="white", points=self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            # ? LEFT TURN
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # ? RIGHT TURN
            self.rotate(dt)
        if keys[pygame.K_w]:
            # ? MOVE FORWARD
            self.move(dt)
        if keys[pygame.K_s]:
            # ? MOVE BACKWARD
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown > 0:
                pass
            else:
                self.shoot()
                self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.weapon == 0:
            shot = Shots(self.position.x, self.position.y)
            shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)
        elif self.weapon == 1:
            shot = Rockets(self.position.x, self.position.y)
            shot.velocity = (pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)
        