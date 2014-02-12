import sys
import pickle
import random
import rooms

spells = {}
#not used for anything yet. need to be able to respond to commands and use
#different forms for different things. things other than small spaces?
#I really like that the HP text adventure has a thesaurus. How do I make one?
npc_list = {}
home = rooms.third_assistant_study

class Player(object):
    def __init__(self, location=home):
        self.alive = True
        self.location = location
        self.shape = 'human'
        self.size = 'medium'
        self.flying = False
        self.known_spells = ['human']
        self.inventory = []

    def inventory_check(self):
        if self.inventory == []: print "You're not holding anything!"
        else:
            print "You're holding:"
            print
            for thing in self.inventory:
                print "%s" % (thing)

    def spell_check(self):
        if self.inventory == ['human']: print "You don't know any spells."
        else:
            print "You know these spells:"
            for spell in self.known_spells:
                if spell != 'human':
                    print "\n%s" % (spell)

    def move(self, direction):
        if direction == 'e' and self.location == rooms.reading_room:
            print "No, I really don't think you want to go that way. Why don't you stick to the library?"
        elif direction not in self.location.directions:
            print "You can't go that way, stupid."
        elif direction in self.location.directions and self.location.directions[direction].locked == True:
            print "That door's locked. And it'll stay locked no matter how many times you tug on the handle, so stop trying."
        # elif direction in rooms.self.location.directions and...:
        #     print "That opening is too small for a full-sized person. Perhaps something smaller, like a cat or otter, could get through."
        #need a way to ID a DOOR (as opposed to a room, which I did for the locked rooms above),
        #since a door goes both ways and a key is one-time in one direction.
        elif direction in self.location.directions:
            self.location = self.location.directions[direction]
            self.location.describe()
        else:
            print "I didn't understand that direction, sorry."

    def teleport(self):
        if hasattr(self.location, 'labyrinth'):
            self.location = rooms.labyrinth1
            self.location.describe()
        else:
            self.location = home
            self.location.describe()


class Spell(object):
    def __init__(self, name, size='medium', flying=False):
        self.name = name
        self.size = size
        self.flying = flying
        spells[name] = self

    def use_spell(self):
        if self.name in player.known_spells:
            if player.shape != self.name:
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
                elif player.size == 'large':
                    print "You're huge! Nothing's going to mess with you."
                if player.flying == True:
                    print "You can fly!"

            else: print "You're already in that shape."
        else: print "You don't know that spell, sorry."


class NPC(object):
    def __init__(self, name, location, dialogue=[]):
        self.name = name
        self.location = location
        self.dialogue = dialogue
        npc_list[name] = self

    def new_dialogue(self, new_dialogue):
        self.dialogue = new_dialogue

    def talk(self):
        if self.location == player.location:
            try: print self.dialogue[random.randint(0, len(self.dialogue) - 1)]
            except: print "%s doesn't say anything." % (self.name.capitalize())
        else: print "You don't see that person here."


class GameEngine(object):
    def input_format(self):
        user_input = raw_input(">").lower().split(" ")

    def add_dialogue(self, dialogue):
        self.dialogue = dialogue

    def talk(self):
        try: print self.dialogue[random.randint(0, len(self.dialogue))]
        except: print "%s doesn't say anything." % (self.name.capitalize())

class GameEngine(object):
    def save():
        #Currently saves/loads player's location and sets correct item locations.
        #Doesn't save other player/room status info (alive/dead, opened doors, etc).
        print "Save file name:"
        save_name = verbs_list.input_format()[0] + '.txt'
        #can i ask about overwriting a previous save file?
        with open(save_name, 'wb') as save_file:
            pickle.dump(player.location, save_file)
            pickle.dump(items.item_list, save_file)
        #recommended by Dive Into Python 3 (excellent explanation of
        #serialization and how to use pickle).
        #with open() ensures that the file is closed. Pickle only reads/writes
        #binary, so 'wb' is needed.
        print "File saved."

    def load():
        print "What's the file name?"
        save_name = verbs_list.input_format()[0] + '.txt'
        #how to search for file, so it doesn't try to open a non-existent file?
        with open(save_name, 'rb') as save_file:
            player.location = pickle.load(save_file)
            items.item_list = pickle.load(save_file)
        self.start()

    def restart():
        print "Are you sure you want to restart? Y/N"
        user_input = verbs_list.input_format()
        if user_input == "y" or user_input == "yes":
            self.start()
        elif user_input == "n" or user_input == "no": self.play()
        else: print 'I\'m sorry, I don\'t understand that command.'

    def start(self):
        player = Player()

        for npc in npc_list:
            npc.location.npc = npc.name
        for item in item_list:
            if item_list[item].location == 'player':
                player.inventory.append(item)
            elif item_list[item].location in rooms.directory:
                item_list[item].location.inventory.append(item)

        player.location.describe()
        self.play()

    def play(self):
        import verbs_list
        while True:
            verbs_list.command(verbs_list.input_format())

game = GameEngine()

#Spells
otter = Spell('otter', 'small')
human = Spell('human')

#NPCs
uu_librarian = NPC('orangutan', rooms.reading_room, ['Ooook ook.', 'Eeek eek!', 'Ook eek. >:('])
vancelle = NPC('vancelle', rooms.chiefs_office)
imshi = NPC('imshi', rooms.middle_librarian_hallway)

game.start()

#To do:
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)
#Sloppy code, incl. initializations at the bottom.
#Bells (item) need to be a recursive so you can call each bell by name.
#Make room states that can change over time (locked doors, etc). Also need to prevent going through the hole at the bottom of the tunnel.
#   Could also use this to create different room descriptions if you get promoted and get a new study, etc.
#NPCs.
#Need to note somewhere that you can use 'human' to change back.
#Shelve command, how to distinguish books? "Which book would you like to x?" > Numbered list?
#Only describe the room the first time through? This would also cause issues with the way the save function is currently written.
#   (Would also have to divide the directions from the description.)

#Bug: couldn't do class Player(object, location) to automatically init the location correctly.
#Bug: bottom code is super sloppy. It was in GameEngine's init, but it complained about variables being defined (global/local issues).
#Bug: since the rooms all call each other, they give errors when other rooms haven't been initialized.
#       Is there a way to initialize without a value, non-descructively?
#       HP solved this by NOT initializing with the paths, but adding them second. (Current workaround.)
#SOLVED: save isn't working. Having the same issue that I was earlier with the item dictionary, where it records an object's
#       location but not its data. (Calling by name gives location, not data.)
#SOLVED: save isn't working. Remembers player's location but not their inventory, and doesn't do anything about items that have been taken/
#moved from their original location.
#SOLVED: #Taking an item puts it in your inventory and removes it from the room, but doesn't change the room description.
#Bug: moving not working since dividing into multiple files. The "self" part of the location is confusing it.
#SOLVED: 'take all' only takes the first two items. Trying 'take all' again then only takes the next one item (in a room with four items).
#(Due to iteration over a changing list. Created a temp list to solve this.)
#Bug: two-word commands throw a fatal error if used without a "noun."
