from stanfordkarel import *


def main():
    """
    The task is to place a beeper in the southeast corner of the world
    and return home. Karel should be facing east at the end.
    """
    # 1. move to the other corner
    move_to_other_corner()

    # 2. put down a beeper
    put_beeper()

    # 3. turn around to face west
    turn_around()

    # 4. move to the other corner
    move_to_other_corner()

    # 5. turn around to face east
    turn_around()

def move_to_other_corner():
    # move()
    # move()
    # move()
    # move()
    # move()

    # for i in range(5):
    #     move()

    while front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("6x5")
