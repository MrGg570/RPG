from RPG.zones import forest, desert, swamp, nether, boss

class Build:
    def __init__(self) -> None:
        pass

    @classmethod
    def create_zone(self, name: str, type: str, lvl: tuple) -> object:
        """
        Permet d'instancier une zone selon les paramètres
        """
        type = type.lower()
        match type:
            case 'forest':
                return forest.Forest(name=name, lvl=lvl)
            case 'desert':
                return desert.Desert(name=name, lvl=lvl)
            case 'swamp':
                return swamp.Swamp(name=name, lvl=lvl)
            case 'nether':
                return nether.Nether(name=name, lvl=lvl)
            case 'boss':
                return boss.Boss(lvl=lvl)
            case _:
                raise Exception(f'<{type}> is not a valid zone type')