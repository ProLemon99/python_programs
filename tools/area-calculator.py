import math

def calculate_area():
    print("Welcome to the Area Calculator!")
    print("Please choose a shape to calculate its area:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Exit")

    while True:
        try:
            choice = int(input("Enter the number of your choice (1-5): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            # Square
            side = float(input("Enter the side length of the square: "))
            area = side ** 2
            print(f"The area of the square is {area:.2f} square units.")
        
        elif choice == 2:
            # Rectangle
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            print(f"The area of the rectangle is {area:.2f} square units.")
        
        elif choice == 3:
            # Triangle
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = 0.5 * base * height
            print(f"The area of the triangle is {area:.2f} square units.")
        
        elif choice == 4:
            # Circle
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * radius ** 2
            print(f"The area of the circle is {area:.2f} square units.")
        
        elif choice == 5:
            print("Thank you for using the Area Calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")
        
        print("\nWould you like to calculate another area?")
        print("1. Yes")
        print("2. No")
        again = input("Enter your choice (1 or 2): ")
        if again != '1':
            print("Thank you for using the Area Calculator. Goodbye!")
            break

# Run the program
calculate_area()