def move_forward():
    print("moving forward")


def turn(direction):
    print(f"turning {direction}")


def start_engine():
    print("starting engine")


def stop_engine():
    print("stopping engine")


start_engine()
move_forward()

destination = input("Where do you want to go? ")

if destination == "school":
    turn("right")
    print("We arrived at school!")
elif destination == "grocery store" or destination == "dentist":
    turn("left")
    move_forward()
    if destination == "grocery store":
        turn("right")
        print("We arrived at grocery store!")
    else:
        turn("left")
        print("You have arrived at the dentist!")
elif destination == "restaurant":
    move_forward()
    print("We arrived at restaurant!")
else:
    print("You aren't going anywhere!")




