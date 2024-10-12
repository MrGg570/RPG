from random import randint

class Character:
    """
    Classe de base pour définir des personnages
    """
    def __init__(self, name:str, pv:int, atk:int, arm: int=0, lvl: int = 0, dodge: int = 0) -> None:
        self.name = name
        self.maxpv = pv
        self.pv = pv
        self.atk = atk
        self.arm = arm

        self.dodge = dodge

        self.lvl = lvl
        self.xp = 0
        self.maxxp = self.lvl * 100

    def attaquer(self, other: object) -> bool:
        if randint(0, 100) > other.dodge:
            other.pv -= round(self.atk * 0.5 * self.lvl)
            sucess = True
            if other.pv < 0:
                other.pv = 0
        else:
            sucess = False
        return  sucess
    
    def pvbar(self) -> str:
        style = "bold green" if self.name == 'Joueur' else "bold red"
        pvcolor = "bright_green" if self.pv > 80/100*self.maxpv else "orange3" if self.pv > 20/100*self.maxpv else "bright_red"
        length = 20
        fullbarlength = round(self.pv / self.maxpv * length)
        bar = f"[{style}]{self.name}[/{style}] [gold1](lvl. {self.lvl})[/gold1] [green on green]{fullbarlength * ' '}[/green on green][grey19 on grey19]{(length - fullbarlength) * ' '}[/grey19 on grey19] [bold {pvcolor}]{self.pv}[/bold {pvcolor}]/[bold white]{self.maxpv}[/bold white]"
        return bar
    
    def isalive(self):
        return self.pv > 0