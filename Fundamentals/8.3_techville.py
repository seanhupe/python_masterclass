def start_engine():
    print("Starting engine")


def move_forward():
    print("Moving forward")


def turn(direction):
    print(f'Turning {direction}')


def follow_roundabout(exit_number):
    print(f"Taking exit number {exit_number} from the roundabout.")


def stop_engine():
    print("Stopping engine.")


# INSTRUCTIONS: -----------------------------------------------------------------
# 1. Start Engine
start_engine()

# 2. Ask user for their desired destination
destination = input("What is your desired destination? ").lower()

# 3. If destination is "library", move forward, turn left, announce arrival
if destination == "library":
    move_forward()
    turn("left")
    print("We have arrived at the library!")

# if destination is "tech park" - move forward, turn right, announce arrival
elif destination == "tech park":
    move_forward()
    turn("right")
    print("We have arrived at the Tech Park")

# if destination involves the roundabout (hospital, mall, airport, university, stadium...
# .. move forward, announce entering the roundabout
elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
    move_forward()
    print("Entering the Roundabout...")

    # If hospital, take the 1st exit, move forward, turn right, announce arrival
    if destination == "hospital":
        follow_roundabout(1)
        print("You are now at the Hospital!")

    # if mall - take the 2nd exit, move forward, turn right, announce arrival
    elif destination == "mall":
        follow_roundabout(2)
        move_forward()
        turn("Right")
        print("You are now at the Mall!")

    # If airport, take the 3rd exit, announce arrival
    elif destination == "airport":
        follow_roundabout(3)
        print("You are now at the Airport!")

    # If 'university' or 'stadium' - take 4th exit, move forward
    elif destination in ["university", "stadium"]:
        follow_roundabout(4)
        move_forward()

        # if university - turn left, announce arrival
        if destination == "university":
            turn("Left")
            print("You have arrived at the University!")

        # if stadium - turn right, announce arrival
        else:    # destination == "stadium":
            turn("Right")
            print("Stadium arrival!!")


else:
    print("That destination is unavailable.")

stop_engine()
