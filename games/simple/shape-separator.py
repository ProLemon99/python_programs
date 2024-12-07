import time

print("I am a basic 2D shape separator. Pick a shape and I will guess it.")
time.sleep(3)
print("Before you start, we need to go through the rules. My rules are very simple, only type yes or no for all the questions otherwise it will give you an error and I will not guess your shape.") 
time.sleep(4)
print("You must also must not choose an irregular shape or I will not guess it. Types of triangles are not allowed, neither are stars. I will not go past 6 sided shapes.")  
time.sleep(3)
print("Without much further ado, let's begin.")

thanks = "Thank you for playing!"

answer = input("Does your shape have a curved side? ")

if answer.upper() == "YES":
  curved = input("Does your shape have a consistent radius? ")
  if curved.upper() == "YES":
    circle = input("Your shape is a circle. ")
    if circle.upper() == "YES":
            print(thanks)
  if curved.upper() == "NO":
    oval = input("Your shape is an oval. ")
    if oval.upper() == "YES":
            print(thanks)    
else:
  reply = input("Does your shape have more than 4 sides? ")
  if reply.upper() == "YES":
    fivesides = input("Does your shape have more than 5 sides? ")
    if fivesides.upper() == "YES":
      moreside = input("Does your shape have 6 sides? ")
      if moreside.upper() == "YES":
        hexagon = input("Your shape is a hexagon. ")
        if hexagon.upper() == "YES":
          correcta = input("Did I get it correct? ")
          if correcta.upper() == "YES":
            print(thanks)
    elif fivesides.upper() == "NO":
      pentagon = input("Your shape is a pentagon. ")
      if pentagon.upper() == "YES":
        correcta = input("Did I get it correct? ")
        if correcta.upper() == "YES":
          print(thanks)
      
  elif reply.upper() == "NO":
    foursides = input("Does your shape have more than 3 sides? ")
    if foursides.upper() == "YES":
      equal = input("Are all the sides equal? ")
      if equal.upper() == "YES":
        square = ("Your shape is a square. ")
        if square.upper() == "YES":
          correcta = input("Did I get it correct? ")
          if correcta.upper() == "YES":
            print(thanks)
      elif equal.upper() == "NO":
        rectangle = ("Your shape is a rectangle. ")
        if rectangle.upper() == "YES":
          correcta = input("Did I get it correct? ")
          if correcta.upper() == "YES":
            print(thanks)
    elif foursides.upper() == "NO":
      triangle = input("Your shape is a triangle. ")
      if triangle.upper() == "YES":
        print(thanks)