import os
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = (800, 600)
GRID_COLS = 5
GRID_ROWS = 10
CELL_SIZE = 40

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Character Journey")

# Load and scale player image
try:
    player_img = pygame.image.load(os.path.join('assets', 'Char 1.png'))
    player_img = pygame.transform.scale(player_img, (CELL_SIZE, CELL_SIZE))
except pygame.error as e:
    print(f"Couldn't load player image: {e}")
    sys.exit(1)

def draw_grid(p_r, p_c):
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)  # Draw grid cell
    
    # Draw player image instead of rectangle
    player_pos = (p_c * CELL_SIZE, p_r * CELL_SIZE)
    screen.blit(player_img, player_pos)

def main():
    # Initialize player position
    p_r, p_c = 2, 2
    clock = pygame.time.Clock()
    
    # Game loop
    running = True
    while running:
        screen.fill(BLACK)  # Clear screen
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and p_r > 0:
                    p_r -= 1
                elif event.key == pygame.K_s and p_r < GRID_ROWS - 1:
                    p_r += 1
                elif event.key == pygame.K_a and p_c > 0:
                    p_c -= 1
                elif event.key == pygame.K_d and p_c < GRID_COLS - 1:
                    p_c += 1
        
        # Draw everything
        draw_grid(p_r, p_c)
        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()