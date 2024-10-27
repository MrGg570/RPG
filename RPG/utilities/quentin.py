from random import choice

class Event:

    def __init__(self):
        self.event_negatif = [
            ("Poche trouée: Par avarice mesquine, le refus d'acheter un nouveau pantalon vous a coûté 10 pièces !", 'argent', -10),
            ("Baba-cool pas très cool: B'Orc Marley vous poursuit et vous trébuchez laissant derrière vous vos bottes... Vous êtes pieds nus !", 'stuff', -1),
            ("Narcolepsie: En pleine pause casse-croûte, le sommeil vous rattrape... Votre casque a disparu !", 'stuff', -1),
            ("Abus de Fast-Food: Vous subissez une intoxication alimentaire. Ce ragoût n'avait pas l'air complètement innocent...", 'pv', -15),
            ("Satané blague !: Un elfe vous attire dans un trou pour se moquer de vous... Vous avez l'air ridicule !", 'argent', -15)
        ]
        self.event_positif = [
            ("Gain d'argent: Un gobelin malicieux décide de vous dédommager pour pardonner ses méfaits des anciens temps !", 'argent', 15),
            ("Bouclier enchanté: En explorant une vieille bibliothèque, vous trouvez un vieux parchemin qui renforce vos défenses !", 'def', 10),
            ("Force surhumaine: Vous mangez un champignon inconnu au bataillon et gagnez de la force supplémentaire !", 'atk', 5),
            ("Docteur Maboul: Un médecin ayant eu son diplôme lors du COVID fait des tests sur vous !", 'pv', 20),
            ("Roulette pas Russe: Moins risquée mais plus rentable... Gagnez un objet au hasard !", 'stuff', 1),
            ("Dopage suspicieux: Votre vitesse augmente, mais votre vie se réduit.", 'vit', 10),
            ("Baba-cool très cool: Un mage retraité sous champignon vous donne un remède...", 'stuff', 1),
            ("Bénédiction gargantuesque: Non, vous ne devenez pas un dieu, vos stats sont juste augmentées de 10%.", 'atk', 10),
            ("Quitte ou double: Bonhomme ou pas bonhomme? Vous avez le choix de doubler vos pièces, mais attention ! Vous risquez de tout perdre.", 'double', 0)  # Choix aléatoire à gérer
        ]

    def evenement(self):
        eventtype = choice(['positif', 'negatif'])
        if eventtype == 'positif':
            evenement = choice(self.event_positif)
            return evenement[0], evenement[1], evenement[2]
        else:
            evenement = choice(self.event_negatif)
            return evenement[0], evenement[1], evenement[2]