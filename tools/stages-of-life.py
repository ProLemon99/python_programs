try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("You don't exist!")
    elif age == 0 or age == 1:
        category = 'infant'
        dependency = "an"
    elif age > 1 and age <= 4:
        category = "toddler"
        dependency = "a"
    elif age > 4 and age <= 12:
        category = 'child'
        dependency = "a"
    elif age > 12 and age <= 19:
        category = 'teenager'
        dependency = "a"
    elif age > 19 and age <= 39:
        category = 'adult'
        dependency = "an"
    elif age > 39 and age <= 59:
        category = 'middle-aged adult'
        dependency = "a"
    elif age > 59 and age <= 150:
        category = 'senior adult'
        dependency = "a"
    elif age > 150:
        print("You are deceased! R.I.P ❤️")
    else:
        print("Invalid input.")
except ValueError:
    print("Please input a valid full number!")
else:
    if age >= 0 and age <= 150:
        print(f"You are {dependency} {category}.")