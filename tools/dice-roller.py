import random

class Dice:
    def roll_dice(self, num_dice):
        return [random.randint(1, 6) for _ in range(num_dice)]

dice = Dice()

print("Welcome to the online dice roller.")

while True:
    try:
        num_dice = int(input("How many dice do you want to roll? (1-10): "))
        if 1 <= num_dice <= 10:
            rolled_values = dice.roll_dice(num_dice)
            print(f"You rolled: {rolled_values}")
        else:
            print("Please enter a number between 1 and 10.")
            continue

    except ValueError:
        print("Invalid input! Please enter a number.")

    reroll = input("Do you want to reroll? (Y/N): ").strip().lower()
    if reroll != 'y':
        print("Thanks for playing!")
        break