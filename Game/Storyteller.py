from random import choice, randint

import Regions.Forest
from .Textengine import Text
import Regions

lesregions = [Regions.Forest.Forest]
class Story:
    def __init__(self, display) -> None:
        self.text = Text(display)
        self.display = display
        self.region = choice(lesregions)(2,10)
        self.map = list()
        self.map.append(self.region)

        self.mobdico = {'spider': 'Araignée', 'goblin': 'Goblin'}

    def tell(self, string: str, previouslines: list = []) -> None:
        self.text.render(string=string, previouslines=previouslines)

    def introduction(self):
        # self.tell("Bunch of stuff here, blablabla \u25BA")
        # self.display.waitinput()
        # self.tell("More stuff, blablabla, wonderful! \u25BA", ["Bunch of stuff here, blablabla \u25BA"])
        # self.display.waitinput()
        # self.tell("......")
        self.tell(f"Nouvelle zone découverte: [bright_red]{self.region.name}[/bright_red]...")

    def getmob(self) -> str:
        return choice(self.region.moblist)
    
    def getlevel(self, player):
        return randint(self.region.minlvl, player.lvl + 3) if player.lvl + 3 < self.region.maxlvl else randint(player.lvl - 5, self.region.maxlvl)
    
    def numberofenemies(self):
        return randint(1,self.region.maxmob)
    
    def outofcombat(self, actions:list) -> str:
        return self.display.menu(actions, 'MENU')

    def eglise(self, player) -> None:
        self.tell("Vous vous rendez à l'église pour prier...")
        self.region.eglise(player)
        self.tell("Vos [green]PV[/green] ont été restaurés \u25BA")
        self.display.waitinput()