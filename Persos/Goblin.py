from .Perso import Character

class Goblin(Character):
    def __init__(self, lvl) -> None:
        super().__init__('Goblin', 5*lvl, 1*lvl, 0, lvl)