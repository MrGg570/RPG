class Character:
    """
    Classe de base pour définir des personnages
    """
    def __init__(self, name:str, pv:int, atk:int, arm: int=0, xp: int = 0) -> None:
        self.name = name
        self.maxpv = pv
        self.pv = pv
        self.atk = atk
        self.arm = arm

        self.lvl = 1
        self.xp = xp
        self.maxxp = self.lvl * 100

    def attaquer(self, other: object) -> bool:
        # probas
        # if probas:
        other.pv -= self.atk
        return  True # if probas else False
    
    def pvbar(self) -> str:
        style = "bold green" if self.name == 'Joueur' else "bold red"
        length = 20
        fullbarlength = round(self.pv / self.maxpv * length)
        bar = f"[{style}]{self.name}[/{style}] [yellow](lvl. {self.lvl})[/yellow] [green on green]{fullbarlength * ' '}[/green on green][red on red]{(length - fullbarlength) * ' '}[/red on red] {self.pv}/{self.maxpv}"
        return bar
    
    def isalive(self):
        return self.pv > 0