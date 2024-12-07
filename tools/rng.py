import random

def get_integer_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid number!")
        return None

# Get the minimum number
min_number = None
while min_number is None:
    min_number = get_integer_input("Min number? ")

# Get the maximum number
max_number = None
while max_number is None:
    max_number = get_integer_input("Max number? ")

# Ensure min is less than max
if min_number >= max_number:
    print("Min number must be less than Max number!")
else:
    while True:
        # Generate a random number
        rng = random.randint(min_number, max_number)
        print(f"Generated number: {rng}")
        
        # Regenerate option
        regenerate = input("Regenerate? Y/N: ").strip().upper()
        if regenerate == "Y":
            continue
        elif regenerate == "N":
            print("Have a good day!")
            break
        else:
            print("I don't understand...")
            break