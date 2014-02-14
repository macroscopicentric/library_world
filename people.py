import random
import rooms

npc_list = {}

class NPC(object):
    def __init__(self, name, location, dialogue=[]):
        self.name = name
        self.location = location
        self.dialogue = dialogue
        self.counter = 0
        npc_list[name] = self

    def new_dialogue(self, new_dialogue):
        self.dialogue = new_dialogue

    def talk(self, location):
        if self.location == location:
            try: print self.dialogue[random.randint(0, len(self.dialogue) - 1)]
            except: print "%s doesn't say anything." % (self.name.capitalize())
        else: print "You don't see that person here."


uu_librarian = NPC('orangutan', rooms.uu_library1, ['Ooook ook.', 'Eeek eek!',
    'Ook eek. >:('])
vancelle = NPC('vancelle', rooms.chiefs_office)
imshi = NPC('imshi', rooms.middle_librarian_hallway, ['Hi!'])
clippy = NPC('clippy', rooms.binding_room,
    ['''It looks like you're trying to become a first-assistant librarian!... I'm sorry, I can't help with that. ''',
'''I'm sorry, I've been ordered to ignore all attempts to hide my super useful awesome tips.''',
'''Why would you want to disable me? I'm so helpful. :( :( :(''',
'''YES HELPFUL I AM HELPING SO HELPFUL.'''])