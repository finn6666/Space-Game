import pygame
import random
from circleshape import CircleShape
from constants import *

class PowerUp(CircleShape):
    def __init__(self, x, y, powerup_type):
        super().__init__(x, y, 15)  # Power-ups are smaller than asteroids
        self.powerup_type = powerup_type
        self.velocity = pygame.Vector2(0, 0)  # Power-ups don't move
        self.lifetime = 10.0  # Power-ups disappear after 10 seconds
        self.timer = 0
        
    def draw(self, screen):
        # Draw power-up with different colors based on type
        color = WHITE
        if self.powerup_type == 'shield':
            color = CYAN
        elif self.powerup_type == 'rapid_fire':
            color = RED
        elif self.powerup_type == 'triple_shot':
            color = YELLOW
            
        # Draw with pulsing effect
        pulse = int(5 * (1 + 0.3 * abs(pygame.time.get_ticks() % 1000 - 500) / 500))
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius + pulse, 2)
        
        # Draw power-up symbol
        if self.powerup_type == 'shield':
            # Draw shield symbol (circle with lines)
            pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), self.radius - 5, 1)
        elif self.powerup_type == 'rapid_fire':
            # Draw rapid fire symbol (multiple dots)
            for i in range(3):
                offset = (i - 1) * 3
                pygame.draw.circle(screen, color, (int(self.position.x + offset), int(self.position.y)), 2)
        elif self.powerup_type == 'triple_shot':
            # Draw triple shot symbol (three lines)
            for i in range(3):
                angle = (i - 1) * 15
                end_pos = pygame.Vector2(0, -self.radius + 5).rotate(angle)
                pygame.draw.line(screen, color, 
                               (int(self.position.x), int(self.position.y)),
                               (int(self.position.x + end_pos.x), int(self.position.y + end_pos.y)), 2)
    
    def update(self, dt):
        self.timer += dt
        if self.timer >= self.lifetime:
            self.kill() 