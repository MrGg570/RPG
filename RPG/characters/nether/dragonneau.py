from ..character import Character

class Dragonneau(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(nom='Dragonneau', pv=80, atk=round((70/enemies)*f), arm=0, lvl=lvl, number=enemies, f=f)
        self.attacks.update( { 'Souffle de Feu': (70, 80),
            'Coup de Griffe': (40, 90)})