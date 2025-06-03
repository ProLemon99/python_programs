import random
import time

def play_game():
    print("\n🎲 WELCOME TO TERMINAL RUSSIAN ROULETTE 🎲")
    print("One chamber has a bullet. How long can you survive?\n")

    bullet_chamber = random.randint(1, 6)
    rounds_survived = 0

    while True:
        input("Press enter to pull the trigger > ")
        current_chamber = random.randint(1, 6)
        print(f"Chamber: {current_chamber}")

        if current_chamber == bullet_chamber:
            print("💥 BANG! You've been hit.")
            print(f"You survived {rounds_survived} round(s).")
            break
        else:
            print("😌 Click... you're safe. Try again!\n")
            rounds_survived += 1
            time.sleep(0.5)

    # Ask if they want to play again
    replay = input("\nWould you like to play again? (Y/N): ").strip().lower()
    if replay == "Y":
        play_game()
    else:
        print("Thanks for playing! Stay lucky. 🎯")

# Start the game
play_game()