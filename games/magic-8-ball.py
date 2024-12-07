import random
import time

name = input('What is your name?\n')
example = input(f'Hello {name}! I am a magical 8 ball! Do you wish to play with me??\n')

if example == "yes":
   print("let's go")
   question = input("Ask me a question: ")
   responses = [
        'it is certain.', 'it is decidedly so.', 'without a doubt.',
        'yes - definitely.', 'you may rely on it.', 'as I see it, yes.',
        'yost likely.', 'outlook good!', 'yes.', 'signs point to yes.',
        'reply hazy, try again.', 'ask again later...',
        'better not tell you now.', 'cannot predict now.',
        "don't count on it.", 'my reply is no.', 'my source say no.',
        'outlook not so good.', 'very doubtful.']
   print(f"🎱 Well dear {name}, {random.choice(responses)} 🎱")

if example == "no":
   print("okay have a good day")

if example != "yes" and example != "no":
   print("?????")