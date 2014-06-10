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
                if player.location == rooms.alexandria1:
                    rooms.alexandria1.add_counter()
                    return "You spray the fires, and they go out. The walls are now gently smoking."
                else:
                    return '''You spray water everywhere. In a library. You're clearly very
bright and good at your job.'''

            elif player.shape != self.name:
                player.shape = self.name
                player.size = self.size
                player.flying = self.flying
                #For spells that start with a vowel:
                if self.name == 'otter' or self.name == 'owl':
                    return "You're an %s!" % self.name
                elif self.name == 'human':
                    return "You're human again."
                else:
                    return "You're a %s!" % self.name

                if player.size == 'small':
                    for room in small_spaces:
                        rooms.room.unlock()
                    return "You've shrunk substantially. Now you can climb through small spaces."
                elif player.size == 'large':
                    return "You're huge! Nothing's going to mess with you."
                if player.flying == True:
                    return "You can fly!"

            else: return "You're already in that shape."
        else: return "You don't know that spell, sorry."

otter = Spell('otter', 'small')
human = Spell('human')
water = Spell('water')