import math
import cmath

def display_menu():
    print("\nAdvanced Calculator")
    print("1. Basic Arithmetic")
    print("2. Trigonometric Functions")
    print("3. Exponential and Logarithmic Functions")
    print("4. Factorial")
    print("5. Complex Number Operations")
    print("6. Unit Conversion")
    print("7. Exit")
    choice = input("Select an option (1-7): ")
    return choice

def basic_arithmetic():
    print("\nBasic Arithmetic Operations")
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

def trigonometric_functions():
    print("\nTrigonometric Functions")
    try:
        angle = float(input("Enter the angle in degrees: "))
        radian = math.radians(angle)
        print(f"sin({angle}) = {math.sin(radian)}")
        print(f"cos({angle}) = {math.cos(radian)}")
        print(f"tan({angle}) = {math.tan(radian)}")
    except ValueError:
        print("Invalid input! Please enter a number.")

def exponential_logarithmic():
    print("\nExponential and Logarithmic Functions")
    try:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        print(f"{base}^{exponent} = {math.pow(base, exponent)}")
        if base > 0:
            print(f"log({base}) = {math.log(base)}")
        else:
            print("Logarithm undefined for non-positive base.")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def factorial():
    print("\nFactorial")
    try:
        num = int(input("Enter a non-negative integer: "))
        if num >= 0:
            print(f"{num}! = {math.factorial(num)}")
        else:
            print("Error: Factorial is not defined for negative numbers.")
    except ValueError:
        print("Invalid input! Please enter a non-negative integer.")

def complex_number_operations():
    print("\nComplex Number Operations")
    try:
        real1 = float(input("Enter the real part of the first number: "))
        imag1 = float(input("Enter the imaginary part of the first number: "))
        real2 = float(input("Enter the real part of the second number: "))
        imag2 = float(input("Enter the imaginary part of the second number: "))
        c1 = complex(real1, imag1)
        c2 = complex(real2, imag2)
        print(f"{c1} + {c2} = {c1 + c2}")
        print(f"{c1} - {c2} = {c1 - c2}")
        print(f"{c1} * {c2} = {c1 * c2}")
        print(f"{c1} / {c2} = {c1 / c2}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def unit_conversion():
    print("\nUnit Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    choice = input("Select an option (1-4): ")
    try:
        value = float(input("Enter the value to convert: "))
        if choice == '1':
            print(f"{value}°C = {value * 9/5 + 32}°F")
        elif choice == '2':
            print(f"{value}°F = {(value - 32) * 5/9}°C")
        elif choice == '3':
            print(f"{value} km = {value * 0.621371} miles")
        elif choice == '4':
            print(f"{value} miles = {value / 0.621371} km")
        else:
            print("Invalid option!")
    except ValueError:
        print("Invalid input! Please enter a numerical value.")

def main():
    while True:
        choice = display_menu()
        if choice == '1':
            basic_arithmetic()
        elif choice == '2':
            trigonometric_functions()
        elif choice == '3':
            exponential_logarithmic()
        elif choice == '4':
            factorial()
        elif choice == '5':
            complex_number_operations()
        elif choice == '6':
            unit_conversion()
        elif choice == '7':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()