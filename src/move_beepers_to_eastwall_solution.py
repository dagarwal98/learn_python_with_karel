from stanfordkarel import *


def main():
    """
    The task is to pick all beepers and move them to the corner near
    east wall and return home.
    """
    # 1. Move across the first row
    move_all_beepers()

    # 4. Return to initial position
    go_home()

def move_all_beepers():
    while front_is_clear():
        # 2. If a beeper is found, move it to the corner next to the east wall
        if beepers_present():
            # pick up beeper and move to the SE corner
            move_beeper_to_east()
        else:
            move()

def move_beeper_to_east():
    pick_beeper()
    while front_is_clear():
        move()
    put_beeper()
    go_home()

def go_home():
    # Return Karel to the southwest corner and face east
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def turn_around():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program("move_beepers_to_eastwall_start")
