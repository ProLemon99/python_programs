import random

HANGMAN = [
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |
    |
    |
    |
    |
    |
    ----------
    """,
    """
    ------
    |    |
    |    O
    |   -+-
    | 
    |   
    |   
    |   
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-
    |   
    |   
    |   
    |   
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |   
    |   
    |   
    |   
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |   
    |   
    |   
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |    |
    |   | 
    |   | 
    |   
    ----------
    """,
    """
    ------
    |    |
    |    O
    |  /-+-/
    |    |
    |    |
    |   | |
    |   | |
    |  
    ----------
    """
]

MAX_WRONG = len(HANGMAN) - 1

WORDS = {
    "easy": ["PLANET", "BRIDGE", "FROSTY", "CANDLE", "MARKET", "JUMPED", "SILENT", "HUNTER"],
    "medium": ["APPROACH", "ELEPHANT", "CAMPFIRE", "FANTASY", "TELEGRAM", "VIBRANCE", "RAINBOW"],
    "hard": ["IMAGINATION", "EXPERIMENTAL", "CONSEQUENCE", "PARTICIPATION", "CELEBRATION", "TECHNOLOGY"]
}

def choose_difficulty():
    while True:
        print("\nSelect Difficulty:\n1. Easy\n2. Medium\n3. Hard\n")
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def play_hangman():
    difficulty = choose_difficulty()
    word = random.choice(WORDS[difficulty])  # Select a word from the chosen difficulty
    so_far = "-" * len(word)  # Masked word
    wrong = 0
    used = []  # List of guessed letters

    print(f"\nYou chose {difficulty.capitalize()} difficulty. Good luck!")

    while wrong < MAX_WRONG and so_far != word:
        print(HANGMAN[wrong])
        print("\nUsed letters:", ", ".join(used) if used else "None")
        print("\nWord progress:\t", so_far)

        guess = input("\nEnter your guess:\t").upper()

        while not guess.isalpha() or len(guess) != 1 or guess in used:
            if guess in used:
                print("You already guessed that letter!")
            else:
                print("Invalid input! Please enter a single letter.")
            guess = input("Enter your guess:\t").upper()

        used.append(guess)

        if guess in word:
            print(f"\nGreat! The letter '{guess}' is in the word.")
            so_far = "".join(guess if word[i] == guess else so_far[i] for i in range(len(word)))
        else:
            print(f"\nNope! The letter '{guess}' is not in the word.")
            wrong += 1

    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou have been hanged! The word was:", word)
    else:
        print("\nCongratulations! You guessed the word:", word)

    replay_or_exit()

def replay_or_exit():
    while True:
        choice = input("\nWould you like to play again? (R to replay, E to exit): ").lower()
        if choice == 'r':
            play_hangman()  # Restart game
        elif choice == 'e':
            print("Thanks for playing! Goodbye.")
            exit()
        else:
            print("Invalid input. Please enter 'R' or 'E'.")

if __name__ == "__main__":
    play_hangman()