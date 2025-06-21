import pygame
import random
from constants import *

class Particle:
    def __init__(self, x, y, color=WHITE):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(
            random.uniform(-100, 100),
            random.uniform(-100, 100)
        )
        self.color = color
        self.lifetime = random.uniform(0.5, 1.5)
        self.timer = 0
        self.size = random.randint(2, 5)
        
    def update(self, dt):
        self.position += self.velocity * dt
        self.velocity *= 0.98  # Friction
        self.timer += dt
        self.size = max(0, self.size - dt * 2)  # Shrink over time
        
    def is_dead(self):
        return self.timer >= self.lifetime or self.size <= 0
        
    def draw(self, screen):
        alpha = int(255 * (1 - self.timer / self.lifetime))
        color = (*self.color, alpha)
        pygame.draw.circle(screen, self.color, 
                          (int(self.position.x), int(self.position.y)), 
                          int(self.size))

class ParticleSystem:
    def __init__(self):
        self.particles = []
        
    def create_explosion(self, x, y, color=WHITE, count=10):
        """Create an explosion effect at the given position"""
        for _ in range(count):
            particle = Particle(x, y, color)
            self.particles.append(particle)
            
    def update(self, dt):
        """Update all particles"""
        self.particles = [p for p in self.particles if not p.is_dead()]
        for particle in self.particles:
            particle.update(dt)
            
    def draw(self, screen):
        """Draw all particles"""
        for particle in self.particles:
            particle.draw(screen) 