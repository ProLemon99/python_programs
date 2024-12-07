try:
    weight = float(input("Weight: "))
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