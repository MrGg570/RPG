# Le code principal sera ici

from rich.progress import Progress

from Game.Console import console
from Game.Builder import Build
from Game.Display import Display
    

player = Build.build('player', 100,10)

enemy = Build.build('enemy', 100,5)

display = Display(console)

display.initdisplay(player, enemy)

while True:
    assert player.pv > 0, "Joueur mort!"
    display.rfrsh()
    actions = ["Attaquer", "Ne rien faire"]
    action = display.menu(actions)
    match action:
        case 0:
            display.rfrsh(f"Vous attaquez {enemy.name}")
            display.waitinput()
            player.attaquer(enemy)
        case 1:
            display.rfrsh(f"Vous ne faites rien...")
            display.waitinput()

    assert enemy.pv > 0, "Enemy mort!"
    display.rfrsh(f"{enemy.name} vous attaque!")
    display.waitinput()
    enemy.attaquer(player)