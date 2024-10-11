from keyboard import is_pressed
from time import sleep

class Input:
    def __init__(self, console, rfrsh) -> None:
        self.console = console
        self.rfrsh = rfrsh

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

    def menu(self, options: list) -> int:
        cursor = 0
        input = None
        while input != 'enter':
            self.rfrsh()
            cursor = cursor%len(options)
            for i, e in enumerate(options):
                if cursor == i:
                    self.console.print('> ' + e)
                else:
                    self.console.print('  ' + e)

            input = self.get_keyboard_input()
            if input == 'haut':
                cursor -= 1
                if cursor<0:
                    cursor = len(options)+1 - cursor
            elif input == 'bas':
                cursor += 1
        return cursor%len(options)
            