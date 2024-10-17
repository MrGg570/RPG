from .Region import Region

class Forest(Region):
    """
    Classe utilisée pour instancier une région de type Forêt
    """
    def __init__(self, minlvl, maxlvl) -> None:
        super().__init__("Fôret Profonde", minlvl, maxlvl, ['goblin','spider'], maxmob=3)
