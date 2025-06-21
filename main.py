import pygame 
from asteroid import *
from constants import *
from asteroidfield import *
from player import *
from circleshape import *
from powerup import *
from ui import *
from particles import *
import sys
import random

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")

# Game state
game_state = GAME_MENU
paused = False

# Sprite groups
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
powerups = pygame.sprite.Group()

# Set up sprite containers
Player.containers = (updatable, drawable)
Shot.containers = (shots, updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
PowerUp.containers = (powerups, updatable, drawable)

clock = pygame.time.Clock()
ui = UI()
particle_system = ParticleSystem()

def reset_game():
    """Reset the game to initial state"""
    global game_state, paused
    
    # Clear all sprite groups
    updatable.empty()
    drawable.empty()
    asteroids.empty()
    shots.empty()
    powerups.empty()
    
    # Create new player and asteroid field
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    AsteroidField.containers = (updatable,)
    asteroidField = AsteroidField()
    
    # Connect asteroid field to player for UI display
    player.asteroid_field = asteroidField
    
    game_state = GAME_PLAYING
    paused = False
    
    return player, asteroidField

def handle_events():
    """Handle pygame events"""
    global game_state, paused
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_state == GAME_MENU:
                    game_state = GAME_PLAYING
                elif game_state == GAME_OVER:
                    game_state = GAME_MENU
            elif event.key == pygame.K_p and game_state == GAME_PLAYING:
                paused = not paused
            elif event.key == pygame.K_ESCAPE:
                if game_state == GAME_PLAYING:
                    game_state = GAME_MENU
                else:
                    return False
    return True

def update_game(dt, player, asteroidField):
    """Update game logic"""
    if paused:
        return
        
    # Update all game objects
    updatable.update(dt)
    particle_system.update(dt)
    
    # Check player collision with asteroids
    for asteroid in asteroids:
        if asteroid.coll_detect(player):
            if player.take_damage():
                print(f'Player hit! Lives remaining: {player.lives}')
                # Create explosion effect
                particle_system.create_explosion(int(player.position.x), int(player.position.y), RED, 15)
                if player.lives <= 0:
                    return GAME_OVER
    
    # Check shot collision with asteroids
    for shot in shots:
        for asteroid in asteroids:
            if asteroid.coll_detect(shot):
                # Add score
                score = asteroid.split(asteroids)
                player.add_score(score)
                shot.kill()
                
                # Create explosion effect
                particle_system.create_explosion(int(asteroid.position.x), int(asteroid.position.y), WHITE, 8)
                
                # Chance to spawn power-up
                if random.random() < POWERUP_SPAWN_RATE:
                    powerup_type = random.choice(POWERUP_TYPES)
                    powerup = PowerUp(int(asteroid.position.x), int(asteroid.position.y), powerup_type)
                    powerups.add(powerup)
                break
    
    # Check player collision with power-ups
    for powerup in powerups:
        if powerup.coll_detect(player):
            player.activate_powerup(powerup.powerup_type)
            powerup.kill()
            # Create power-up collection effect
            color = CYAN if powerup.powerup_type == 'shield' else RED if powerup.powerup_type == 'rapid_fire' else YELLOW
            particle_system.create_explosion(int(powerup.position.x), int(powerup.position.y), color, 5)
            print(f'Power-up collected: {powerup.powerup_type}')
    
    # Clean up shots that are off screen
    for shot in shots:
        if (shot.position.x < -50 or shot.position.x > SCREEN_WIDTH + 50 or 
            shot.position.y < -50 or shot.position.y > SCREEN_HEIGHT + 50):
            shot.kill()
    
    return GAME_PLAYING

def draw_game(screen, player):
    """Draw the game"""
    screen.fill(BLACK)
    
    # Draw all game objects
    for sprite in drawable:
        sprite.draw(screen)
    
    # Draw particles
    particle_system.draw(screen)
    
    # Draw UI
    ui.draw_game_ui(screen, player)
    
    if paused:
        ui.draw_pause_screen(screen)

def main():
    global game_state, paused
    
    print("Starting Asteroids!")
    player = None
    asteroidField = None
    
    while True:
        # Handle events
        if not handle_events():
            break
        
        # Game state management
        if game_state == GAME_MENU:
            if player is None:
                player, asteroidField = reset_game()
            screen.fill(BLACK)
            ui.draw_menu(screen)
            
        elif game_state == GAME_PLAYING:
            if player is None:
                player, asteroidField = reset_game()
            
            dt = clock.tick(60) / 1000.0
            
            # Update game
            new_state = update_game(dt, player, asteroidField)
            if new_state == GAME_OVER:
                game_state = GAME_OVER
            else:
                # Draw game
                draw_game(screen, player)
                
        elif game_state == GAME_OVER:
            screen.fill(BLACK)
            ui.draw_game_over(screen, player)
            player = None  # Reset player for next game
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()