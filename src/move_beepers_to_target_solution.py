from stanfordkarel import *


def main():
    """
    Task: Go to the pile of beepers. Pickup three beepers. Then go to the target
    location as shown in the end state (move_beepers_to_target_end). Put three
    beepers and then return home.
    """
    # 1. Go to beepers
    move()
    # 2. Pick 3 beepers
    pick_beeper()
    pick_beeper()
    pick_beeper()
    # 3. Go to target
    move()
    turn_left()
    move()
    # turn right
    turn_right()
    move()
    move()
    # 4. Put beepers
    put_beeper()
    put_beeper()
    put_beeper()
    # 5. Return home
    turn_around()
    move()
    move()
    turn_left()
    move()
    # turn right
    turn_right()
    move()
    move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program("move_beepers_to_target_start")
