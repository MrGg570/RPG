from Persos import PersoPrincipal
from Persos import Goblin

class Build:
    def __init__(self) -> None:
        pass

    @classmethod
    def build(self, name: str, lvl: int = 1):
        name = name.lower()
        if name == 'goblin':
            return Goblin.Goblin(lvl)
        if name == 'player':
            return PersoPrincipal.Player()