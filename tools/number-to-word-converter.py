import inflect

p = inflect.engine()

def number_to_words(number):
    return p.number_to_words(number)

print("This is a very basic converter that converts numbers into words.")

while True:
    try:
        num = int(input("Enter a number: "))
        print(number_to_words(num))

        reroll = input("Again? (Y/N): ").strip().lower()
        if reroll != 'y':
            print("Goodbye!")
            exit()

    except ValueError:
        print("Please enter a valid number.")
        continue