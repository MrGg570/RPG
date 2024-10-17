from .Console import console
from Inputs.inputHandler import Input, sleep
from os import system

class Display:
    """
    Classe permettant de gérer l'affichage à l'écran
    """
    def __init__(self) -> None:
        """
        Instancie un objet Display avec comme attributs la console, une fonction permettant de clear la console et un objet Input
        """
        self.console = console
        self.clear = lambda: system('cls||clear')
        self.input = Input(self.console)

    def log(self, string: str, style: str | None = None, justify: str | None = None) -> None:
        """
        Permet d'afficher du texte à l'écran
        """
        self.console.print(string, style=style, highlight=False, justify=justify)

    def waitinput(self) -> None:
        """
        Permet d'attendre jusqu'à-ce qu'une touche du clavier soit appuyée
        """
        wait = True if self.input.get_keyboard_input() != 'enter' else False
        while wait:
                    wait = True if self.input.get_keyboard_input() != 'enter' else False

    def logbars(self, prompt: str = "", xp: bool = False):
        """
        Permet d'afficher els barres de vie des personnages lors d'un combat
        """
        self.clear()
        self.console.print(self.player.pvbar()+"\n", highlight=False)
        self.console.print(self.enemy.pvbar()+"\n", highlight=False)
        self.console.print(prompt)
        if xp:
            length = 20
            fullbarlength = round(self.player.xp / self.player.maxxp * length)
            color = "gold3" if self.player.xp >= 75/100 * self.player.maxxp else "light_goldenrod3" if self.player.xp >= 50/100 * self.player.maxxp else "tan" if self.player.xp >= 25/100 * self.player.maxxp else "misty_rose3"
            self.console.print(f":sparkler:  [underline bold gold1]XP[/underline bold gold1] [{color} on {color}]{fullbarlength * ' '}[/{color} on {color}][grey19 on grey19]{(length - fullbarlength) * ' '}[/grey19 on grey19] [bold gold1]{self.player.xp}/{self.player.maxxp}[/bold gold1]")

    def buildtitle(self, title: str) -> str:
        horizontalbar = "\u2500"
        maintitle = "\u250c"
        for i in range(len(title)+4):
            maintitle += horizontalbar
        maintitle += "\u2510\n"
        maintitle += "\u2502  "
        maintitle += title
        maintitle += "  \u2502\n"
        maintitle += "\u2514"
        for i in range(len(title)+4):
            maintitle += horizontalbar
        maintitle += "\u2518\n"
        return maintitle

    def mainMenu(self): 
        actions = ["Démarer  ", "Options  ", "Quitter  "]
        cursor = 0
        key = None
        while key != 'enter':
            self.clear()
            self.log(self.buildtitle("RPG: A ROLE PLAYING GAME"), justify='center', style='bold white')
            cursor = cursor%len(actions)
            for i, e in enumerate(actions):
                if cursor == i:
                    self.console.print('> ' + e, justify='center')
                else:
                    self.console.print('  ' + e, justify='center')

            key = self.input.get_keyboard_input()
            if key == 'haut':
                cursor -= 1
                if cursor<0:
                    cursor = len(actions) - 1
            elif key == 'bas':
                cursor += 1
        return cursor%len(actions)
    
    def menu(self, availableactions: list, menuname: str) -> str: 
        actions = availableactions
        cursor = 0
        key = None
        while key != 'enter':
            self.clear()
            self.log(self.buildtitle(menuname), justify='center', style='bold white')
            cursor = cursor%len(actions)
            for i, e in enumerate(actions):
                if cursor == i:
                    self.console.print('> ' + e + (10-len(e))*"\u2508", justify='center')
                else:
                    self.console.print('  ' + e + (10-len(e))*"\u2508", justify='center')

            key = self.input.get_keyboard_input()
            if key == 'haut':
                cursor -= 1
                if cursor<0:
                    cursor = len(actions) - 1
            elif key == 'bas':
                cursor += 1
        return actions[cursor%len(actions)]

    def combatinitdisplay(self, combat):
        self.player = combat.player
        self.enemy = combat.enemy  

    def combatrefresh(self, menu: bool = False, actions: list = None, prompt: str = "") -> int | None:
        if menu:
            assert actions != None, "Vous devez fournit une liste d'action valide!"
            cursor = 0
            key = None
            while key != 'enter':
                if prompt != "":
                    self.logbars(f"{prompt}\nChoisissez une action:")
                else:
                    self.logbars("Choisissez une action:")
                cursor = cursor%len(actions)
                for i, e in enumerate(actions):
                    if cursor == i:
                        self.console.print('> ' + e)
                    else:
                        self.console.print('  ' + e)

                key = self.input.get_keyboard_input()
                if key == 'haut':
                    cursor -= 1
                    if cursor<0:
                        cursor = len(actions) - cursor
                elif key == 'bas':
                    cursor += 1
        else:
            self.logbars(prompt)
        return cursor%len(actions) if menu else None
