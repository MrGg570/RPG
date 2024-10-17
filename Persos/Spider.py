from .Perso import Character

class Spider(Character):
    """
    Classe utilisée pour instancier une Araignée
    """
    def __init__(self, lvl) -> None:
        super().__init__('Araignée', pv=4*lvl, atk=3*lvl, arm=0, lvl=lvl, dodge=2)
