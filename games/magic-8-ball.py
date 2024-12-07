import random

name = input('What is your name?\n')
example = input(f'Hello {name}! This is your magical 8 ball! Do you wish to play with me??\n')

if example == "yes":
   print("let's go")
   question = input("Ask me a question: ")
   choices = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
   print(f"Well dear {name}, {random.choice(choices)}")

if example == "no":
   print("okay have a good day")

if example != "yes" and example != "no":
   print("?????")