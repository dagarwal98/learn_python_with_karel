from stanfordkarel import *


def main():
    """
    Task: Go to the beeper. Pickup beeper. Go to the target
    location and put a beeper. Return home.
    """

    # 1. Go to beeper
    move()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    move()
    turn_left()
    move()
    move()

    # 2. Pick-up beeper
    pick_beeper()

    # 3. Go to target
    turn_right()
    move()
    turn_right()
    move()
    move()
    move()
    move()

    # 4. Put beeper
    put_beeper()

    # 5. Return home
    turn_around()
    move()
    move()
    turn_left()
    move()
    move()
    move()
    move()
    move()
    turn_right()
    move()
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
    run_karel_program("move_beepers_to_target2_start")
