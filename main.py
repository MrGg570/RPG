# Le code principal sera ici

from Game import Builder, Combat, Display

    

player = Builder.Build.build('player')

display = Display.Display()

combat = Combat.Combat(display)

while player.isalive():

    enemy = Builder.Build.build('goblin', 3)

    combat.initialize(player, enemy)

    combat.start()