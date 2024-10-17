from time import sleep

class Text:
    """
    Classe utilisée comme moteur de texte pour la narration
    """
    def __init__(self, display) -> None:
        """
        Instancie un moteur de texte avec l'objet display
        """
        self.display = display

    def render(self, string: str, previouslines: list = []) -> None:
        """
        Permet d'afficher une chaine de caractère caractère par caractère
        """
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
        
