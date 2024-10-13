from .Perso import Character

class Player(Character):
    def __init__(self) -> None:
        super().__init__('Joueur', pv=100, atk=10, arm=0, lvl=1, dodge=5)
        self.gold = 0

    def lvlup(self) -> int:
        self.maxpv += 5+2*self.lvl
        self.xp = 0
        self.maxxp = self.lvl * 100
        goldamount = 10 + round(1.5 * self.lvl)
        self.gold += goldamount
        return goldamount