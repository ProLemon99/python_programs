import random

number = random.randint(1, 100)
running = True

print("Welcome to the number guessing game!")
print("I am guessing a number between 1 to 100, guess which number it is to win!")

while running:
    try:
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