from keyboard import is_pressed
from time import sleep

def get_keyboard_input() -> str:
    while is_pressed('haut') or is_pressed('bas') or is_pressed('enter'):
        sleep(1)
    input = False
    while not input:
        if is_pressed('haut'):
            input = 'haut'
        elif is_pressed('bas'):
            input = 'bas'
        elif is_pressed('enter'):
            input = 'enter'
    return input