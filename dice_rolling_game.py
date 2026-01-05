import random

# Dice symbols for numbers 1 to 6
dice_symbols = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

roll_count = 0

while True:
    choice = input("Roll the dice? (y / n): ").lower()

    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        roll_count += 1

        print(f"Roll #{roll_count}")
        print(f"Dice 1: {dice_symbols[die1]} ({die1})")
        print(f"Dice 2: {dice_symbols[die2]} ({die2})")
        print("-" * 20)

    elif choice == 'n':
        print("Thank you for playing!")
        print(f"Total rolls: {roll_count}")
        break

    else:
        print("Invalid choice! Please enter y or n.")
