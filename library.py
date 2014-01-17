import sys

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
        print "You're holding:"
        for thing in self.inventory:
            print "\n%s" % (thing.name)

    def move(self, direction):
        self.location = self.location.directions[direction] #not sure if this is going to work
        self.location.describe()

    def take(self, item):
        print "You take the %s." % (item.name)
        self.inventory += item.name

    def drop(self, item):
        print "You drop the %s." % (item.name)
        self.inventory -= item.name


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def examine(self):
        print self.description


class Room(object):
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.directions = {}
        self.inventory = inventory

    def add_directions(self, directions):
        self.directions = directions

    def describe(self):
        print self.name
        print
        print self.description

    def take(self, item):
        self.inventory -= item.name

    def drop(self, item):
        self.inventory += item.name

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
            elif 'inventory' in user_input or 'i' in user_input: player.inventory()
            elif user_input[0] in moves:
                #is there a better way to do this/standardize it with the rest of the commands?
                if user_input[0] in player.location.directions:
                    player.move(user_input[0])
                else:
                    print "You can't go that way!"
            else: self.invalid_input()
        else:
            if user_input[0] == 'examine':
                if user_input[1] in player.inventory or user_input[1] in player.location.inventory:
                    items[user_input[1]].examine()
                else: print "I'm sorry, I don't see that item."
            elif user_input[0] == 'take':
                if user_input[1] in player.location.inventory:
                    player.take(user_input[1])
                    player.location.take(user_input[1])
                else: print "I don't see that item."
            elif user_input[0] == 'drop':
                if user_input[1] in player.inventory:
                    player.drop(items[user_input[1]])
                    player.location.drop(items[user_input[1]])
                else: print "You're not carrying that!"
            else: self.invalid_input()

    def play(self):
        while True:
            self.command(self.input_format())

game = GameEngine()

#Items
ledger = Item('ledger', '''It\'s a small, hand-bound leather ledger. You flip through it. Inside are all books borrowed
from the library in the past five years.''')

#Rooms Inits
entrance = Room("Library Entrance", '''You're standing in the library entrance. The doors are to the west, but they're locked.
There is a tall arched doorway to the east, and a small, plain wooden door to the south.''', [])
#next_room is a placeholder
#can I set up the methods to ignore the fields (ie inventory) that don't apply, so I don't have to type "[]" every time?
librarian_alcove = Room("Librarian Alcove", '''This is the librarian alcove, the main hub of their behind-the-scenes library management.
There is a small roller-top desk in the corner, with a ledger on top. The only exit is to the north.''', [ledger])
next_room = Room("Test Room", "This is the last room in the test library.", [])
#need to add ledger, and possibly open the desk?

#Room Directions
entrance.add_directions({'e': next_room, 's': librarian_alcove})
librarian_alcove.add_directions({'n': entrance})
next_room.add_directions({'w': entrance})

#Player init
player = Player()
player.location = entrance
player.location.describe()
items = {'ledger': ledger} #is there a way I can 'predefine' these items so I can put them up with the other lists?
game.play()

#To do:
#Generic "I'm sorry, I don't know what you mean" error method. Need an allowed list of commands.
#Standardize the command list somehow? The giant if statement seems sloppy.
#Taking an item puts it in your inventory and removes it from the room, but doesn't change the room description.
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)

#Bug: couldn't do class Player(object, location) to automatically init the location correctly.
#Bug: bottom code is super sloppy. It was in GameEngine's init, but it complained about variables being defined (global/local issues).
#Bug: can't take things. Perhaps because my dictionary includes objects? (Readout is funky when you try to print a value.)
#Bug: since the rooms all call each other, they give errors when other rooms haven't been initialized.
#       Is there a way to initialize without a value, non-descructively?
# HP solved this by NOT initializing with the paths, but adding them second.
