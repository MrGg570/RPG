from .Perso import Character

class Player(Character):
    """
    Classe utilisée pour instancier le joueur
    """
    def __init__(self) -> None:*
        """
        Le joueur est instancié avec _ PV, _ ATK, 0 ARM, 5 DODGE et au niveau 1. 
        Il possède un attribut supplémentaire aux ennemies: GOLD, représentant la monnaie du joueur
        """
        super().__init__('Joueur', pv=100, atk=10, arm=0, lvl=1, dodge=5)
        self.gold = 0

    def lvlup(self) -> int:
        """
        Appelé quand le personnage monte de niveau
        """
        self.maxpv += 5+2*self.lvl
        self.xp = 0
        self.maxxp = self.lvl * 100
        goldamount = 10 + round(1.5 * self.lvl)
        self.gold += goldamount
        return goldamount
