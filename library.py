import time

import rooms
import items
import commands
import people

spells = {}
#not used for anything yet. need to be able to respond to commands and use
#different forms for different things. things other than small spaces?
#I really like that the HP text adventure has a thesaurus. How do I make one?

home = rooms.reading_room

class Player(object):
    def __init__(self, location=home):
        self.alive = True
        self.location = location
        self.shape = 'human'
        self.size = 'medium'
        self.flying = False
        self.known_spells = ['human']
        self.inventory = []
        self.shelved_books = set()
        self.level = 1

    def inventory_check(self):
        if self.inventory == []: print "You're not holding anything!"
        else:
            print "You're holding:"
            print
            for thing in self.inventory:
                print "%s" % (thing)

    def spell_check(self):
        if self.known_spells == ['human']: print "You don't know any spells."
        else:
            print "You know these spells:"
            for spell in self.known_spells:
                if spell != 'human':
                    print "\n%s" % (spell)

    def move(self, direction):
        if direction == 'e' and self.location == rooms.reading_room:
            print "No, I really don't think you want to go that way. Why don't you stick to the library?"
        elif direction == 'd' and (self.location == rooms.uu_library1 or
            self.location == rooms.uu_library2):
            print '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
and down is up. But now it's gone, so you don't trouble yourself over it.'''
            print
            self.location = self.location.directions[direction]
            time.sleep(3)
            self.location.describe()
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


class GameEngine(object):
    def start(self):
        # player = Player()

        for npc in people.npc_list:
            people.npc_list[npc].location.npc = npc
        for item in items.item_list:
            if items.item_list[item].location == 'player':
                player.inventory.append(item)
            elif items.item_list[item].location in rooms.directory:
                items.item_list[item].location.inventory.append(item)

        player.location.describe()
        self.play()

    def play(self):
        while True:
            commands.command(commands.input_format(), player, game)

game = GameEngine()
player = Player()

#Spells
otter = Spell('otter', 'small')
human = Spell('human')

game.start()

#To do:
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)
#Sloppy code, incl. initializations at the bottom.
#Bells (item) need to be a recursive so you can call each bell by name.
#Make room states that can change over time (locked doors, etc). Also need to prevent going through the hole at the bottom of the tunnel.
#   Could also use this to create different room descriptions if you get promoted and get a new study, etc.
#   Need a player state that will change as you re-shelve books. But won't actually change unless you go back and talk to Vancelle.
#Need to note somewhere that you can use 'human' to change back.
#Shelve command.
#Only describe the room the first time through? This would also cause issues with the way the save function is currently written.
#   (Would also have to divide the directions from the description.)
#Add in more Clayr hallway landmarks as I add other libraries.
#Sequester code. Stop calling class attributes directly; create new methods instead.
#Add Alexandria, expand WTNV, Dream's library, Restricted Section, Pagemaster, DW?, Powell's.
#Levels up, but doesn't change access. Also need to edit Vancelle's dialogue so that she indicates which books you need to shelve,
#   and perhaps a hint in the beginning that you need to get your key before you can level up.

#Bug: since the rooms all call each other, they give errors when other rooms haven't been initialized.
#       Is there a way to initialize without a value, non-descructively?
#       HP solved this by NOT initializing with the paths, but adding them second. (Current workaround.)
#SOLVED: save isn't working. Having the same issue that I was earlier with the item dictionary, where it records an object's
#       location but not its data. (Calling by name gives location, not data.)
#SOLVED: save isn't working. Remembers player's location but not their inventory, and doesn't do anything about items that have been taken/
#moved from their original location.
#SOLVED: #Taking an item puts it in your inventory and removes it from the room, but doesn't change the room description.
#SOLVED: moving not working since dividing into multiple files. The "self" part of the location is confusing it.
#SOLVED: 'take all' only takes the first two items. Trying 'take all' again then only takes the next one item (in a room with four items).
#(Due to iteration over a changing list. Created a temp list to solve this.)
#Solved?: two-word commands throw a fatal error if used without a "noun."
#Bug: glitches (can be delayed) after saving/loading and then trying to exit. ("I'm sorry, I don't understand that command...")
#Bug: save/load having a lot of issues.
#Solved: list spells doesn't work. Open ledger works, but then prints that you can't open that.
#Bug: when you talk to Vancelle after leveling up, it goes through all the level-up dialogue again (and it'll go through ALL of
#it everytime you level up.)
