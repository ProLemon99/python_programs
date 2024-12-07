import time

# Function to introduce delay for dramatic effect
def delay_print(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()

# Start of the game
def start_game():
    delay_print("Welcome to the Adventure Game!")
    delay_print("You find yourself in a dark forest, with two paths ahead.")
    choice = input("Do you take the left path or the right path? (left/right): ").strip().lower()

    if choice == "left":
        dark_cave()
    elif choice == "right":
        mystical_lake()
    else:
        delay_print("You stand there, indecisive, and the forest swallows you whole...")
        game_over()

# Dark cave path
def dark_cave():
    delay_print("You chose the left path and find yourself in front of a dark cave.")
    choice = input("Do you enter the cave or go back? (enter/back): ").strip().lower()

    if choice == "enter":
        delay_print("You enter the cave and encounter a sleeping dragon!")
        choice = input("Do you sneak past it or try to fight it? (sneak/fight): ").strip().lower()
        
        if choice == "sneak":
            delay_print("You tiptoe past the dragon and find a treasure chest!")
            delay_print("You win!")
        elif choice == "fight":
            delay_print("The dragon wakes up and burns you to a crisp. Ouch!")
            game_over()
        else:
            delay_print("Indecision leads to the dragon waking up. You are toast!")
            game_over()
    elif choice == "back":
        delay_print("You decide to retreat and find yourself back at the fork.")
        start_game()
    else:
        delay_print("You wander aimlessly and are lost forever...")
        game_over()

# Mystical lake path
def mystical_lake():
    delay_print("You chose the right path and arrive at a mystical lake.")
    choice = input("Do you drink the water or keep walking? (drink/walk): ").strip().lower()

    if choice == "drink":
        delay_print("The water grants you superpowers! You fly away to safety.")
        delay_print("You win!")
    elif choice == "walk":
        delay_print("You keep walking and stumble upon a hidden village.")
        delay_print("The villagers welcome you, and you live happily ever after!")
        delay_print("You win!")
    else:
        delay_print("You hesitate and fall into the lake. Goodbye!")
        game_over()

# Game over function
def game_over():
    delay_print("Game over. Better luck next time!")
    replay = input("Do you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        start_game()
    else:
        delay_print("Thanks for playing! Goodbye.")
        exit()

# Run the game
start_game()