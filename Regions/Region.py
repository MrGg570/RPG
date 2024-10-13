class Region:
    def __init__(self, name, minlvl, maxlvl, moblist, maxmob) -> None:
        self.name = name
        self.minlvl = minlvl
        self.maxlvl = maxlvl
        self.moblist = moblist
        self.maxmob = maxmob

    def shop(self):
        pass

    def eglise(self, player) -> None:
        player.pv = player.maxpv