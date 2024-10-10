from .Perso import Character

class Player(Character):
    def __init__(self, pv: int, atk: int, arm: int = 0) -> None:
        super().__init__(pv, atk, arm)