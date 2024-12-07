print("Welcome to the basic unit-of-measurement converter!")
print("This converter can currently only convert units of measurement for weight and temperature, but don't worry, more are coming soon!")
quantity = input("What type of quantity would you like to convert?\na) Weight\nb) Temperature\n").lower()  # Convert input to lowercase

if quantity == "a":
    try:
        weight = float(input("Enter weight: "))
        unit = input("Kg or Lbs?\nK: Kg\nL: Lbs\n")

        if unit.upper() == "L":
            convert = weight * 0.453592
            print("Your weight in Kg is: " + str(round(convert, 2)))
        elif unit.upper() == "K":
            converted = weight / 0.453592
            print("Your weight in Lbs is: " + str(round(converted, 2)))
        else:
            print("Enter a valid unit (K or L).")
    except ValueError:
        print("Enter a valid float.")
elif quantity == "b":
    try:
        temperature = float(input("Enter temperature: "))
        unit = input("Celsius or Fahrenheit?\nC: Celsius\nF: Fahrenheit\n")

        if unit.upper() == "C":
            convert = temperature * (9/5) + 32
            print("The temperature in Fahrenheit is: " + str(round(convert, 2)))
        elif unit.upper() == "F":
            converted = (temperature - 32) * 5/9
            print("The temperature in Celsius is: " + str(round(converted, 2)))
        else:
            print("Enter a valid unit (C or F).")
    except ValueError:
        print("Enter a valid float.")
else:
    print("What?")