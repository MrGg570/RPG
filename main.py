# Le code principal sera ici

from Game import Builder, Combat, Display, Storyteller

player = Builder.Build.build('player')

display = Display.Display()

story = Storyteller.Story(display)

combat = Combat.Combat(display)

def combattre(name: str, lvl: str, tutorial: bool = False) -> None:

    enemy = Builder.Build.build(name, lvl)

    combat.initialize(player, enemy)

    combat.start(tutorial)

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

story.introduction()

combattre(story.getmob(), 2, tutorial=True)