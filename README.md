# Character Journey

A Python-based game that evolves from a simple text-based adventure into a full-fledged Pygame experience. Follow the journey of creating a game from basic terminal interactions to a complete 2D platformer.

## 🎮 Project Overview

Character Journey is a learning project that starts as a terminal-based character movement system and gradually transforms into a graphical game using Pygame. This project serves both as a playable game and an educational resource for learning game development concepts.

## 🎯 Development Roadmap

1. **Phase 1: Terminal Prototype** *(Current)*
   - Basic grid-based movement
   - Simple character representation
   - Terminal-based display

2. **Phase 2: Pygame Graphics**
   - Window and rendering setup
   - Sprite-based graphics
   - Smooth movement controls

3. **Phase 3: Game Mechanics**
   - Player class implementation
   - Collision detection
   - Items and inventory system

4. **Phase 4: Level Design**
   - Multiple game levels
   - Environmental obstacles
   - Enemy AI patterns

## ✨ Features

### Current Features
- Grid-based movement system
- Player position tracking
- Terminal visualization

### Planned Features
- Smooth character controls
- Jumping mechanics
- Collectible items
- Enemy interactions
- Multiple levels

## 🛠️ Tech Stack

- Python 3.x
- Pygame (upcoming)

## 📥 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Muhsin-603/Game.git
   cd Game
   ```

2. Install required packages:
   ```bash
   # Currently no additional packages required
   # Pygame will be required in future updates
   ```

## 🎲 Usage

Run the game using Python:
```bash
python world.py
```

Follow the on-screen prompts to:
1. Enter row position (0-9)
2. Enter column position (0-4)
3. Watch your character (@) appear in the grid!

## 🌱 For Learners

This project is structured to show the evolution of a game from simple concepts to more complex implementations. Each phase builds upon the previous one, making it ideal for learning:

- Basic Python programming
- Game logic implementation
- Grid-based movement systems
- (Future) Pygame fundamentals
- (Future) Object-oriented game design

## 🤝 Contributing

Contributions are welcome! Whether you're fixing bugs, adding features, or improving documentation, please feel free to:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## 📝 Notes

- This project is under active development
- Each phase will be tagged for easy reference
- Watch this space for Pygame implementation updates!

## 🎯 Recent Updates (September 18, 2025)

### Completed Features:
- Migrated from terminal-based to Pygame window system
- Implemented proper game loop with event handling
- Added smooth WASD movement controls
- Created assets management system
- Integrated custom character sprite
- Added grid-based movement in graphical window

### Current Requirements:
- Pygame module: `pip install pygame`

### Project Structure:
```
pygame/
  ├── assets/         # Store game assets (images, sounds)
  │   └── character.png
  ├── character.py    # Character-specific code
  ├── world.py        # Main game logic and window handling
  └── README.md
```

### Controls:
- W: Move Up
- A: Move Left
- S: Move Down
- D: Move Right
- Close window to exit game
