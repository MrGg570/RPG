from random import choice, randint

class Combat:
    """
    Classe qui permet de gérer les combats
    """
    def __init__(self, player: object, display: object) -> None:
        self.player = player
        self.display = display

    def fight(self, *enemies: object) ->  tuple:
        """
        Gère un combat entre le joueur et les ennemies donnés en arguments
        """
        enemiesalive = True
        slayer = enemies[0]
        while self.player.is_alive() and enemiesalive:
            backed = False
            actions = ['Attack', 'Bag', 'Flee']
            selected = self.display.menu(actions=actions, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))
            match selected:
                case 'Attack':
                    availableattacks = list(self.player.attacks.keys())
                    availableattacks.append('Back')
                    selected = self.display.menu(actions=availableattacks, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))

                    match selected:
                        case 'Back':
                            backed = True
                    
                        case _:
                            if len(enemies) == 1:
                                self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous attaquez {enemies[0].name} avec {selected}!')
                                success = self.player.attack(enemies[0], selected)

                            else:
                                enemieslist = list()
                                for i, e in enumerate(enemies):
                                    if e.is_alive():
                                        enemieslist.append(e.name + ' ({})'.format(i+1))
                                enemieslist.append('Cancel')
                                enemy = self.display.menu(actions=enemieslist, text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies))
                                if enemy != 'Cancel':
                                    self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous attaquez {enemies[int(enemy[-2])-1].name} ({enemy[-2]}) avec {selected}!')
                                    success = self.player.attack(enemies[int(enemy[-2])-1], selected)
                                
                                else:
                                    backed = True
                                    success = True
                                    
                            if not success:
                                self.display.menu(actions=['OK'], text=self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Vous ratez votre attaque!')

                case 'Bag':
                    if self.player.bag.potions > 0:
                        selected = self.display.menu(actions = ['Oui', 'Non'], text = self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'Voulez vous utiliser une potion pour récuperer 1/4 des pv?\nPotions restantes: {self.player.bag.potions}')
                        match selected:
                            case 'Non':
                                backed = True
                            case 'Oui':
                                self.player.bag.potions -= 1
                                self.player.pv += round((1/4) * self.player.maxpv)
                    else:
                        backed = True
                        self.display.menu(actions = ['OK'], text = self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = "Vous n'avez plus de potions. Rendez vous à l'église pour en récupérer")

                case 'Flee':
                    return 'flee', self.get_battle_data(enemies=enemies)

            if not backed:
                number = 0
                for i, e in enumerate(enemies):
                    if not e.is_alive():
                        number += 1
                    elif self.player.is_alive():
                        chosen = choice(list(e.attacks.keys()))
                        self.display.menu(actions = ['OK'], text = self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'{e.name} vous attaque avec {chosen}!' if len(enemies) == 1 else f'{e.name} ({i+1}) vous attaque avec {chosen}!')
                        if not e.attack(self.player, chosen):
                            self.display.menu(actions = ['OK'], text = self.display.get_multiple_healthbars(player=self.player, enemies=enemies), info = f'{e.name} rate son attaque!' if len(enemies) == 1 else f'{e.name} ({i+1}) rate son attaque!')
                        elif not self.player.is_alive():
                            slayer = e
                if number == len(enemies):
                    enemiesalive = False
        result = self.lose(self.display.get_multiple_healthbars(player=self.player, enemies=enemies), slayer) if enemiesalive else self.win(self.display.get_multiple_healthbars(player=self.player, enemies=enemies), enemies)
        return result, self.get_battle_data(enemies=enemies)
    
    def win(self, lastbar: str, enemies) -> bool:
        """
        Appelé quand le joueur gagne un combat, permet de calculer les récompenses
        """
        self.display.menu(actions = ['OK'], text = lastbar, info = ':tada: Vous avez gagné le combat!')

        exp = 0
        gold = 0

        for i in enemies:
            if i.name in ('Fallen angel', 'Soul eater'):
                exp += round(i.calc_stat(75,'xpdrop')/len(enemies))
            else:
                exp += round(i.calc_stat(25,'xpdrop')/len(enemies))
        
        for i in enemies:
            if i.name in ('Fallen angel', 'Soul eater'):
                gold += round(i.calc_stat(15,'xpdrop')/len(enemies))
            else:
                gold += round(i.calc_stat(5,'xpdrop')/len(enemies))

        self.display.menu(actions = ['OK'], text = lastbar, info = f':sparkles: [green]Vous[/green] [bold]gagnez[/bold] [bold gold1]{exp} XP[/bold gold1] :sparkler: et [bold gold1]{gold} pièces[/bold gold1] :money_bag: !')
        self.player.xp += exp
        self.player.argent += gold
        self.display.menu(actions = ['OK'], text = lastbar, info = self.display.get_xpbar(self.player) + '\n')

        while self.player.maxxp <= self.player.xp:
            self.display.menu(actions = ['OK'], text = lastbar, info = f'Vous passez niveau {self.player.lvl + 1}!')
            self.player.lvl += 1
            self.player.xp -= self.player.maxxp
            self.player.lvlup()
            self.display.menu(actions = ['OK'], text = lastbar, info = self.display.get_xpbar(self.player) + '\n')

        if enemies[0].name == 'Seigneur Stellaire':
            self.display.menu(actions = ['OK'], text = lastbar, info = 'Félicitation! Vous avez fini le jeu!')
            exit(1)
        
        return True

    def lose(self, lastbar: str, slayer: object) -> bool:
        """
        Appelé quand le joueur meurt
        """
        self.display.menu(actions = ['OK'], text = lastbar, info = f':skull: Vous avez été terrassé par {slayer.name} Lvl. {slayer.lvl}!')
        return False

    def get_battle_data(self, enemies: tuple) -> tuple:
        """
        A la fin du combat, calcule les dégats et le nombre d'ennemies tués et renvoi les valeurs
        """
        kills = 0
        dmg = 0
        for i in enemies:
            if not i.is_alive():
                kills += 1
                dmg += i.maxpv
            else:
                dmg += i.maxpv - i.pv
        return kills, dmg