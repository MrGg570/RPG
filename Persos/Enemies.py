from .Perso import Character

class Enemy(Character):
    def __init__(self, pv: int, atk: int, arm: int = 0) -> None:
        super().__init__('Goblin', pv, atk, arm)