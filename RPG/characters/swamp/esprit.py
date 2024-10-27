from ..character import Character

class Esprit(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(name='Esprit', pv=40, atk=round((45/enemies)*f), arm=0, lvl=lvl, number=enemies, f=f)

        self.attacks.update({'Possession': (50, 60),'Cri Terrifiant': (30, 90)})