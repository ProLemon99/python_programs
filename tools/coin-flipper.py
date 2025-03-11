import random

def coin_flip_counter(flips=None):
    if flips is None:  # Ask for input only on the first run
        print("Welcome to the Coin Flip Counter Program")
        while True:
            try:
                flips = int(input("How many times would you like to flip the coin? (Max: 1000): "))
                if 1 <= flips <= 1000:
                    break
                else:
                    print("Please enter a number between 1 and 1000.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    heads, tails = 0, 0

    for _ in range(flips):
        coin = random.randint(1, 2)
        if coin == 1:
            heads += 1
        else:
            tails += 1

    print(f"\nTotal amount of heads vs tails in {flips} flips:\n\t{heads} heads\n\t{tails} tails.")

    return replay_or_exit(flips)

def replay_or_exit(flips):
    while True:
        choice = input("\nPress R to reroll or E to exit: ").lower()
        if choice == 'r':
            coin_flip_counter(flips)  # Pass the same number of flips
        elif choice == 'e':
            print("Thanks for playing! Goodbye.")
            exit()
        else:
            print("Invalid input. Please enter 'R' or 'E'.")

if __name__ == "__main__":
    coin_flip_counter()