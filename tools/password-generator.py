import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Hello, this is a random password generator that will generate a secure password made of a combination of letters, numbers, and symbols.")

while True:
    try:
        length = int(input("Enter the length of the password (max 30): "))
        if length <= 0:
            print("Please enter a positive number.")
            continue
        elif length > 30:
            print("Don't you think the password would be... too secure?")
            continue
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    while True:
        password = generate_password(length)
        print("Your password is:", password)

        reroll = input("Do you want to generate another password? (Y/N): ").strip().lower()
        if reroll != 'y':
            print("Goodbye! Stay secure.")
            exit()