from Inputs.inputHandler import Input
from os import system

class Display:
    def __init__(self, console) -> None:
        self.console = console
        self.clear = lambda: system('cls||clear')
        self.input = Input(self.console, self.rfrsh)

    def initdisplay(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def rfrsh(self) -> None:
        self.clear()
        self.console.print(self.player.pvbar()+"\n")
        self.console.print(self.enemy.pvbar()+"\n")

    def menu(self, options:list) -> str:
        return self.input.menu(options)


    