from player import player
import rooms

spells = {}
#not used for anything yet. need to be able to respond to commands and use
#different forms for different things. things other than small spaces?

class Spell(object):
    def __init__(self, name, size='medium', flying=False):
        self.name = name
        self.size = size
        self.flying = flying
        spells[name] = self

    def use_spell(self):
        small_spaces = []

        if self.name in player.known_spells:
            if self.name == 'water':
                print '''You spray water everywhere. In a library. You're clearly very
bright and good at your job.'''
                if player.location == rooms.alexandria1:
                    print "You spray the fires, and they go out. The walls are now gently smoking."
                    rooms.alexandria1.add_counter()
            elif player.shape != self.name:
                player.shape = self.name
                player.size = self.size
                player.flying = self.flying
                #For spells that start with a vowel:
                if self.name == 'otter' or self.name == 'owl':
                    print "You're an %s!" % self.name
                elif self.name == 'human':
                    print "You're human again."
                else:
                    print "You're a %s!" % self.name

                if player.size == 'small':
                    print "You've shrunk substantially. Now you can climb through small spaces."
                    for room in small_spaces:
                        rooms.room.unlock()
                elif player.size == 'large':
                    print "You're huge! Nothing's going to mess with you."
                if player.flying == True:
                    print "You can fly!"

            else: print "You're already in that shape."
        else: print "You don't know that spell, sorry."

otter = Spell('otter', 'small')
human = Spell('human')
water = Spell('water')