import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Character")

# Create player rectangle
player = pygame.Rect(
    WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2,  # Center x position
    WINDOW_HEIGHT // 2 - PLAYER_HEIGHT // 2, # Center y position
    PLAYER_WIDTH,
    PLAYER_HEIGHT
)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill screen with background color
    screen.fill(BLACK)
    
    # Draw player rectangle
    pygame.draw.rect(screen, RED, player)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()