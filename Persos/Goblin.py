from .Perso import Character

class Goblin(Character):
    def __init__(self, lvl) -> None:
        super().__init__('Goblin', pv=6*lvl, atk=1*lvl, arm=0, lvl=lvl, dodge=1)