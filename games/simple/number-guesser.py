import random

def guess_computers_number():
    number = random.randint(1, 100)
    guess_count = 0
    running = True

    while running:
        try:
            guess = int(input('Enter a number (1 - 100): '))

            if guess < 1 or guess > 100:
                print("Out of range! Please enter a number between 1 and 100.")
                continue

            guess_count += 1

            if guess == number:
                print(f'Congratulations, you guessed it in {guess_count} attempts! The number was {number}.')
                running = False
            elif guess < number:
                print('No, it is a little higher than that.')
            else:
                print('No, it is a little lower than that.')

        except ValueError:
            print("Not a number! Please enter a valid full number.")

    print('Thanks for playing! Hope you had fun.')
    return replay_or_exit()

def computer_guesses_your_number():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    min_num, max_num = 1, 100
    count = 0

    while True:
        if min_num > max_num:
            print("You're lying! There's no number that fits your previous hints.")
            break
        
        pc_guess = random.randint(min_num, max_num)
        print("My guess is: ", pc_guess)
        correct = input("Is the number lower, higher, or correct? ").lower()
        count += 1

        if correct == "correct":
            print(f"GG! Your number was {pc_guess}, and I guessed it in {count} tries!")
            break
        elif correct == 'higher':
            min_num = pc_guess + 1
        elif correct == 'lower':
            max_num = pc_guess - 1
        else:
            print("Invalid input. Please enter 'lower', 'higher', or 'correct'.")
    
    return replay_or_exit()

def replay_or_exit():
    while True:
        choice = input("Press R to replay or E to exit: ").lower()
        if choice == 'r':
            main()
        elif choice == 'e':
            print("Thanks for playing! Goodbye.")
            exit()
        else:
            print("Invalid input. Please enter 'R' or 'E'.")

def main():
    print("Welcome to the number guessing game!")
    options = input("Would you like me to guess your number, or would you like to guess my number?\n1: Guess computer's number\n2: Guess your number\n")

    if options == "1":
        guess_computers_number()
    elif options == "2":
        computer_guesses_your_number()
    else:
        print("Please input a valid option.")
        main() 

if __name__ == "__main__":
    main()