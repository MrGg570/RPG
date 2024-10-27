from ..character import Character

class Warrior(Character):
    def __init__(self, name: str) -> None:
        self.basepv = 150
        super().__init__(name=name, pv=self.basepv, atk=60, arm=0, lvl=1)
        self.attacks.update({'Charge':(100, 95),'Punch': (150, 80)})
        self.isplayer = True

        self.xp = 0
        self.maxxp = 50

        self.argent = 0

    
    def lvlup(self):
        self.atk += 5
        self.basepv += 5
        self.maxpv = self.calc_stat(self.basepv, 'pv')
        self.pv = self.maxpv
        self.maxxp = self.calc_stat(self.maxxp, 'xp')