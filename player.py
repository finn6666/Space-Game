from circleshape import *
from constants import *
from shot import *

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0
        self.timer = 0
        self.lives = PLAYER_STARTING_LIVES
        self.score = 0
        self.shield_active = False
        self.shield_timer = 0
        self.rapid_fire_active = False
        self.rapid_fire_timer = 0
        self.triple_shot_active = False
        self.triple_shot_timer = 0
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.invulnerable_duration = 2.0  # seconds of invulnerability after being hit
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        add = PLAYER_TURN_SPEED * dt
        self.rotation += add

    def update(self, dt):
        self.timer -= dt 
        
        # Update power-up timers
        if self.shield_active:
            self.shield_timer -= dt
            if self.shield_timer <= 0:
                self.shield_active = False
                
        if self.rapid_fire_active:
            self.rapid_fire_timer -= dt
            if self.rapid_fire_timer <= 0:
                self.rapid_fire_active = False
                
        if self.triple_shot_active:
            self.triple_shot_timer -= dt
            if self.triple_shot_timer <= 0:
                self.triple_shot_active = False
                
        if self.invulnerable:
            self.invulnerable_timer -= dt
            if self.invulnerable_timer <= 0:
                self.invulnerable = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot(Shot)
                cooldown = PLAYER_SHOOT_COOLDOWN / 3 if self.rapid_fire_active else PLAYER_SHOOT_COOLDOWN
                self.timer = cooldown
               
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
        # Wrap around screen edges
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
    
    def draw(self, screen):
        # Draw player with invulnerability flashing
        if not self.invulnerable or int(pygame.time.get_ticks() / 100) % 2:
            pygame.draw.polygon(screen, WHITE, self.triangle(), 2)
        
        # Draw shield if active
        if self.shield_active:
            pygame.draw.circle(screen, CYAN, self.position, self.radius + 10, 3)

    def shoot(self, shots):
        if self.triple_shot_active:
            # Triple shot - fire three shots at different angles
            angles = [-15, 0, 15]
            for angle in angles:
                direction = pygame.Vector2(0, 1)
                direction = direction.rotate(self.rotation + angle)
                shot = Shot(self.position.x, self.position.y)
                shot.velocity = direction * PLAYER_SHOOT_SPEED
        else:
            # Single shot
            direction = pygame.Vector2(0, 1)
            direction = direction.rotate(self.rotation)
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = direction * PLAYER_SHOOT_SPEED

    def take_damage(self):
        if not self.invulnerable and not self.shield_active:
            self.lives -= 1
            self.invulnerable = True
            self.invulnerable_timer = self.invulnerable_duration
            return True
        return False
    
    def activate_powerup(self, powerup_type):
        if powerup_type == 'shield':
            self.shield_active = True
            self.shield_timer = POWERUP_DURATION
        elif powerup_type == 'rapid_fire':
            self.rapid_fire_active = True
            self.rapid_fire_timer = POWERUP_DURATION
        elif powerup_type == 'triple_shot':
            self.triple_shot_active = True
            self.triple_shot_timer = POWERUP_DURATION
    
    def add_score(self, points):
        self.score += points
 
