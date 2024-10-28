# Compte-rendu

**__Table des matières:__**

- [Compte-rendu](#compte-rendu)
- [Détails du projet](#détails-du-projet)
  - [Jeu de rôle (RPG)](#jeu-de-rôle-rpg)
  - [Règles](#règles)
    - [Menus](#menus)
    - [Joueur](#joueur)
    - [Ennemis](#ennemis)
    - [Déplacement](#déplacement)
    - [Boutique et inventaire](#boutique-et-inventaire)
    - [Combat](#combat)
- [Structures de données](#structures-de-données)
  - [Personnages](#personnages)
    - [Attributs](#attributs)
    - [Méthodes](#méthodes)
  - [Zones](#zones)
    - [Attributs](#attributs-1)
  - [Affichage](#affichage)
    - [Attributs](#attributs-2)
    - [Méthodes](#méthodes-1)
  - [Boutique et inventaire](#boutique-et-inventaire-1)
    - [Attributs](#attributs-3)
    - [Méthodes](#méthodes-2)
- [Répartition](#répartition)
  - [Matys](#matys)
  - [Quentin](#quentin)
  - [Bastien](#bastien)
- [Comment jouer](#comment-jouer)
  - [Télécharger le code](#télécharger-le-code)
  - [Extraire le zip](#extraire-le-zip)
  - [Installer les dépendances](#installer-les-dépendances)
  - [Lancer le jeu](#lancer-le-jeu)
    - [⚠️ Si vous avez le moindre problème, une version compilé est comprise dans les fichier (`RPG\build\RPG.exe`)](#️-si-vous-avez-le-moindre-problème-une-version-compilé-est-comprise-dans-les-fichier-rpgbuildrpgexe)

# Détails du projet

## Jeu de rôle (RPG)

Le projet consiste en la création d’un RPG (Role Playing Game) en Python en adoptant le paradigme de la programmation orientée objet (POO). L’idée est de concevoir un jeu où le joueur incarne un personnage évoluant dans un univers fictif avec des ennemis, des défis, et des éléments d'exploration et de combat.

## Règles

__**Sommaire**__

- [Navigation dans les menus](#menus)

- [Le Joueur](#joueur)

- [Les Ennemis](#ennemis)

- [Système de déplacement](#déplacement)

- [Système de combat](#combat)

### Menus

Dans notre RPG, toutes les actions se réalisent à travers des menu.

- Menu de démarrage:
  - Permet de démarrer le jeu (création du personnage)
  - Permet de changer les options:
    - Skipintro: passe la création du personnage (Nom fixé par avance, classe prédéfinie)
    - Language: non implémenté, aurait permis de changer la langue entre français et anglais
  - Permet de quitter le programme
  
.

- Menu principal:
  - Accès aux combats
  - Affichage des objets du joueur
  - Accès à la boutique de la zone
  - Accès à l'église pour les soins
  - Accès à la carte pour changer de zone
  - Accès au tableau de quêtes
  - Quitter le jeu

### Joueur

Le joueur est crée au démarrage du jeu (après le menu de démarrage). Il est instancié avec le nom donné par l'utilisateur ainsi que la classe précisé, au niveau 1.

Il possède plusieurs attributs utiles au bon déroulement du jeu: points de vie, attaques, statistique de défense...

### Ennemis 

Les ennemis sont proche du joueur: ils possèdent aussi les statistiques de points de vie, défense... ainsi que différentes attaque. Ils sont toutefois instancié avec un nom prédéfini (un goblin sera toujour appelé 'Goblin') et un niveau dépendant du contexte.

### Déplacement 

Les déplacements s'effectuent à travers le menu 'Carte' du [menu principal](#menus). Le joueur à la possibilité, si les quêtes correspondantes ont été effectués, de se déplacer à la zone ou à la zone précédentes (si elles existent).

### Boutique et inventaire

Dans chaque zone du jeu se trouve une boutique.

Pour chacune de ces boutiques, le niveau de sympathie du vendeur est différent et amène à des coût augmentés ou réduits (appelés *réductions* dans le jeu).

Chaque boutique propose une liste d'objets différente, tirée d'une liste prédéfinie.

Dans l'inventaire (sac), les objets sont trié par types (Dégats, défense...)

*⚠️ La statistique de vitesse n'a pas été implémenté*

### Combat 

Lorsque le joueur entre en combat, il est mit face à un ou plusieurs ennemis (jusqu'à 3). Les statistiques des ennemis sont ajustés de manière à rendre le combat équilibré selon leur nombre. 

Le joueur se retrouve face à un [menu](#menus) lui proposant 3 actions:
- Attaquer 
- Ouvrir son sac
- Fuir

Choisir attaquer ouvre un sous-menu proposant les différentes attaques disponibles, et ensuite une liste des ennemis s'il y en a plus d'un. Les dégats du joueur sur l'ennemis est calculé puis appliqué

Choisir sac ouvre un sous-menu permetant d'utiliser une potion (restaure 1/4 des points de vie, récupération gratuite à l'église)

C'est ensuite au tour de(s) ennemi(s) d'ataquer.

Si l'option fuite a été choisie, alors le joueur quitte le combat prématurément, perdant quelque pièces par la même occasion.

# Structures de données

Structure de donnée par élément

- [Personnages](#personnages)
- [Zones](#zones)
- [Affichage](#affichage)
- [Boutique et inventaire](#boutique-et-inventaire-1)

## Personnages

### Attributs

Il a été choisi de représenter les statistiques des personnages par des attributs simple. Par exemple, les points de vie ou l'attaque sont représentés par des variables de types 'integers'. Le nom des personnage lui aussi est stocké de manière simple dans une variable de type 'string'.

Pour les attaques, il a néanmoins été choisi d'utiliser un dictionnaire suivant à chaque fois la structure suivante:
```py
{'Nom de la première attaque': (valeur_dégats, valeur_précision)}
```
Avec la valeur de dégats un pourcentage de la statistique d'attaque du personnage (cette dernière étant calculée selon le niveau lors d'une attaque) et la valeur de précision un pourcentage de précision (100 équivaut à 100% de réussite)

### Méthodes

Chaque personnage possède 3 méthodes:
- Une première qui permet de calculer une statistique selon le niveau du personnage en suivant un modèle exponentiel
- Une seconde permettant de calculer les dégat du personnage sur un autre
- Une dernière permettant de savoir si le personnage est décédé

Le joueur possède une méthode en plus: lvlup
Elle est appelé quand le joueur monte de niveau.

(Pour plus d'info voir les [docs](https://mrgg570.github.io/RPG/)

## Zones

### Attributs 

Les zones possède quelques attributs simples. Un nom, un type, une fourchette de niveau, une liste de monstre.
Elles possède aussi un attribut contenant une boutique

## Affichage

### Attributs 

La classe Display possède surtout des fonction comme attributs.
Toutefois elle possède un attribut 'console' qui est un objet 'Console' du module 'rich.console' qui permet d'effectuer des affichages formatés

### Méthodes

La classe possèdes une méthode print qui se base sur la console du module rich, une méthode menu permettant de créer des menus, et d'autres méthodes (començant par get) qui permmettent de construire des chaines de caractères

## Boutique et inventaire

### Attributs

La boutique possède quelques attributs simples (réduction, liste des objets disponibles), ainsi qu'un dictionnaire contenant tout les objets du jeu.

L'inventaire possède un attribut (dictionnaire) contenant les objets du joueur, et un autre attribut avec le nombre de potions que le joueur a en sa possession.

### Méthodes

Les méthodes de la boutiques sont assez simple. La réduction est calculé par la méthode Direbonjour, et les méthodes afficher_inventaire et acheter_objet permettent respectivement d'avoir la liste d'objet disponible et d'acheter un objet.

Pour l'inventaire, ajouterobj et enleverobj permettent d'ajouter et d'enlever des objets de l'inventaire du joueur, la méthode afficherobjs renvoie l'inventaire du joueur et finalement estvide retourne vrai si l'inventaire ne contient aucun objet.

# Répartition

## Matys

Matys a réalisé le code contenu dans les fichier suivants:
- `matys.py`
- `nether.py`
- `phenix.py`
- `dragonneau.py`
- `sorciere.py`
- `esprit.py`
- `boss.py` (celui dans le dossier `characters`)

## Quentin

Quentin a réalisé le code contenu dans les fichiers suivants:
- `quentin.py`

## Bastien

Bastien a réalisé tout le reste du code, ainsi que l'implémentation et la mise en relation des codes de chacun dans le projet final.

Il a aussi réalisé l'entièreté du compte-rendu et de la [documentation](https://mrgg570.github.io/RPG/), ainsi que la compilation en .exe du jeu.

# Comment jouer

## Télécharger le code

Vous pouvez le télécharger en cliquant [ici](https://github.com/MrGg570/RPG/archive/refs/heads/Bastien.zip)

## Extraire le zip

## Installer les dépendances

Se mettre dans le répertoire où se trouve `main.py` et `requirement.txt` et executer la commande suivante:
```ssh
python -m pip install -r requirements.txt
```

## Lancer le jeu

Il ne vous reste maintenant plus qu'à lancer le jeu!
```ssh
python -m pip install -r requirements.txt
```

***Note: pour une meilleur expérience, veuillez utiliser le nouveau terminal windows (pas l'invite de commande) ou le terminal intégré de Visual Studio Code***

### ⚠️ Si vous avez le moindre problème, une version compilé est comprise dans les fichier (`RPG\build\RPG.exe`)
