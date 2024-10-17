from keyboard import is_pressed
from time import sleep

class Input:
    """
    Classe qui gère les appuis de touche du clavier
    """
    def __init__(self, console) -> None:
        self.console = console

    def get_keyboard_input(self) -> str:
        while is_pressed('haut') or is_pressed('bas') or is_pressed('enter'):
            sleep(0.05)
        input = False
        while not input:
            if is_pressed('haut'):
                input = 'haut'
            elif is_pressed('bas'):
                input = 'bas'
            elif is_pressed('enter'):
                input = 'enter'
        return input
