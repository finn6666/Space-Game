import pygame
from constants import *

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.large_font = pygame.font.Font(None, FONT_SIZE * 2)
        
    def draw_game_ui(self, screen, player):
        """Draw the in-game UI elements"""
        # Draw score
        score_text = self.font.render(f"Score: {player.score}", True, WHITE)
        screen.blit(score_text, (UI_PADDING, UI_PADDING))
        
        # Draw lives
        lives_text = self.font.render(f"Lives: {player.lives}", True, WHITE)
        screen.blit(lives_text, (UI_PADDING, UI_PADDING + FONT_SIZE))
        
        # Draw difficulty level (if available)
        if hasattr(player, 'asteroid_field') and hasattr(player.asteroid_field, 'difficulty_multiplier'):
            difficulty_text = self.font.render(f"Level: {player.asteroid_field.difficulty_multiplier:.1f}x", True, YELLOW)
            screen.blit(difficulty_text, (UI_PADDING, UI_PADDING + FONT_SIZE * 2))
            y_offset = UI_PADDING + FONT_SIZE * 3
        else:
            y_offset = UI_PADDING + FONT_SIZE * 2
        
        # Draw power-up status
        if player.shield_active:
            shield_text = self.font.render(f"Shield: {player.shield_timer:.1f}s", True, CYAN)
            screen.blit(shield_text, (UI_PADDING, y_offset))
            y_offset += FONT_SIZE
            
        if player.rapid_fire_active:
            rapid_text = self.font.render(f"Rapid Fire: {player.rapid_fire_timer:.1f}s", True, RED)
            screen.blit(rapid_text, (UI_PADDING, y_offset))
            y_offset += FONT_SIZE
            
        if player.triple_shot_active:
            triple_text = self.font.render(f"Triple Shot: {player.triple_shot_timer:.1f}s", True, YELLOW)
            screen.blit(triple_text, (UI_PADDING, y_offset))
            
    def draw_menu(self, screen):
        """Draw the main menu"""
        title = self.large_font.render("ASTEROIDS", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        screen.blit(title, title_rect)
        
        start_text = self.font.render("Press SPACE to Start", True, WHITE)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(start_text, start_rect)
        
        controls_text = self.font.render("WASD to move, SPACE to shoot", True, WHITE)
        controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3))
        screen.blit(controls_text, controls_rect)
        
    def draw_game_over(self, screen, player):
        """Draw the game over screen"""
        game_over_text = self.large_font.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        screen.blit(game_over_text, game_over_rect)
        
        score_text = self.font.render(f"Final Score: {player.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(score_text, score_rect)
        
        restart_text = self.font.render("Press SPACE to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3))
        screen.blit(restart_text, restart_rect)
        
    def draw_pause_screen(self, screen):
        """Draw the pause screen"""
        pause_text = self.large_font.render("PAUSED", True, YELLOW)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(pause_text, pause_rect)
        
        resume_text = self.font.render("Press P to Resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3))
        screen.blit(resume_text, resume_rect) 