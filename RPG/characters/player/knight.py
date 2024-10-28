from ..character import Character

class Knight(Character):
    def __init__(self, name: str) -> None:
        self.basepv = 100
        super().__init__(name=name, pv=self.basepv, atk=75, arm=0, lvl=1)
        self.attacks.update({'Charge':(100, 95),'Sword attack': (150, 80)})
        self.isplayer = True

        self.xp = 0
        self.maxxp = 50

        self.argent = 0

    
    def lvlup(self) -> None:
        """
        Appelé pour augmenter les statistiques du joueur lors d'un gain de niveau
        """
        self.atk += 5
        self.basepv += 5
        self.maxpv = self.calc_stat(self.basepv, 'pv')
        self.pv = self.maxpv
        self.maxxp = self.calc_stat(self.maxxp, 'xp')