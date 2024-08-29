from stanfordkarel import *


"""
    Task:
    This is a 7x7 world.
    First row has 0 or 1 beeper on each corner.
    If a beeper is present, create a column of 5 beepers on that corner.
    After completing the task, Karel should return to its starting position
    and face east.
"""


def main():
    # 1. Move across the first row
    while front_is_clear():
        # 2. Build column if a beeper is present
        if beepers_present():
            build_column()
        move()

    # build a column on the last corner only if a beeper is present
    if beepers_present():
        build_column()

    # 3. Return home
    go_home()


def turn_around():
    turn_left()
    turn_left()


def go_home():
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def build_column():
    """
    Karel is facing east
    build column
    Face east again
    """
    turn_left()
    for i in range(4):
        move()
        put_beeper()
    turn_around()
    while front_is_clear():
        move()
    turn_left()


if __name__ == "__main__":
    run_karel_program("build_beeper_columns_start")
