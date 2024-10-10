# Le code principal sera ici

from os import system
from rich.progress import Progress

from Game.Console import console
from Game.Builder import Build
    

player = Build.build('player', 100,10)

enemy = Build.build('enemy', 100,5)

clear = lambda: system('cls||clear')

# def display():
#     console.print(player.pvbar()+'\n')
#     console.print(enemy.pvbar()+'\n')

# while True:
#     clear()
#     assert player.pv > 0, "Joueur mort!"
#     display()
#     print("0 - Attaquer\n1 - Ne rien faire")
#     action = input(">>> ")
#     clear()
#     match action:
#         case "0":
#             display()
#             print(f"Vous attaquez {enemy.name}")
#             player.attaquer(enemy)
#             input()
#         case "1":
#             display()
#             print(f"Vous ne faites rien...")
#             input()
#         case _:
#             display()
#             print(f"Vous {action}!... Mais ça veut dire quoi?")
#             input()
#     assert enemy.pv > 0, "Enemy mort!"
#     clear()
#     display()
#     print(f"{enemy.name} vous attaque!")
#     enemy.attaquer(player)
#     input()

def rfrsh(menu):
    pass