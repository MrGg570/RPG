# Le code principal sera ici

from Game import Builder, Combat, Display

    

player = Builder.Build.build('player', 30,10)

enemy = Builder.Build.build('goblin', 20,5)

display = Display.Display()

combat = Combat.Combat(display)

combat.initialize(player, enemy)

combat.start()

enemy = Builder.Build.build('goblin', 20,5)

combat.initialize(player, enemy)

combat.start()