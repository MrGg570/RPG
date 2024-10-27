from .character import Character

class Seigneur_Stellaire(Character):
    def __init__(self, lvl: int = 1, enemies: int = 1, f: int = 1) -> None:
        super().__init__(name='Seigneur Stellaire', pv=300, atk=200, arm=0, lvl=lvl, number=enemies, f=f)

        self.attacks.update({'Lames d''étoiles''': (50, 100, 'Physique'),'Frappe stellaire':(60,70,'Physique'),'Destruction massive': (100, 20, 'Physique')})