
choice = 'y'
while choice != 'n':
    print("Enter the position of player :- ")
    p_r = input("row: ")
    p_c = input("column: ")
    for i in range (10):
        for j in range (5):
            if i == int(p_r) and j == int(p_c):
                print("@", end=" ")  # Print '@' for player position
            else:
                print("*", end=" ")    # Add space between asterisks
        print()
    choice = input("Do you want to change the position of player? (y/n): ") #menu to change player position

                    # Add new line after each row