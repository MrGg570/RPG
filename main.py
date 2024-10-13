# Le code principal sera ici

from Game import Builder, Combat, Display, Storyteller
from time import sleep

player = Builder.Build.build('player')

display = Display.Display()

combat = Combat.Combat(display)

def combattre(name: str, lvl: str, tutorial: bool = False) -> None | bool:

    if tutorial:
        enemy = Builder.Build.build(name, lvl)

        combat.initialize(player, enemy)

        combat.tuto()

    else:
        enemy = Builder.Build.build(name, lvl)

        combat.initialize(player, enemy)

        return combat.start()

mainmenu = True
while mainmenu:
    choice = display.mainMenu()
    match choice:
        case 0:
            mainmenu = False
        case 1:
            pass
        case 2:
            exit(1)

story = Storyteller.Story(display)

# story.introduction()

# combattre(story.getmob(), 3, True)

menu = False
while not menu:
    action = story.outofcombat(['combat', 'sac', 'shop', 'eglise'])
    match action:

        case 'combat':
            enemies = story.numberofenemies()
            story.tell(f"Vous vous retrouvez face à {enemies} enemies! \u25BA")
            display.waitinput()
            playeralive = True
            i = 1
            while playeralive and i<= enemies:
                mob = story.getmob()
                story.tell(f"Enemi n°{i}: {story.mobdico[mob]} \u25BA")
                display.waitinput()
                playeralive = combattre(mob, story.getlevel(player))
                i += 1
            if not playeralive:
                pass
            else:
                pass

        case 'sac':
            pass

        case 'shop':
            pass

        case 'eglise':
            story.eglise(player)
