from .Textengine import Text

class Story:
    def __init__(self, display) -> None:
        self.text = Text(display)
        self.display = display

    def tell(self, string: str, previouslines: list = []) -> None:
        self.text.render(string=string, previouslines=previouslines)

    def introduction(self):
        self.tell("Bunch of stuff here, blablabla")
        self.display.waitinput()
        self.tell("More stuff, blablabla, wonderful!", ["Bunch of stuff here, blablabla"])

