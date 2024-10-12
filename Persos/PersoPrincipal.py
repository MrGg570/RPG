from .Perso import Character

class Player(Character):
    def __init__(self) -> None:
        super().__init__('Joueur', 100, 10, 0, 1)
        self.gold = 0

    def lvlup(self) -> int:
        self.xp = 0
        self.maxxp = self.lvl * 100
        goldamount = 10 + round(1.5 * self.lvl)
        self.gold += goldamount
        return goldamount