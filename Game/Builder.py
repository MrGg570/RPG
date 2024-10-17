from Persos import PersoPrincipal, Goblin, Spider

class Build:
    """
    Classe utiliser pour obtinir les monstres et le joueur
    """
    def __init__(self) -> None:
        pass

    @classmethod
    def build(self, name: str, lvl: int = 1):
    """
    Le décorateur permet d'appeler la fonction sans instancier d'objet.
    La fonction retourne le personnage demandé avec le niveau précisé 
    """
        name = name.lower()
        if name == 'goblin':
            return Goblin.Goblin(lvl)
        if name == 'player':
            return PersoPrincipal.Player()
        if name == 'spider':
            return Spider.Spider(lvl)
