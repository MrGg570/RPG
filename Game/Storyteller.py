from random import choice

import Regions.Forest
from .Textengine import Text
import Regions

lesregions = [Regions.Forest.Forest]
class Story:
    def __init__(self, display) -> None:
        self.text = Text(display)
        self.display = display
        self.region = choice(lesregions)(1,5)

    def tell(self, string: str, previouslines: list = []) -> None:
        self.text.render(string=string, previouslines=previouslines)

    def introduction(self):
        # self.tell("Bunch of stuff here, blablabla \u25BA")
        # self.display.waitinput()
        # self.tell("More stuff, blablabla, wonderful! \u25BA", ["Bunch of stuff here, blablabla \u25BA"])
        # self.display.waitinput()
        # self.tell("......")
        self.tell(f"Vous vous reveillez dans [bright_red]{self.region.name}[/bright_red]...")

    def getmob(self) -> str:
        return choice(self.region.moblist)