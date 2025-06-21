import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.difficulty_timer = 0.0
        self.difficulty_multiplier = 1.0
        self.current_spawn_rate = ASTEROID_SPAWN_RATE

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius, velocity)

    def update(self, dt):
        # Update difficulty
        self.difficulty_timer += dt
        if self.difficulty_timer >= DIFFICULTY_INCREASE_INTERVAL:
            self.difficulty_timer = 0
            if self.difficulty_multiplier < MAX_DIFFICULTY_MULTIPLIER:
                self.difficulty_multiplier = min(MAX_DIFFICULTY_MULTIPLIER, 
                                               self.difficulty_multiplier * ASTEROID_SPEED_INCREASE)
                self.current_spawn_rate *= SPAWN_RATE_DECREASE
                print(f"Difficulty increased! Multiplier: {self.difficulty_multiplier:.1f}")
        
        self.spawn_timer += dt
        if self.spawn_timer > self.current_spawn_rate:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            base_speed = random.randint(40, 100)
            speed = base_speed * self.difficulty_multiplier
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)