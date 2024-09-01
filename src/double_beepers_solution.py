from stanfordkarel import *


"""
Task:
Move across the first row. 
If beepers are present on any corner, double them. 
After completing the task, Karel should return to its 
starting position and face east.
"""


# Main program
def main():
    # 1. Move across the first row
    while front_is_clear():
        # 2. If beepers are present on a corner, double them
        if beepers_present():
            # double beepers
            double_beepers()
        move()

    # 3. Return to initial position
    go_home()


def double_beepers():
    # move beepers to the row above
    while beepers_present():
        pick_beeper()
        move_up()
        put_beeper()
        move_down()

    # move to the row above
    move_up()

    # move all beepers back to the first row
    while beepers_present():
        pick_beeper()
        move_down()
        put_beeper()
        put_beeper()
        move_up()

    # Return to the first row
    move_down()

def move_up():
    turn_left()
    move()

def move_down():
    turn_around()
    move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def go_home():
    # Return Karel to the southwest corner and face east
    turn_around()
    while front_is_clear():
        move()
    turn_around()


if __name__ == "__main__":
    run_karel_program("double_beepers_start")
