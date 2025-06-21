from circleshape import *
from constants import (ASTEROID_MIN_RADIUS, SCORE_LARGE_ASTEROID, SCORE_MEDIUM_ASTEROID, 
                      SCORE_SMALL_ASTEROID, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT)
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity 
        
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
        # Wrap around screen edges
        if self.position.x < -self.radius:
            self.position.x = SCREEN_WIDTH + self.radius
        elif self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y < -self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius
        elif self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius

    def get_score_value(self):
        """Return score value based on asteroid size"""
        if self.radius >= ASTEROID_MIN_RADIUS * 3:
            return SCORE_LARGE_ASTEROID
        elif self.radius >= ASTEROID_MIN_RADIUS * 2:
            return SCORE_MEDIUM_ASTEROID
        else:
            return SCORE_SMALL_ASTEROID

    def split(self, asteroids_group):
        score_value = self.get_score_value()
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return score_value
        else:
            randon_ang = random.uniform(20, 50)
            one_way = self.velocity.rotate(randon_ang)
            other_way = self.velocity.rotate(-randon_ang)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(int(self.position.x), int(self.position.y), new_radius, one_way * 1.2)
            asteroid2 = Asteroid(int(self.position.x), int(self.position.y), new_radius, other_way * 1.2)
            asteroids_group.add(asteroid1)
            asteroids_group.add(asteroid2)
            return score_value
