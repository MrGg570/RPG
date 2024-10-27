from ..character import Character

class Phenix(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(nom='Phénix', pv=120, atk=round((70/enemies)*f), arm=0, lvl=lvl, number=enemies, f=f)

        self.attacks.update({'Pluie de Feu': (80, 80),'Explosion solaire':(100,50)})