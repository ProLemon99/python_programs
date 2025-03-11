import random

running = True

print("Welcome to the number guessing game!")
options = input("Would you like me to guess your number, or would you like to guess my number?\n1: Guess computer's number\n2: Guess your number\n")

if options == "1":
    number = random.randint(1, 100)
    while running:
        try:
            print(number)
            guess = int(input('Enter a number: '))

            if guess == number:
                print(f'Congratulations, you guessed it! The number was indeed {number}')
                running = False # stop the while loop
            elif guess < number:
                print('No, it is a little higher than that.')
            else:
                print('No, it is a little lower than that.')
        except ValueError:
            print("Not a number! Please enter a valid full number.")
    else:
        print('Thanks for playing! Hope you had fun')
elif options == "2":
    pc_guess = random.randint(1,100)
    print("My first guess is: ", pc_guess)
    correct = input("Is the number lower, higher, or correct? ")

    min = 1
    max = 100
    count = 1

    while correct != "correct":
        if correct == 'higher':
            min = pc_guess + 1
        elif correct == 'lower':
            max = pc_guess - 1
        elif correct != 'higher' or 'lower':
            print("??????")

        pc_guess = random.randint(min, max)
        print(pc_guess)
        correct = input("Is the number lower, higher, or correct? ")
        count += 1

    print("GG! Your number was ", pc_guess, ", and I guessed it in only ", count, " tries!")
else:
    print("Please input a valid option.")