from .character import Character

class Seigneur_Stellaire(Character):
    def __init__(self, niveau: int = 1, ennemis: int = 1, facteur: int = 1) -> None:
        super().__init__(nom='Seigneur Stellaire', pv=300, atk=200, arm=0, lvl=niveau, number=ennemis, f=facteur)

        self.attacks.update({'Lames d''étoiles''': (50, 100, 'Physique'),'Frappe stellaire':(60,70,'Physique'),'Destruction massive': (100, 20, 'Physique')})