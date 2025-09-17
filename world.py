def move_player(move, p_r, p_c):
    if move == 'W' and p_r > 0:
        p_r -= 1
    elif move == 'S' and p_r < 9:  # Changed to 9 for 10x5 grid
        p_r += 1
    elif move == 'A' and p_c > 0:
        p_c -= 1
    elif move == 'D' and p_c < 4:  # Keep at 4 for 5 columns
        p_c += 1
    
    return p_r, p_c

def print_grid(p_r, p_c):
    for i in range(10):
        for j in range(5):
            if i == p_r and j == p_c:
                print("@", end=" ")
            else:
                print("*", end=" ")
        print()  # New line after each row

# Initialize player position
p_r, p_c = 2, 2  # Starting position
choice = 'y'

while choice != 'n':
    print_grid(p_r, p_c)  # Display current grid
    move = input("Move (W,A,S,D): ").upper()
    p_r, p_c = move_player(move, p_r, p_c)
    choice = input("Continue? (y/n): ")