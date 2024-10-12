# Le code principal sera ici

from Game import Builder, Combat, Display, Storyteller

    

player = Builder.Build.build('player')

display = Display.Display()

story = Storyteller.Story(display)

combat = Combat.Combat(display)

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

# while player.isalive():

#     enemy = Builder.Build.build('goblin', 3)

#     combat.initialize(player, enemy)

#     combat.start()