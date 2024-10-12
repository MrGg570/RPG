from Persos import PersoPrincipal
from Persos import Goblin

class Build:
    def __init__(self) -> None:
        pass

    @classmethod
    def build(self, name: str, pv: int, atk: int, arm: int = 0):
        name = name.lower()
        if name == 'goblin':
            return Goblin.Goblin(pv, atk, arm)
        if name == 'player':
            return PersoPrincipal.Player(pv, atk, arm)