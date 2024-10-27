from random import randint, choice

class Objets:
    def __init__(self, nom, prix, categorie, effet):
        self.nom = nom  # texte
        self.prix = prix  # entier
        self.categorie = categorie  # texte
        self.effet = effet  # entier

    def __str__(self):
        return f'{self.nom}: +{self.effet} {self.categorie if self.categorie != "Spécial" else "Toutes les sats"}'

class Shop:
    def __init__(self):
        self.simpatie = randint(0, 100)
        self.Valeurprix = 0
        self.reduction = 0  # Pourcentage de réduction appliqué
        self.Objetsdispo = []

        # Définitions des objets en magasin avec leurs catégories et effets.
        self.Objets = {
            "Dégats": [
                Objets('Torche', 10, 'Dégats', 2),
                Objets('Epée de légende', 50, 'Dégats', 5),
                Objets('Dague démoniaque', 70, 'Dégats', 7),
                Objets('Fouchette', 5, 'Dégats', 1),
                Objets('Turbo-marteau', 90, 'Dégats', 9)
            ],
            "Spécial": [
                Objets('Objets mystères', 40, 'objmystères', '2 objets aléatoires'),
                Objets('Bouclier inébranlable', 75, 'Defense', 9),
                Objets('Spatule dorée', 100, 'Spécial', 6)
            ],
            "Vitesse": [
                Objets('Botte draconique', 30, 'Vitesse', 5),
                Objets('Geox qui court vite', 60, 'Vitesse', 8),
                Objets('Botte du vieux pêcheur', 10, 'Vitesse', 1),
                Objets('vieille sabate', 15, 'Vitesse', 3)
            ],
            "Defense": [
                Objets('Casque du roi arthur', 40, 'Defense', 6),
                Objets('Chapeau de paille', 20, 'Defense', 2),
                Objets('Casserole', 5, 'Defense', 1),
                Objets('Bouclier doré', 50, 'Defense', 5)
            ]
        }

        # Générer des objets aléatoires pour le magasin
        for i in range(7):
            categorie = choice(list(self.Objets.keys()))
            objet = choice(self.Objets[categorie])
            self.Objetsdispo.append(objet)
        self.Objetsdispo.append(self.Objets["Spécial"][0])

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
                prix_final = round(objet.prix * (1 - self.reduction / 100))
                
                if joueur.argent >= prix_final:  # Vérifie que le joueur a assez d'argent
                    joueur.argent -= prix_final  # Déduit le prix réduit de l'argent du joueur
                    if objet.categorie == "objmystères":
                        objetsrecu = []
                        categorie = list(self.Objets.keys())
                        categorie.remove("Spécial")
                        for i in range(2):
                            categoriechoisi = choice(categorie)
                            obj = choice(self.Objets[categoriechoisi])
                            joueur.bag.ajouterobj(obj, joueur)
                            objetsrecu.append(obj)
                        self.Objetsdispo.remove(objet)
                        return f'Vous recevez {objetsrecu[0]} et {objetsrecu[1]} pour {prix_final} pièces (réduction de {self.reduction}%).'

                    joueur.bag.ajouterobj(objet, joueur)  # Ajoute l'objet dans l'inventaire du joueur
                    self.Objetsdispo.remove(objet)  # Retire l'objet du magasin
                    return f'Vous avez acheté {objet.nom} pour {prix_final} pièces (réduction de {self.reduction}%).'
                else:
                    return "Vous n'avez pas assez d'argent pour cet objet."
        return "Cet objet n'est pas disponible dans le magasin."
    
class Stuf:
    def __init__(self):
        self.Stuf = {"Dégats": [], "Vitesse": [], "Defense": [], "Spécial": []}

    def ajouterobj(self, objet, joueur):
        try:
            self.Stuf[objet.categorie].append(objet)  # Ajoute l'objet dans la bonne catégorie de l'inventaire
        except Exception as e:
            pass
        if objet.categorie == "Dégats":
            joueur.atk += objet.effet
        elif objet.categorie == "Defense":
            joueur.arm += objet.effet
        elif objet.categorie == "Vitesse":
            pass
        elif objet.categorie == "Spécial":
            joueur.atk += objet.effet
            joueur.arm += objet.effet
            joueur.pv += objet.effet

    def afficherobjs(self):
        return self.Stuf