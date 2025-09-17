import os
import time  # Add this for a small delay between frames

def clear_screen():
    # Clear command for Windows
    _ = os.system('cls')

def move_player(move, p_r, p_c):
    if move == 'W' and p_r > 0:
        p_r -= 1
    elif move == 'S' and p_r < 9:
        p_r += 1
    elif move == 'A' and p_c > 0:
        p_c -= 1
    elif move == 'D' and p_c < 4:
        p_c += 1
    return p_r, p_c

def print_grid(p_r, p_c):
    for i in range(5):  # Changed to 5 rows
        for j in range(5):
            if i == p_r and j == p_c:
                print("@", end=" ")
            else:
                print("*", end=" ")
        print()

# Initialize player position
p_r, p_c = 2, 2

# Main game loop
while True:
    clear_screen()
    print_grid(p_r, p_c)
    print("\nUse WASD to move, press Ctrl+C to quit")
    move = input("Move: ").upper()
    p_r, p_c = move_player(move, p_r, p_c)
    time.sleep(0.1)  # Small delay to prevent screen flicker