# Enhanced Asteroids Game

A modern implementation of the classic Asteroids arcade game with enhanced features and visual effects.

## Features

### Core Gameplay
- **Classic Asteroids mechanics**: Destroy asteroids to score points
- **Player movement**: WASD controls for movement and rotation
- **Shooting**: Spacebar to fire projectiles
- **Asteroid splitting**: Large asteroids break into smaller pieces when hit
- **Screen wrapping**: Objects wrap around screen edges

### Enhanced Features

#### 🎯 Scoring System
- **Large asteroids**: 100 points
- **Medium asteroids**: 50 points  
- **Small asteroids**: 25 points
- Score display in real-time

#### ❤️ Lives System
- **3 starting lives** instead of instant game over
- **Invulnerability period** after being hit
- Visual flashing effect during invulnerability
- Lives counter display

#### ⚡ Power-ups
- **Shield** (Cyan): Protects from asteroid collisions for 5 seconds
- **Rapid Fire** (Red): Triples firing rate for 5 seconds
- **Triple Shot** (Yellow): Fires three projectiles at once for 5 seconds
- **10% chance** to spawn when destroying asteroids
- **Visual indicators** for active power-ups
- **Timer display** for remaining duration

#### 🎮 Game States
- **Main Menu**: Press SPACE to start
- **Playing**: Active gameplay
- **Pause**: Press P to pause/resume
- **Game Over**: Display final score, press SPACE to restart
- **Escape key**: Return to menu or quit

#### 📈 Difficulty Progression
- **Automatic difficulty increase** every 30 seconds
- **Faster asteroid spawning** over time
- **Increased asteroid speed** as difficulty rises
- **Maximum 3x difficulty multiplier**
- **Level display** in UI

#### ✨ Visual Effects
- **Particle explosion effects** when asteroids are destroyed
- **Player hit effects** with red particles
- **Power-up collection effects** with colored particles
- **Pulsing power-up animations**
- **Invulnerability flashing**

#### 🎨 UI Improvements
- **Real-time score display**
- **Lives counter**
- **Difficulty level indicator**
- **Active power-up timers**
- **Game state screens** (menu, pause, game over)
- **Color-coded information**

## Controls

| Key | Action |
|-----|--------|
| **W** | Move forward |
| **S** | Move backward |
| **A** | Rotate left |
| **D** | Rotate right |
| **SPACE** | Shoot / Start game / Restart |
| **P** | Pause/Resume |
| **ESC** | Return to menu / Quit |

## Power-up Types

### 🛡️ Shield (Cyan)
- **Effect**: Protects from asteroid collisions
- **Duration**: 5 seconds
- **Visual**: Cyan circle around player

### 🔥 Rapid Fire (Red)
- **Effect**: Triples firing rate
- **Duration**: 5 seconds
- **Visual**: Red particles when collected

### 🎯 Triple Shot (Yellow)
- **Effect**: Fires three projectiles at different angles
- **Duration**: 5 seconds
- **Visual**: Yellow particles when collected

## Game Mechanics

### Scoring
- Destroy asteroids to earn points
- Larger asteroids give more points
- Score persists until game over

### Difficulty
- Game starts at normal speed
- Every 30 seconds, difficulty increases
- Asteroid speed and spawn rate increase
- Maximum difficulty is 3x normal

### Collision Detection
- Player collision with asteroids reduces lives
- Invulnerability period after being hit
- Shield power-up blocks damage
- Shots destroy asteroids on contact

## File Structure

```
Pygame/
├── main.py              # Main game loop and state management
├── player.py            # Player class with movement and power-ups
├── asteroid.py          # Asteroid class with splitting and scoring
├── asteroidfield.py     # Asteroid spawning and difficulty management
├── shot.py              # Projectile class
├── powerup.py           # Power-up system
├── particles.py         # Particle effects system
├── ui.py                # User interface and text rendering
├── circleshape.py       # Base class for circular game objects
├── constants.py         # Game constants and configuration
└── README.md           # This file
```

## Installation

1. Ensure you have Python 3.6+ installed
2. Install pygame: `pip install pygame`
3. Run the game: `python main.py`

## Future Enhancements

Potential features for future versions:
- Sound effects and background music
- High score system with file persistence
- Multiple weapon types
- Boss asteroids
- Multiplayer support
- Different asteroid types with unique behaviors
- Achievement system
- Customizable controls

## Credits

This is an enhanced version of the classic Asteroids arcade game, originally created by Atari in 1979. The implementation uses Pygame for graphics and game logic. 