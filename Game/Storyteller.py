from random import choice, randint

import Regions.Forest
from .Textengine import Text
import Regions

lesregions = [Regions.Forest.Forest]
class Story:
    """
    Classe utiliser pour instancier un objet Story qui permet de narrer et gérer le scénario
    """
    def __init__(self, display) -> None:
        """
        S'instancie avec un objet Display
        Possède les attributs text (objet Text), display (objet Display), region (une région aléatoire), map (liste de régions), mobdico (traduction du nom des mobs pour l'affichage)
        """
        self.text = Text(display)
        self.display = display
        self.region = choice(lesregions)(2,10)
        self.map = list()
        self.map.append(self.region)

        self.mobdico = {'spider': 'Araignée', 'goblin': 'Goblin'}

    def tell(self, string: str, previouslines: list = []) -> None:
        """
        Affiche à l'aide du moteur de texte une chaine de caractères
        """
        self.text.render(string=string, previouslines=previouslines)

    def introduction(self):
        """
        Narration
        Introduction dans le jeu
        """
        # self.tell("Bunch of stuff here, blablabla \u25BA")
        # self.display.waitinput()
        # self.tell("More stuff, blablabla, wonderful! \u25BA", ["Bunch of stuff here, blablabla \u25BA"])
        # self.display.waitinput()
        # self.tell("......")
        self.tell(f"Nouvelle zone découverte: [bright_red]{self.region.name}[/bright_red]...")

    def getmob(self) -> str:
        """
        Retourne un monstre disponible dans la région actuelle
        """
        return choice(self.region.moblist)
    
    def getlevel(self, player):
        """
        Retourne un monstre de niveau approprié selon le niveau du joueur et la région actuelle
        """
        return randint(self.region.minlvl, player.lvl + 3) if player.lvl + 3 < self.region.maxlvl else randint(player.lvl - 5, self.region.maxlvl)
    
    def numberofenemies(self):
        """
        Retourne le nombre de monstre à combattre selon la région actuelle
        """
        return randint(1,self.region.maxmob)
    
    def outofcombat(self, actions:list) -> str:
        """
        Affiche un menu avec une liste d'action possible
        Retourne l'action choisie
        """
        return self.display.menu(actions, 'MENU')

    def eglise(self, player) -> None:
        """
        Permet au joueur de récupérer de la vie
        """
        self.tell("Vous vous rendez à l'église pour prier...")
        self.region.eglise(player)
        self.tell("Vos [green]PV[/green] ont été restaurés \u25BA")
        self.display.waitinput()
