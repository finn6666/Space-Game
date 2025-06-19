from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity 
    def draw(self,screen):
            pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt) 

    def split(self, asteroids_group):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
             return 
        else:
             randon_ang = random.uniform(20, 50)
             one_way = self.velocity.rotate(randon_ang)
             other_way = self.velocity.rotate(-randon_ang)
             new_radius = self.radius - ASTEROID_MIN_RADIUS
             asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, one_way * 1.2)
             asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, other_way * 1.2)
             asteroids_group.add(asteroid1)
             asteroids_group.add(asteroid2)
