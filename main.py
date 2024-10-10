# Le code principal sera ici

from os import system
from Game.Builder import Build

player = Build.build('player', 100,10)

enemy = Build.build('enemy', 100,5)

clear = lambda: system('cls||clear')

while True:
    clear()
    assert player.pv > 0, "Joueur mort!"
    print(f"Enemy : {enemy.pv}/{enemy.maxpv}\nPlayer : {player.pv}/{player.maxpv}")
    print("0 - Attaquer\n1 - Ne rien faire")
    action = input(">>> ")
    clear()
    match action:
        case "0":
            print(f"Enemy : {enemy.pv}/{enemy.maxpv}\nPlayer : {player.pv}/{player.maxpv}")
            print("Vous attaquez enemy")
            player.attaquer(enemy)
            input()
        case "1":
            print(f"Enemy : {enemy.pv}/{enemy.maxpv}\nPlayer : {player.pv}/{player.maxpv}")
            print(f"Vous ne faites rien...")
            input()
        case _:
            print(f"Enemy : {enemy.pv}/{enemy.maxpv}\nPlayer : {player.pv}/{player.maxpv}")
            print(f"Vous {action}!... Mais ça veut dire quoi?")
            input()
    assert enemy.pv > 0, "Enemy mort!"
    clear()
    print(f"Enemy : {enemy.pv}/{enemy.maxpv}\nPlayer : {player.pv}/{player.maxpv}")
    print("Enemy vous attaque!")
    enemy.attaquer(player)
    input()