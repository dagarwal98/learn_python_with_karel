from stanfordkarel import *

"""
    Task:
    This is a 6x5 world.
    Each row has beepers in some corners.
    Fill the rows with missing beepers.
    There are walls between each row except in the first column.
    After completing the task, Karel should return to its starting position
    and face east.
"""

def main():
    while left_is_clear():
        # 1. Move across the row and place beeper on empty corners.
        fill_row()

        # 2. Move to the next row above. Repeat step 1.
        move_to_next_row()

    # fill the last row
    fill_row()

    # 4. Return home after completing all rows.
    go_home()


def go_home():
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def fill_row():
    while front_is_clear():
        check_and_place_beeper()
        move()

    # check and place beeper on the last corner
    check_and_place_beeper()

    # return to first corner
    go_to_other_corner()


def check_and_place_beeper():
    if no_beepers_present():
        put_beeper()

def move_to_next_row():
    turn_left()
    move()
    turn_right()

def go_to_other_corner():
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program("fill_beepers_start")