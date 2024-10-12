from Inputs.inputHandler import Input, sleep
from os import system

class Display:
    def __init__(self, console) -> None:
        self.console = console
        self.clear = lambda: system('cls||clear')
        self.input = Input(self.console, self.rfrsh)

    def initdisplay(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def rfrsh(self, prompt: str = "") -> None:
        self.clear()
        self.console.print(self.player.pvbar()+"\n")
        self.console.print(self.enemy.pvbar()+"\n")
        self.console.print(prompt)

    def menu(self, options:list) -> int:
        return self.input.menu(options)
    
    def waitinput(self) -> None:
        wait = True if self.input.get_keyboard_input() != 'enter' else False
        while wait:
                    wait = True if self.input.get_keyboard_input() != 'enter' else False


    