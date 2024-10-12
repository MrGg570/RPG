from time import sleep

class Text:
    def __init__(self, display) -> None:
        self.display = display

    def render(self, string: str, previouslines: list = []) -> None:
        fragment = ""
        slowdown = [",",".", "?", "!"]
        closing = False
        for i in string:
            if i != "[" and not closing:
                fragment += i
                self.display.clear()
                for j in previouslines:
                    self.display.log(j, "bold white", justify="center")
                self.display.log(fragment, "bold white", justify="center")
                sleep(0.1 if i not in slowdown else 0.4)
            else:
                fragment +=i               
                closing = True if i != "]" else False
        