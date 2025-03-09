import random

HANGMAN = (
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
""")

MAX_WRONG = len(HANGMAN) - 1

WORDS = ("APOSTROPHE", "MUSHROOM", "TELEVISION",
         "GEOMETRY", "RELATABLE", "BRAINROT",
         "APPLICATION", "VISUALISATION", "PRACTICE")

word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print (HANGMAN[wrong])
    print ("\nYou've used the following letters:\n", used)
    print ("\nSo far, you have guessed:\t", so_far)

    guess = input("Enter your guess:\t")
    guess = guess.upper()

    while guess in used:
        print ("You already guessed the letter:\t", guess)
        guess = input("Guess again:\t")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print ("The letter, ", guess, "is in the word")

        new = ""

        for i in range(len(word)):
            if guess == word [i]:
                new += guess
            else:
                new += so_far [i]
        so_far = new

    else:
        print ("\nSorry,", guess, "isn't in word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print ("You have been hanged :(")

else:
    print("\nCongratulations! You guessed it!")

print("\nThe word was", word)

input ("\n\nPress Enter key to exit")