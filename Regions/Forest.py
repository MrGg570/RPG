from .Region import Region

class Forest(Region):
    def __init__(self, minlvl, maxlvl) -> None:
        super().__init__("Fôret Profonde", minlvl, maxlvl, ['goblin','spider'])