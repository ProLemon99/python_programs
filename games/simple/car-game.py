import time
import threading

# Initialize variables
started = False
speed = 0
distance = 0
unit = ""

# Ask user for preferred speed unit
while True:
    unit = input("Do you prefer km/h or mph? (K/M): ").strip().upper()
    if unit == "K":
        unit = "km/h"
        break
    elif unit == "M":
        unit = "mph"
        break
    else:
        print("Invalid choice. Please enter 'K' for km/h or 'M' for mph.")

# Function to convert speed to metres per second
def speed_to_mps(speed, unit):
    if unit == "km/h":
        return round(speed * 1000 / 3600)  # Convert km/h to m/s
    else:
        return round(speed * 1609.34 / 3600)  # Convert mph to m/s

# Function to update distance in a separate thread
def update_distance():
    global distance, speed, started
    while started:
        time.sleep(1)
        if speed > 0:
            distance += speed_to_mps(speed, unit)
            print(f"Distance traveled: {distance} meters")

print("\nCar Simulator Started! Type HELP for commands.\n")

# Main game loop
while True:
    command = input("- ").strip().upper()

    if command == "START":
        if started:
            print("Car is already started!")
        else:
            started = True
            speed = 0
            distance = 0
            print("Car started. Enter a speed to begin driving.")
            threading.Thread(target=update_distance, daemon=True).start()  # Start distance tracking in the background

    elif command == "STOP":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            speed = 0
            print(f"Car stopped. Total distance traveled: {distance} meters.")

    elif command == "HELP":
        print("""
START - Start the car
STOP - Stop the car
SPEED - Set car speed
A - Accelerate
D - Decelerate
QUIT - Exit the simulation
        """)

    elif command == "SPEED":
        if not started:
            print("You need to start the car first!")
        else:
            try:
                speed = int(input(f"Enter speed in {unit}: "))
                print(f"Speed set to {speed} {unit}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif command == "A":
        if not started:
            print("The car is stopped! Start it first.")
        else:
            try:
                new_speed = int(input(f"Enter new speed in {unit}: "))
                speed = new_speed
                print(f"Accelerated to {speed} {unit}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif command == "D":
        if not started:
            print("The car is stopped! Start it first.")
        else:
            try:
                new_speed = int(input(f"Enter new speed in {unit}: "))
                speed = max(0, new_speed)  # Speed cannot be negative
                print(f"Decelerated to {speed} {unit}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif command == "QUIT":
        time.sleep(0.5)
        print("Exiting simulation...")
        time.sleep(1)
        break

    else:
        print("Invalid command. Type HELP for available commands.")

print("Goodbye!")