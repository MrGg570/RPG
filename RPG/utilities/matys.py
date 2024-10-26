from random import randint, choice

class Objets:
    def __init__(self, nom, prix, categorie, effet):
        self.nom = nom  # texte
        self.prix = prix  # entier
        self.categorie = categorie  # texte
        self.effet = effet  # entier

    def __str__(self):
        return f'{self.nom}: +{self.effet} {self.categorie} -> {self.prix} pièces'

class Shop:
    def __init__(self):
        self.simpatie = randint(0, 100)
        self.Valeurprix = 0
        self.reduction = 0  # Pourcentage de réduction appliqué
        self.Objetsdispo = []

        # Définitions des objets en magasin avec leurs catégories et effets.
        self.Objets = {
            "Dégats": [
                Objets('Torche', 10, 'dégats', 2),
                Objets('Epée de légende', 50, 'dégats', 5),
                Objets('Dague démoniaque', 70, 'dégats', 7),
                Objets('Fouchette', 5, 'dégats', 1),
                Objets('Turbo-marteau', 90, 'dégats', 9)
            ],
            "Specials": [
                Objets('Objets mystères', 40, 'special', '2 objets aléatoires'),
                Objets('Bouclier inébranlable', 75, 'défense', 9),
                Objets('Spatule dorée', 100, 'toutes stats', 6)
            ],
            "Vitesse": [
                Objets('Botte draconique', 30, 'vitesse', 5),
                Objets('Geox qui court vite', 60, 'vitesse', 8),
                Objets('Botte du vieux pêcheur', 10, 'vitesse', 1),
                Objets('vieille sabate', 15, 'vitesse', 3)
            ],
            "Defense": [
                Objets('Casque du roi arthur', 40, 'défense', 6),
                Objets('Chapeau de paille', 20, 'défense', 2),
                Objets('Casserole', 5, 'défense', 1),
                Objets('Bouclier doré', 50, 'défense', 5)
            ]
        }

        # Générer des objets aléatoires pour le magasin
        for i in range(7):
            categorie = choice(list(self.Objets.keys()))
            objet = choice(self.Objets[categorie])
            self.Objetsdispo.append(objet)

    def Direbonjour(self):
        if self.simpatie > 50:
            if self.simpatie > 75:
                self.reduction = 25
                return "Wow ce vendeur est super joyeux, profitez-en avec une réduction de 25% !!"
            else:
                self.reduction = 15
                return "Le vendeur est de bonne humeur aujourd'hui, il est temps de faire des affaires avec une réduction de 15%..."
        elif self.simpatie < 50:
            if self.simpatie < 25:
                self.reduction = -25  # Augmentation de 25% des prix
                return "Le vendeur est fou de colère, mieux vaut ne pas négocier aujourd'hui... Les prix sont augmentés de 25%."
            else:
                self.reduction = -15  # Augmentation de 15% des prix
                return "Le vendeur est ronchon, les affaires vont être dures... Les prix sont augmentés de 15%."
        else:
            self.reduction = 0
            return "Le vendeur est normal. Les prix sont standard."

    def afficher_inventaire(self):
        return self.Objetsdispo

    def acheter_objet(self, nom_objet, joueur):
        # Recherche l'objet dans le magasin
        for objet in self.Objetsdispo:
            if objet.nom == nom_objet:
                # Calcul du prix avec la réduction
                prix_final = objet.prix * (1 - self.reduction / 100)
                
                if joueur.argent >= prix_final:  # Vérifie que le joueur a assez d'argent
                    joueur.argent -= prix_final  # Déduit le prix réduit de l'argent du joueur
                    joueur.bag.aajouterobj(objet)  # Ajoute l'objet dans l'inventaire du joueur
                    self.Objetsdispo.remove(objet)  # Retire l'objet du magasin
                    return f'Vous avez acheté {objet.nom} pour {prix_final:.2f} pièces (réduction de {self.reduction}%).'
                else:
                    return "Vous n'avez pas assez d'argent pour cet objet."
        return "Cet objet n'est pas disponible dans le magasin."
    
class Stuf:
    def __init__(self):
        self.Stuf = {"Dégats": [], "Vitesse": [], "Defense": []}

    def ajouterobj(self, objet):
        self.Stuf[objet[2]].append(objet)  # Ajoute l'objet dans la bonne catégorie de l'inventaire

    def afficherobjs(self):
        return self.Stuf