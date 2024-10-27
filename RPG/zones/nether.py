from .zone import Zone

class Nether(Zone):
    """
    Permet d'instancier une zone de type 'Neither'
    """
    def __init__(self, name: str, lvl: tuple) -> None:
        super().__init__(name, 'Nether', lvl, ('dragonneau', 'phenix'))