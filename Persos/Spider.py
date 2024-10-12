from .Perso import Character

class Spider(Character):
    def __init__(self, lvl) -> None:
        super().__init__('Araignée', 4*lvl, 3*lvl, 0, lvl)