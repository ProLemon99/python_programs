import time
started = False
stopped = True
command = ""
while True:
    command = input("- ").upper()
    if command == "START":
        if started:
            print("CAR IS ALREADY STARTED")
        else: 
            started = True
            print("CAR STARTED...")
    elif command == "STOP":
        if stopped:
            print("CAR IS ALREADY STOPPED!")
        else:
            stopped = True
            print("CAR STOPPED.")

    elif command == "HELP":
        print
        ("""
START - START THE CAR
STOP - STOP THE CAR
QUIT - QUIT THE GAME
        """)
    elif command == "QUIT":
        time.sleep(0.5)
        print("EXITING THE GAME...")
        time.sleep(2.5)
        break
    else:
        print("INVALID")