from stanfordkarel import *

"""
    Task:
    First row has beepers on some corners.
    Remove all beepers from the first row and place them in the second row
    in corresponding positions.
    After clearing the first row, Karel should return to its starting position
    and face east.
"""

def main():
    # 1. Move across the first row.
    while front_is_clear():
        # 2. If beepers are found, move them to the row above.
        while beepers_present():
            pick_beeper()
            # move beeper to the row above
            move_up_and_put_beeper()
        move()

    while beepers_present():
        pick_beeper()
        # move beeper to the row above
        move_up_and_put_beeper()

    # 3. Return home.
    go_home()


def go_home():
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def move_up_and_put_beeper():
    turn_left()
    move()
    put_beeper()
    turn_around()
    move()
    turn_left()


# Turn around
def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program("clear_beepers_start")