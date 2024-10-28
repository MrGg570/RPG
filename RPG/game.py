from time import sleep

from RPG.utilities import characterbuilder, display, fight, zonebuilder, quentin
from random import randint, choice

class RPG:
    """
    Classe utilisée pour gérer l'entiereté du jeu et des modules
    """
    def __init__(self, skipintro: bool = False) -> None:
        self.screen = display.Display()
        self.event = quentin.Event()

        self.region = list()
        zonetype = ('forest', 'desert', 'swamp', 'nether')
        zonename = {
            'forest': ['Deep forest', 'Scary forest', 'Death forest', 'Spooky forest', 'Unpleasant forest'],
            'desert': ['Dry desert', 'Creepy desert', 'Torrid desert', 'Burning desert', 'Unpleasant desert'],
            'swamp': ['Deep swamp', 'Scary swamp', 'Death swamp', 'Spooky swamp', 'Unpleasant swamp'],
            'nether': ['Dry nether', 'Creepy nether', 'Torrid nether', 'Burning nether', 'Unpleasant nether']
                    }
        for i in range(5):
            chosentype = choice(zonetype)
            self.region.append(zonebuilder.Build.create_zone(name=choice(zonename[chosentype]), type=chosentype, lvl=(i*10+1, i*10+10)))
            zonename[chosentype].pop(zonename[chosentype].index(self.region[-1].name)) # Pour que chaque zone ai un nom différent
        self.region.append(zonebuilder.Build.create_zone(name='', type='boss', lvl=(50,50)))
        self.currentzone = self.region[0]

        self.quests = {1:['Vaincre 10 ennemies', 0, 10, 'kill'], 2: ['Infliger 1 000 points de dégat', 0, 1000, 'dmg'], 3:['Vaincre 50 ennemies', 0, 50, 'kill'], 4: ['Infliger 10 000 points de dégat', 0, 10000, 'dmg'],5:['Vaincre 150 ennemies', 0, 150, 'kill']}

        start = False
        while not start:
            selected = self.screen.menu(actions=['Démarrer', 'Options', 'Quitter'], text=self.screen.get_title('RPG'))
            match selected:
                case 'Démarrer':
                    start = True

                case 'Options':
                    selected =self.screen.menu(actions=[f'Skip intro : {skipintro}', 'Langue : ', 'Retour'], text=self.screen.get_title('RPG'))
                    match selected:
                        case 'Skip intro : True':
                            skipintro = False
                        case 'Skip intro : False':
                            skipintro = True
                        
                        case _:
                            pass

                case 'Quitter':
                    self.screen.clear()
                    exit(1)

        self.difficulty = 1.5
        self.specialmonsters = ('Soul eater', 'Fallen angel')

        if skipintro:
            self.player = characterbuilder.Build.create_player(name='ImThePlayerOwO')

            self.combat = fight.Combat(player=self.player, display=self.screen)

            return None
        validname = False

        while not validname:
            self.tell("Quel est tom nom, aventurier?\n", style='bold gold1')
            name = input('>>> ')
            if len(name)>25:
                self.tell("Oh... On dirait que ce nom est trop long, peux-tu en essayer un autre?", style='bold gold1')
                self.screen.menu(actions=['OK'], text="[bold gold1]Oh... On dirait que ce nom est trop long, peux-tu en essayer un autre?[/bold gold1]")
            elif name == '':
                self.tell("Oh... Ce nom ne fait malheureusement pas l'affaire, essaye en un autre.", style='bold gold1')
                self.screen.menu(actions=['OK'], text="[bold gold1]Oh... Ce nom ne fait malheureusement pas l'affaire, essaye en un autre.[/bold gold1]")
            else:
                validname = True

        self.tell(f"Donc ton nom est [bold green]{name}[/bold green]... Et quelle est ta classe?", style='bold gold1')
        self.player = characterbuilder.Build.create_player(name=name, playerclass=self.screen.menu(actions=['Archer', 'Knight', 'Mage', 'Warrior'], text=f"[bold gold1]Donc ton nom est [bold green]{name}[/bold green]... Et quelle est ta classe?[/bold gold1]\n"))

        self.tell(f"On dirait que tu t'es réveillé dans {self.currentzone.type}...", style='bold gold1')

        self.combat = fight.Combat(player=self.player, display=self.screen)
            
    def tell(self, string: str, style: str | None = None) -> None:
        """
        Affiche un texte caractère par caractère
        """
        fragment = ''
        slowdown = (',','.', '?', '!')
        closing = False
        for i in string:
            if i != "[" and not closing:
                fragment += i
                self.screen.clear()
                self.screen.print(fragment, style=style)
                sleep(0.05 if i not in slowdown else 0.3)
            else:
                fragment +=i               
                closing = True if i != "]" else False


    def battle(self) -> tuple:
        """
        Crée des ennemies et lance un combat
        """
        if self.currentzone.type.lower() == 'boss':
            enemiesnumber = 1
        else:
            enemiesnumber = randint(1, 3)
        enemies = list()
        if enemiesnumber == 1 and randint(0, 100) <= 5 and not self.currentzone.type.lower() == 'boss':
            name = self.get_enemy(True)
        else:
            name = self.get_enemy()
        for i in range(enemiesnumber):
            enemies.append(characterbuilder.Build.create_enemy(name=name, lvl=self.get_level() if name not in self.specialmonsters else self.player.lvl, enemies=enemiesnumber, f=self.difficulty))
        return self.combat.fight(*enemies)
    
    def get_enemy(self, special: bool = False) -> str:
        """
        Retourne un ennemi parmis ceux disponible dans la zone
        """
        if self.currentzone.type.lower() == 'boss':
            return 'seigneur stellaire'
        return choice(self.currentzone.monsters) if not special else choice(self.specialmonsters)
    
    def get_level(self) -> int:
        """
        Retourne un niveau d'ennemi approprié par rapport à la zone et au joueur
        """
        if self.currentzone.type.lower() == 'boss':
            return 50
        if self.currentzone.lvl[0] > self.player.lvl:
            return randint(self.currentzone.lvl[0], self.currentzone.lvl[0]+4)
        chosenlvl = 9999
        while chosenlvl > self.player.lvl+1:
            chosenlvl = randint(*self.currentzone.lvl)
        return chosenlvl
    
    def global_menu(self):
        """
        Gère le menu prinbcipal du jeu
        """
        selected = self.screen.menu(actions=['Combattre', 'Sac', 'Boutique', 'Eglise', 'Carte', 'Quêtes', 'Quitter'], text=self.screen.get_title('MENU'))

        match selected:
            case 'Combattre':
                result,  data = self.battle()
                if result == 'flee':
                    self.tell('Vous fuyez le combat...')
                    goldloss = round(randint(5,10) * self.player.lvl)
                    self.screen.menu(actions=['OK'], text=f'Vous perdez {goldloss} pièces :money_bag: pendant votre fuite!')
                    self.player.argent -= goldloss
                    if self.player.argent < 0: self.player.argent = 0
                elif result:
                    pass
                else:
                    self.respawn()
                self.update_quests(data)
                if randint(0,100) >= 90:
                    self.get_event()

            case 'Sac':
                self.sac()

            case 'Boutique':
                self.shop()
                
            case 'Eglise':
                self.eglise()

            case 'Carte':
                actions = ['Zone suivante', 'Retour'] if self.currentzone == self.region[0] else ['Zone précédente', 'Retour'] if self.currentzone == self.region[-1] else ['Zone suivante', 'Zone précédente', 'Retour']
                selected = self.screen.menu(actions=actions, text=self.screen.get_map(self.region, self.currentzone))
                match selected:
                    case 'Zone suivante':
                        if self.is_quest_done(self.quests[self.region.index(self.currentzone)+1]):
                            self.currentzone = self.region[self.region.index(self.currentzone)+1]
                            self.screen.menu(actions=['OK'], text=self.screen.get_map(self.region, self.currentzone), info=f'Vous entrez dans {self.currentzone.name}')
                        else: 
                             self.screen.menu(actions=['OK'], text=self.screen.get_map(self.region, self.currentzone), info=f"[bold bright_red]Vous devez d'abord terminer la quête {self.region.index(self.currentzone)+1}: {self.quests[self.region.index(self.currentzone)+1][0]}")

                    case 'Zone précédente':
                        self.currentzone = self.region[self.region.index(self.currentzone)-1]
                        self.screen.menu(actions=['OK'], text=self.screen.get_map(self.region, self.currentzone), info=f'Vous entrez dans {self.currentzone.name}')

                    case _:
                        pass

            case 'Quêtes':
                self.screen.menu(actions=['OK'], text=self.screen.get_quests(self.quests))

            case 'Quitter':
                self.quit()

    def is_quest_done(self, quest: list) -> bool:
        """
        Vérifie si une quête est terminée
        """
        return quest[1] >= quest[2]
    
    def update_quests(self, data: tuple):
        """
        Met à jour les quêtes
        """
        kills, dmg = data
        for quest in self.quests.keys():
            if self.quests[quest][3] == 'kill':
                self.quests[quest][1] += kills
            elif self.quests[quest][3] == 'dmg':
                self.quests[quest][1] += dmg

    def eglise(self, respawn: bool = False) -> None:
        """
        Permet au joueur de récupérer ses points de vies et des potions
        """
        if not respawn:
            self.tell(string="Vous vous rendez à l'église pour prier...")
        self.screen.menu(actions=['OK'], text='Vos [bold green]PV[/bold green] et [bold bright_red]Potions[/bold bright_red] ont été restaurés!')
        self.player.pv = self.player.maxpv
        self.player.bag.potions = 2

    def respawn(self) -> None:
        """
        Appelé quand le joueur meurt lors d'un combat
        """
        self.tell(string="Vous vous réveillez à l'église...")
        goldloss = round(randint(5,10) * self.player.lvl)
        self.screen.menu(actions=['OK'], text=f'Vous avez perdu {goldloss} pièces :money_bag:!')
        self.player.argent -= goldloss
        if self.player.argent < 0: self.player.argent = 0
        self.eglise(True)

    def shop(self) -> None:
        """
        Permet de gérer l'interaction avec la boutique
        """
        if self.currentzone.shopfirsttime:
            text = self.currentzone.shop.Direbonjour()
            self.tell(text)
            self.screen.menu(actions=['OK'], text=text)
            self.currentzone.shopfirsttime = False
        while True:
            liste = list()
            for i in self.currentzone.shop.afficher_inventaire():
                liste.append(str(i) + f' -> {round(i.prix * (1 - self.currentzone.shop.reduction / 100))} pièces')
            liste.append('Back')
            selected = self.screen.menu(actions=liste, text=f'Vous avez {self.player.argent} pièces')
            match selected:
                case 'Back':
                    return
                
                case _:
                    self.screen.menu(actions=['OK'], text=self.currentzone.shop.acheter_objet(selected.split(':')[0], self.player))

    def sac(self) -> None:
        """
        Affiche un menu avec le contenu du sac
        """
        self.screen.menu(actions=['OK'], text=self.affichagesac(self.player.bag.afficherobjs()))

    def affichagesac(self, dico: dict) -> str:
        """
        Retourne le contenu du sac
        """
        string = f'Pièces :money_bag:: {self.player.argent}\n\n'
        for key in dico:
            string += key + ':\n'
            if len(dico[key]) == 0:
                string += '  /\n\n'
            else:
                i = 0
                for item in dico[key]:
                    i += 1
                    if len(dico[key]) > i:
                        string += '  - ' + str(item) + '\n'
                    else:
                        string += '  - ' + str(item) + '\n\n'      
        return string
    
    def get_event(self) -> None:
        """
        Appelé lorsqu'on veut lancer un événement. Gère l'affichage et les effets d'un evenement tiré au hasard
        """
        self.screen.menu(actions=['OK'], text='Oh! Un évenement se déclenche!')
        texte, catego, montant = self.event.evenement()
        self.screen.menu(actions=['OK'], text=texte)
        match catego:
            case 'argent':
                self.screen.menu(actions=['OK'], text=f'Vous gagnez {montant} pièces' if montant>0 else f'Vous perdez {abs(montant)} pièces')
                self.player.argent += self.player.calc_stat(montant, 'xp')
                if self.player.argent < 0: self.player.argent = 0
            case 'pv':
                self.screen.menu(actions=['OK'], text=f'Votre statistique de points de vie augmente de {montant}' if montant>0 else f'Votre statistique de points de vie diminue de {abs(montant)}')
                self.player.basepv += montant
                if self.player.basepv < 1: self.player.basepv = 1
                self.player.maxpv = self.player.calc_stat(self.player.basepv, 'pv')
            case 'atk':
                self.screen.menu(actions=['OK'], text=f"Votre statistique d'attaque augmente de {montant}" if montant>0 else f"Votre statistique de d'attaque diminue de {abs(montant)}")
                self.player.atk += montant
                if self.player.atk < 1: self.player.atk = 1
            case 'def':
                self.screen.menu(actions=['OK'], text=f'Votre statistique de défense augmente de {montant}' if montant>0 else f'Votre statistique de défense diminue de {abs(montant)}')
                self.player.arm += montant
                if self.player.arm < 0: self.player.arm = 0
            case 'stuff':
                if montant < 0:
                    if not self.player.bag.estvide():
                        objet = None
                        while objet == None :
                            cat = choice(list(self.player.bag.Stuf.keys()))
                            if not len(self.player.bag.Stuf[cat]) == 0:
                                objet = choice(self.player.bag.Stuf[cat]) if len(self.player.bag.Stuf[cat]) > 1 else self.player.bag.Stuf[cat][0]
                        self.player.bag.enleverobj(objet, self.player)
                        self.screen.menu(actions=['OK'], text=f'Vous perdez {objet}!')
                    else:
                        self.screen.menu(actions=['OK'], text=f"Vous n'avez pas d'objets à perdre")
                else:
                    cat = choice(['Dégats', 'Spécial', 'Vitesse', 'Defense'])
                    obj = choice(self.currentzone.shop.Objets[cat])
                    self.player.bag.ajouterobj(obj, self.player)
                    self.screen.menu(actions=['OK'], text=f'Vous avez gagné {obj}!')
            case 'double':
                selected = self.screen.menu(actions=['Oui', 'Non'], text=f'Voulez vous tenter votre chance?')
                match selected:
                    case 'Oui':
                        if randint(0,100)>=50:
                            self.screen.menu(actions=['OK'], text='Vous avez gagné votre pari! Vos pièces ont été doublées')
                        else:
                            self.screen.menu(actions=['OK'], text='Vous avez perdu!')
                    case _:
                        pass
    
    def quit(self) -> None:
        """
        Appelé pour quitter le jeu
        """
        if self.screen.menu(actions=['Oui', 'Non'], text='Êtes vous sûr de vouloir quitter?') == 'Oui':
            exit(1)