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

class Librarian(NPC):
    def __init__(self, *args):
        super(Librarian, self).__init__(*args)

    def level_up(self):
        self.counter += 1

uu_librarian = NPC('orangutan', rooms.reading_room, ['Ooook ook.', 'Eeek eek!', 'Ook eek. >:('])
vancelle = Librarian('vancelle', rooms.chiefs_office)
imshi = NPC('imshi', rooms.middle_librarian_hallway, ['Hi!'])