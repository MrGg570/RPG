from time import sleep

class Text:
    def __init__(self, display) -> None:
        self.display = display

    def render(self, string: str, previouslines: list = []) -> None:
        fragment = ""
        for i in string:
            fragment += i
            self.display.clear()
            for j in previouslines:
                self.display.log(j, "bold white", justify="center")
            self.display.log(fragment, "bold white", justify="center")
            sleep(0.05)
        