class Combat:
    def __init__(self, display) -> None:
        self.display = display

    def initialize(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.display.combatinitdisplay(self)

    def start(self) -> bool:

        actions = ["Attaquer", "Ne rien faire"]

        self.display.clear()
        self.display.log("Début du combat", "bold white")
        self.display.waitinput()
        while self.player.isalive() and self.enemy.isalive():
            actions = ["Attaquer", "Ne rien faire"]
            action = self.display.combatrefresh(True, actions)
            match action:
                case 0:
                    if self.player.attaquer(self.enemy):
                        self.display.combatrefresh(prompt=f"Vous attaquez {self.enemy.name}")
                    else:
                        self.display.combatrefresh(prompt=f"Vous avez raté votre attaque!")
                    self.display.waitinput()
                case 1:
                    self.display.combatrefresh(prompt=f"Vous ne faites rien...")
                    self.display.waitinput()
            if self.enemy.isalive():
                if self.enemy.attaquer(self.player):
                    self.display.combatrefresh(prompt=f"{self.enemy.name} vous attaque!")
                else:
                    self.display.combatrefresh(prompt=f"{self.enemy.name} à raté son attaque!")
                self.display.waitinput()
                
        return self.win() if self.player.isalive() else self.lose()
    
    def win(self) -> bool:
        self.display.logbars(f":crossed_swords-emoji:  Vous avez vaincu {self.enemy.name} Lvl. {self.enemy.lvl} :tada::tada::tada:")
        self.display.waitinput()


        goldamount = round(100 + 1.1 * self.enemy.lvl)
        xpamount = round(10 + 1.1 * self.enemy.lvl)


        self.player.gold += goldamount
        self.player.xp += xpamount
        self.display.logbars(f":sparkles: Vous gagnez [bold gold1]{xpamount} XP[/bold gold1] :sparkler:  et [bold gold1]{goldamount} GOLD[/bold gold1] :money_bag:")
        self.display.waitinput()
        if self.player.xp >= self.player.maxxp:
            self.player.lvl += 1
            self.player.xp -+ self.player.maxxp
            self.display.logbars(f":up_arrow-emoji:  Vous passez niveau {self.player.lvl}! :tada::tada::tada:")
            self.display.waitinput()
            self.display.logbars(f":sparkles: Vous gagnez [bold gold1]{self.player.lvlup()} GOLD[/bold gold1] :money_bag: !")
            self.display.waitinput()
        else:
            self.display.logbars(xp=True)
            self.display.waitinput()
        return True

    def lose(self) -> bool:
        self.display.logbars(f":skull: Vous avez été terrassé par {self.enemy.name} Lvl. {self.enemy.lvl} :cry::cry::cry:")
        self.display.waitinput()
        return False