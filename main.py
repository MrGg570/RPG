# Le code principal sera ici

from rich.progress import Progress

from Game.Console import console
from Game.Builder import Build
from Game.Display import Display
    

player = Build.build('player', 100,10)

enemy = Build.build('enemy', 100,5)

display = Display(console)


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



options = ["Option 1", "Option 2", "Option 3"]
display.initdisplay(player, enemy)
choice = display.menu(options)
print(choice)
input()