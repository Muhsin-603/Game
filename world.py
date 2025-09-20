import os
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = (800, 600)
GRID_COLS = 20
GRID_ROWS = 15
CELL_SIZE = 40
GAME_OVER_COLOR = (255, 0, 0)

# Calculate grid offset to center it in window
GRID_WIDTH = GRID_COLS * CELL_SIZE
GRID_HEIGHT = GRID_ROWS * CELL_SIZE
GRID_X_OFFSET = (WINDOW_SIZE[0] - GRID_WIDTH) // 2
GRID_Y_OFFSET = (WINDOW_SIZE[1] - GRID_HEIGHT) // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up display
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Character Journey")

# Load and scale player image
try:
    player_img = pygame.image.load(os.path.join("assets", "Char 1.png"))
    player_img = pygame.transform.scale(player_img, (CELL_SIZE, CELL_SIZE))
except pygame.error as e:
    print(f"Couldn't load player image: {e}")
    sys.exit(1)

# Enemy settings
ENEMY_PATH = [(5, 5), (5, 15), (10, 15), (10, 5)]
DETECTION_RANGE = 3
ALTERNATE_PATH = [(2, 2), (2, 17), (12, 17), (12, 2)]

# Load enemy sprite
try:
    enemy_img = pygame.image.load(os.path.join("assets", "enemy.png"))
    enemy_img = pygame.transform.scale(enemy_img, (CELL_SIZE, CELL_SIZE))
except pygame.error as e:
    print(f"Couldn't load enemy image: {e}")
    sys.exit(1)

# Load door image
try:
    door_img = pygame.image.load(os.path.join('assets', 'Door.png'))  # Note the capital 'D' if that's the actual filename
    # Scale door image to fit two vertical cells
    door_img = pygame.transform.scale(door_img, (CELL_SIZE, CELL_SIZE * 2))
except pygame.error as e:
    print(f"Couldn't load door image: {e}")
    sys.exit(1)

# Add door position constants
DOOR_COL = GRID_COLS - 1  # Door at rightmost column
DOOR_ROW = GRID_ROWS - 2  # Door position allowing 2 vertical cells

class Enemy:
    def __init__(self):
        self.path = ENEMY_PATH.copy()
        self.current_point = 0
        self.position = list(self.path[0])
        self.is_alerted = False
        self.chase_range = 1  # Distance to start chasing player

    def move(self, player_pos):
        """Move enemy towards player or patrol. Return True if player is caught."""
        dist_row = abs(self.position[0] - player_pos[0])
        dist_col = abs(self.position[1] - player_pos[1])

        # ✅ Check if player is already caught
        if dist_row == 0 and dist_col == 0:
            return True   # enemy is standing on the player

        # ✅ Chase if player is near
        if dist_row <= self.chase_range and dist_col <= self.chase_range:
            if self.position[0] < player_pos[0]:
                self.position[0] += 1
            elif self.position[0] > player_pos[0]:
                self.position[0] -= 1
            elif self.position[1] < player_pos[1]:
                self.position[1] += 1
            elif self.position[1] > player_pos[1]:
                self.position[1] -= 1

            # Check again after moving
            return self.position == list(player_pos)

        # ✅ Switch patrol path if player in detection range
        if dist_row <= DETECTION_RANGE and dist_col <= DETECTION_RANGE:
            if not self.is_alerted:
                self.path = ALTERNATE_PATH.copy()
                self.current_point = 0
                self.is_alerted = True
        else:
            if self.is_alerted:
                self.path = ENEMY_PATH.copy()
                self.current_point = 0
                self.is_alerted = False

        # ✅ Patrol movement
        target = self.path[self.current_point]
        if self.position[0] < target[0]:
            self.position[0] += 1
        elif self.position[0] > target[0]:
            self.position[0] -= 1
        elif self.position[1] < target[1]:
            self.position[1] += 1
        elif self.position[1] > target[1]:
            self.position[1] -= 1
        else:
            self.current_point = (self.current_point + 1) % len(self.path)

        return False

def draw_grid(p_r, p_c, enemy):
    """Draw the grid, enemy, and player."""
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            rect = pygame.Rect(
                GRID_X_OFFSET + j * CELL_SIZE,
                GRID_Y_OFFSET + i * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, WHITE, rect, 1)

    # Draw door (before player and enemy to layer correctly)
    door_pos = (
        GRID_X_OFFSET + DOOR_COL * CELL_SIZE,
        GRID_Y_OFFSET + DOOR_ROW * CELL_SIZE,
    )
    screen.blit(door_img, door_pos)

    # Enemy
    enemy_pos = (
        GRID_X_OFFSET + enemy.position[1] * CELL_SIZE,
        GRID_Y_OFFSET + enemy.position[0] * CELL_SIZE,
    )
    screen.blit(enemy_img, enemy_pos)

    # Player
    player_pos = (
        GRID_X_OFFSET + p_c * CELL_SIZE,
        GRID_Y_OFFSET + p_r * CELL_SIZE,
    )
    screen.blit(player_img, player_pos)

def check_win(p_r, p_c):
    """Check if player has reached the door"""
    return p_c == DOOR_COL and (p_r == DOOR_ROW or p_r == DOOR_ROW + 1)

# Global variables for game state
global_p_r = 2
global_p_c = 2
global_enemy = None
global_game_over = False


def reset_game():
    """Reset player and enemy to starting positions."""
    global global_p_r, global_p_c, global_enemy, global_game_over
    global_p_r = 2
    global_p_c = 2
    global_enemy = Enemy()
    global_game_over = False
    return global_p_r, global_p_c, global_enemy, global_game_over


def check_game_over():
    """Return True if player is out of bounds or caught by the enemy."""
    if (
        global_p_r < 0
        or global_p_r >= GRID_ROWS
        or global_p_c < 0
        or global_p_c >= GRID_COLS
    ):
        return True
    return global_enemy.move((global_p_r, global_p_c))


def draw_game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, GAME_OVER_COLOR)
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))
    screen.blit(text, text_rect)

    font_small = pygame.font.Font(None, 36)
    restart_text = font_small.render("Press SPACE to restart", True, WHITE)
    restart_rect = restart_text.get_rect(center=(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2 + 50))
    screen.blit(restart_text, restart_rect)
def draw_you_win():
    font = pygame.font.Font(None, 74)
    text = font.render("You Win!", True, (0, 255, 0))
    text_rect = text.get_rect(center=(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2))
    screen.blit(text, text_rect)

    font_small = pygame.font.Font(None, 36)
    restart_text = font_small.render("Press SPACE to restart", True, WHITE)
    restart_rect = restart_text.get_rect(center=(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2 + 50))
    screen.blit(restart_text, restart_rect)

def main():
    global global_p_r, global_p_c, global_enemy, global_game_over
    global_p_r, global_p_c, global_enemy, global_game_over = reset_game()
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global_p_r, global_p_c, global_enemy, global_game_over = reset_game()
                elif not global_game_over:
                    old_pos = [global_p_r, global_p_c]
                    if event.key == pygame.K_w and global_p_r > 0:
                        global_p_r -= 1
                    elif event.key == pygame.K_s and global_p_r < GRID_ROWS - 1:
                        global_p_r += 1
                    elif event.key == pygame.K_a and global_p_c > 0:
                        global_p_c -= 1
                    elif event.key == pygame.K_d and global_p_c < GRID_COLS - 1:
                        global_p_c += 1
                    
                    # Move enemy when player moves
                    if old_pos != [global_p_r, global_p_c]:
                        global_game_over = global_enemy.move((global_p_r, global_p_c))
                        
                        # Check for win condition after movement
                        if check_win(global_p_r, global_p_c):
                            # Handle win condition (you can add your own win screen)
                            print("You Win!")
                            global_game_over = True

        draw_grid(global_p_r, global_p_c, global_enemy)
        if global_game_over:
            if check_win(global_p_r, global_p_c):
                # Draw win screen
                font = pygame.font.Font(None, 74)
                text = font.render('You Win!', True, (0, 255, 0))
                text_rect = text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2))
                screen.blit(text, text_rect)
            else:
                draw_game_over()
                
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
