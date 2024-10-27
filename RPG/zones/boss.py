from .zone import Zone

class Boss(Zone):
    """
    Permet d'instancier une zone de type 'boss'
    """
    def __init__(self, lvl: tuple) -> None:
        super().__init__('Planète du seigneur stellaire', 'boss', lvl, None)