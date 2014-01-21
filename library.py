import sys
import pickle

moves = ["up", "down", "n", "e", "w", "s"]
one_liners = ['hello', 'hi', 'quit', 'exit', 'help', 'restart']
dictionary = moves + one_liners
#I really like that the HP text adventure has a thesaurus. Also, the above lists don't do anything, other than give a list of legit commands
#in order to check the validity of user input.

class Player(object):
    def __init__(self):
        self.alive = True
        self.location = None
        self.inventory = []

    def inventory_check(self):
        if self.inventory == []: print "You're not holding anything!"
        else:
            print "You're holding:"
            for thing in self.inventory:
                print "\n%s" % (thing)

    def move(self, direction):
        self.location = self.location.directions[direction] #not sure if this is going to work
        self.location.describe()


class Item(object):
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location

    def examine(self):
        print self.description

    def take(self):
        player.inventory.append(self.name)
        self.location = 'player'
        player.location.inventory.remove(self.name)
        print "You take the %s." % (self.name)

    def drop(self):
        player.inventory.remove(self.name)
        self.location = player.location
        player.location.inventory.append(self.name)
        print "You drop the %s." % (self.name)


class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.directions = {}
        self.inventory = []

    def add_directions(self, directions):
        self.directions = directions

    def describe(self):
        print self.name
        print
        print self.description
        if len(self.inventory) == 1:
            print "\nThere's a %s here." % (self.inventory[0])
        elif len(self.inventory) > 1:
            print "\nThere are a %s and %s here." % (self.inventory[0], self.inventory[1]) #how to make this flexible for more than two items in the room?


class GameEngine(object):
    def input_format(self):
        user_input = raw_input(">").lower().split(" ")

        if "." in user_input[-1]:
            detail = user_input.pop().split(".").pop(0)
            user_input.append(detail)

        if len(user_input) > 2:
            print 'I do better with just one or two words. Type "help" for some commands you can use.'
            self.play()

        return user_input

    def invalid_input(self):
        print "I'm sorry, I don't understand that command."
        self.play()

    def start(self):
        if player.location == None:
            player.location = entrance
        for item in items:
            if items[item].location == 'player':
                player.inventory.append(item)
            elif items[item].location in rooms: #not sure if this will work, for the same reason that player wouldn't work above (had to switch it to string)
                items[item].location.inventory.append(item)

        player.location.describe()
        self.play()

    def save(self):
        #Currently saves/loads player's location and sets correct item locations.
        #Doesn't save other player/room status info (alive/dead, opened doors, etc).
        print "Save file name:"
        save_name = self.input_format()[0] + '.txt'
        #can i ask about overwriting a previous save file?
        with open(save_name, 'wb') as save_file:
            pickle.dump(player.location, save_file)
            pickle.dump(items, save_file)
        #recommended by Dive Into Python 3 (excellent explanation of serialization and how to use pickle).
        #with open() ensures that the file is closed. Pickle only reads/writes binary, so 'wb' is needed.
        #how to ensure items are where they're supposed to be? what if someone picks up an item in one room and drops it in another?
        print "File saved."

    def load(self):
        print "What's the file name?"
        save_name = self.input_format()[0] + '.txt'
        #how to search for file, so it doesn't try to open a non-existant file.
        with open(save_name, 'rb') as save_file:
            player.location = pickle.load(save_file)
            items = pickle.load(save_file)
        self.start()

    def command(self, user_input):
        if len(user_input) == 1:
            #Easter Eggs
            if 'hello' in user_input or 'hi' in user_input: print "Hullo!"
            #Commands
            elif 'help' in user_input:
                print '''My commands are like a traditional text adventure\'s. To move, use the cardinal directions ("n", "s", "e", or "w")
or "up" and "down". Other commands you can use: "look" (describes the room to you), "examine [object]", "take [object]",
"drop [object]", "exit" or "quit" (exits the game), or "restart" (restarts the game).'''
            elif 'exit' in user_input or 'quit' in user_input: sys.exit()
            elif 'restart' in user_input:
                print "Are you sure you want to restart? Y/N"
                user_input = self.input_format()
                if "y" in user_input or "yes" in user_input:
                    global game, player
                    game = GameEngine()
                    player = Player()
                    player.location = entrance
                    player.location.describe()
                    game.play()
                elif "n" in user_input or "no" in user_input: self.play()
                else: self.invalid_input()
            elif 'look' in user_input: player.location.describe()
            elif 'inventory' in user_input or 'i' in user_input: player.inventory_check()
            elif 'save' in user_input: self.save()
            elif 'load' in user_input: self.load()
            elif user_input[0] in moves:
                #is there a better way to do this/standardize it with the rest of the commands?
                try: player.move(user_input[0])
                except: raise KeyError("You can't go that way!")
            else: self.invalid_input()
        else:
            verb = user_input[0]
            noun = user_input[1]
            if verb == 'examine':
                try: items[noun].examine()
                except: print "I'm sorry, I don't see that item."
            elif verb == 'take':
                try: items[noun].take()
                except: print "I don't see that item."
            elif verb == 'drop':
                try: items[noun].drop()
                except: print "You're not carrying that!"
            else: self.invalid_input()

    def play(self):
        while True:
            self.command(self.input_format())

game = GameEngine()

#Rooms Inits
entrance = Room("Library Entrance", '''You're standing in the library entrance. The doors are to the west, but they're locked.
There is a tall arched doorway to the east, and a small, plain wooden door to the south.''')
librarian_alcove = Room("Librarian Alcove", '''This is the librarian alcove, the main hub of their behind-the-scenes
library management. The only exit is to the north. There is a small roller-top desk in the corner.''')
#possibly open the desk?
next_room = Room("Test Room", "This is the last room in the test library.")

#Room Directions
entrance.add_directions({'e': next_room, 's': librarian_alcove})
librarian_alcove.add_directions({'n': entrance})
next_room.add_directions({'w': entrance})

#Items
ledger = Item('ledger', '''It's a small, hand-bound leather ledger. You flip through it. Inside are all books borrowed
from the library in the past five years.''', librarian_alcove)
#Changed so items now have a location instead of being in a room's inventory. This should make saving easier, but makes
#complications in noting that an object is in a room.

pan_pipes = Item('pipes', '''It's a set of pan pipes. There are seven total. They're plain wood,
bound together with leather, and inscribed with Charter marks.''', None)
bells = Item('bells', '''A set of seven bells hang on a bandolier, meant to be worn across the chest. Their leather pouches are
etched with Charter marks and the bells' mahogany handles stick out of the top of the pouches.''', None)

#Player init
player = Player()
items = {'ledger': ledger, 'pipes': pan_pipes, 'bells': bells} #is there a way I can 'predefine' these items so I can put them up with the other lists?
rooms = [entrance, librarian_alcove, next_room]

game.start()

#To do:
#Standardize the command list somehow? The giant if statement seems sloppy.
#Taking an item puts it in your inventory and removes it from the room, but doesn't change the room description.
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)
#Sloppy code, incl. initializations at the bottom and the multiple lists and items dict.
#Needs save/load functions.
#Bells (item) need to be a recursive so you can call each bell by name.
#Automate descriptions based on paths (ie, like the items are only described in the rooms they're in, if there's a path
#in a specific direction, automatically describe that path).

#Bug: couldn't do class Player(object, location) to automatically init the location correctly.
#Bug: bottom code is super sloppy. It was in GameEngine's init, but it complained about variables being defined (global/local issues).
#Bug: since the rooms all call each other, they give errors when other rooms haven't been initialized.
#       Is there a way to initialize without a value, non-descructively?
#       HP solved this by NOT initializing with the paths, but adding them second.
#SOLVED Bug: save isn't working. Having the same issue that I was earlier with the item dictionary, where it records an object's
#       location but not its data. (Calling by name gives location, not data.)
#New Bug: save isn't working. Remembers player's location but not their inventory, and doesn't do anything about items that have been taken/
#moved from their original location.
