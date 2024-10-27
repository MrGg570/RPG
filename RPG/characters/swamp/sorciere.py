from ..character import Character

class Sorciere(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(name='Sorcière', pv=50, atk=round((35/enemies)*f), arm=0, lvl=lvl, number=enemies, f=f)

        self.attacks.update({'Boule de magie': (45, 85),'Malédiction': (30, 70), 'coup de baguette': (20, 65) })