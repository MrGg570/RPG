class Region:
    """
    Classe utiliser comme base pour les régions
    """
    def __init__(self, name, minlvl, maxlvl, moblist, maxmob) -> None:
        """
        Instancier une région avec son nom, le niveau minimum et maximum des monstres, la liste des monstres de la région et le nombre maximum de monstre rencontrables d'afilés
        """
        self.name = name
        self.minlvl = minlvl
        self.maxlvl = maxlvl
        self.moblist = moblist
        self.maxmob = maxmob

    def shop(self):
        pass

    def eglise(self, player) -> None:
        """
        Appelé quand le joueuer s'est rendu à l'église pour restaurer ses pvs
        """
        player.pv = player.maxpv
