from .Console import console
from Inputs.inputHandler import Input, sleep
from os import system

class Display:
    def __init__(self) -> None:
        self.console = console
        self.clear = lambda: system('cls||clear')
        self.input = Input(self.console)

    def log(self, string: str, style: str | None = None) -> None:
        self.console.print(string, style=style)

    def waitinput(self) -> None:
        wait = True if self.input.get_keyboard_input() != 'enter' else False
        while wait:
                    wait = True if self.input.get_keyboard_input() != 'enter' else False

    def logbars(self, prompt: str = "", xp: bool = False):
        self.clear()
        self.console.print(self.player.pvbar()+"\n", highlight=False)
        self.console.print(self.enemy.pvbar()+"\n", highlight=False)
        self.console.print(prompt)
        if xp:
            length = 20
            fullbarlength = round(self.player.xp / self.player.maxxp * length)
            color = "gold3" if self.player.xp >= 75/100 * self.player.maxxp else "light_goldenrod3" if self.player.xp >= 50/100 * self.player.maxxp else "tan" if self.player.xp >= 25/100 * self.player.maxxp else "misty_rose3"
            self.console.print(f":sparkler:  [underline bold gold1]XP[/underline bold gold1] [{color} on {color}]{fullbarlength * ' '}[/{color} on {color}][grey19 on grey19]{(length - fullbarlength) * ' '}[/grey19 on grey19] [bold gold1]{self.player.xp}/{self.player.maxxp}[/bold gold1]")

    def combatinitdisplay(self, combat):
        self.player = combat.player
        self.enemy = combat.enemy  

    def combatrefresh(self, menu: bool = False, actions: list = None, prompt: str = "") -> int | None:
        if menu:
            assert actions != None, "Vous devez fournit une liste d'action valide!"
            cursor = 0
            key = None
            while key != 'enter':
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
