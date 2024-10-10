class Character:
    """
    Classe de base pour définir des personnages
    """
    def __init__(self, pv:int, atk:int, arm: int=0) -> None:
        self.maxpv = pv
        self.pv = pv
        self.atk = atk
        self.arm = arm

    def attaquer(self, other: object) -> bool:
        # probas
        # if probas:
        other.pv -= self.atk
        return  True # if probas else False