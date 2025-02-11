import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Hello, this is a random password generator that will generate a secure password made of a combination of letters, numbers and symbols.")
length = int(input("Enter the length of the password: "))
print("Your password is:", generate_password(length))