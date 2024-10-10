from Persos import Enemies, PersoPrincipal

class Build:
    def __init__(self) -> None:
        pass

    @classmethod
    def build(self, name: str, pv: int, atk: int, arm: int = 0):
        name = name.lower()
        if name == 'enemy':
            return Enemies.Enemy(pv, atk, arm)
        if name == 'player':
            return PersoPrincipal.Player(pv, atk, arm)