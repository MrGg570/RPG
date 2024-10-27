from .zone import Zone

class Swamp(Zone):
    """
    Permet d'instancier une zone de type 'Swamp'
    """
    def __init__(self, name: str, lvl: tuple) -> None:
        super().__init__(name, 'Swamp', lvl, ('sorciere', 'esprit'))