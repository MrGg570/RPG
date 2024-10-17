class Combat:
    """
    Classe utilisée pour gérer les combats
    """
    def __init__(self, display) -> None:
        """
        Instancie un objet Combat avec l'objet display permettant d'affficher à l'écran
        """
        self.display = display

    def initialize(self, player, enemy): # A CHANGER
        self.player = player
        self.enemy = enemy
        self.display.combatinitdisplay(self)

    def tuto(self):
        """
        Déroulement du premier combat tutoriel
        """
        roundtrack = 0

        self.display.logbars("Bienvenue dans votre premier combat! \u25BA")
        self.display.waitinput()
        self.display.combatrefresh(menu = True, actions = ["Attaquer"], prompt="Vous pouvez attaquer l'ennemi en appuyant sur [underline bold blue]ENTRER[/underline bold blue] \u25BA")
        if self.player.attaquer(self.enemy):
            self.display.combatrefresh(prompt=f"[green]Vous[/green] [bold]attaquez[/bold] [bright_red]{self.enemy.name}[/bright_red] \u25BA")
        else:
            self.display.combatrefresh(prompt=f"[green]Vous[/green] avez [bold]raté votre attaque![/bold] \u25BA")
        self.display.waitinput()
        self.display.logbars("Maintenant, c'est au tour de l'[bold bright_red]ennemi[/bold bright_red] d'attaquer \u25BA")
        self.display.waitinput()
        if self.enemy.attaquer(self.player):
            self.display.combatrefresh(prompt=f"[bright_red]{self.enemy.name}[/bright_red] [green]vous[/green] [bold]attaque![/bold] \u25BA")
        else:
            self.display.combatrefresh(prompt=f"[bright_red]{self.enemy.name}[/bright_red] à [bold]raté son attaque![/bold] \u25BA")
        self.display.waitinput()
        self.display.logbars("D'autres options sont aussi disponible en combat. Vous pouvez utiliser [underline bold blue]FLECHE HAUT[/underline bold blue] et [underline bold blue]FLECHE BAS[/underline bold blue] pour naviguer \u25BA")
        self.display.waitinput()
        self.start()
        self.display.logbars("[bold gold1]Bravo![/bold gold1] [green]Vous[/green] avez terminé votre [bold]premier combat![/bold] \u25BA")
        self.display.waitinput()

    def start(self) -> bool:
        """
        Lance un combat
        """
        actions = ["Attaquer", "Ne rien faire"]

        while self.player.isalive() and self.enemy.isalive():
            actions = ["Attaquer", "Ne rien faire"]
            action = self.display.combatrefresh(True, actions)
            match action:
                case 0:
                    if self.player.attaquer(self.enemy):
                        self.display.combatrefresh(prompt=f"[green]Vous[/green] [bold]attaquez[/bold] [bright_red]{self.enemy.name}[/bright_red] \u25BA")
                    else:
                        self.display.combatrefresh(prompt=f"[green]Vous[/green] avez [bold]raté votre attaque![/bold] \u25BA")
                    self.display.waitinput()
                case 1:
                    self.display.combatrefresh(prompt=f"[green]Vous[/green] ne [bold]faites rien[/bold][white]...[/white] \u25BA")
                    self.display.waitinput()
            if self.enemy.isalive():
                if self.enemy.attaquer(self.player):
                    self.display.combatrefresh(prompt=f"[bright_red]{self.enemy.name}[/bright_red] [green]vous[/green] [bold]attaque![/bold] \u25BA")
                else:
                    self.display.combatrefresh(prompt=f"[bright_red]{self.enemy.name}[/bright_red] à [bold]raté son attaque![/bold] \u25BA")
                self.display.waitinput()
                
        return self.win() if self.player.isalive() else self.lose()
    
    def win(self) -> bool:
        """"
        Appelé lorqu'un combat est gagné
        """
        self.display.logbars(f":crossed_swords-emoji:  [green]Vous[/green] avez [bold]vaincu[/bold] [bright_red]{self.enemy.name}[/bright_red] [gold1]Lvl. {self.enemy.lvl}[/gold1] :tada::tada::tada: \u25BA")
        self.display.waitinput()


        goldamount = round(100 + 1.1 * self.enemy.lvl)
        xpamount = round(20 + 10* self.enemy.lvl)


        self.player.gold += goldamount
        self.player.xp += xpamount
        self.display.logbars(f":sparkles: [green]Vous[/green] [bold]gagnez[/bold] [bold gold1]{xpamount} XP[/bold gold1] :sparkler:  et [bold gold1]{goldamount} GOLD[/bold gold1] :money_bag: \u25BA")
        self.display.waitinput()
        if self.player.xp >= self.player.maxxp:
            self.player.lvl += 1
            self.player.xp -+ self.player.maxxp
            self.display.logbars(f":up_arrow-emoji:  [green]Vous[/green] passez [bold]niveau [gold1]{self.player.lvl}![/gold1][/bold] :tada::tada::tada: \u25BA")
            self.display.waitinput()
            self.display.logbars(f":sparkles: [green]Vous[/green] gagnez [bold gold1]{self.player.lvlup()} GOLD[/bold gold1] :money_bag: ! \u25BA")
            self.display.waitinput()
        else:
            self.display.logbars(xp=True)
            self.display.waitinput()
        return True

    def lose(self) -> bool:
        """
        Appelé quand un combat est perdu
        """
        self.display.logbars(f":skull: [green]Vous[/green] avez été [bold]terrassé[/bold] par [bright_red]{self.enemy.name}[/bright_red] [gold1]Lvl. {self.enemy.lvl}[/gold1] :cry::cry::cry: \u25BA")
        self.display.waitinput()
        return False
