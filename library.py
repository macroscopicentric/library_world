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
        print "You take %s." % (item.name)
        self.inventory += item


class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def examine(self):
        print self.description


class Room(object):
    def __init__(self, name, description, directions, inventory):
        self.name = name
        self.description = description
        self.directions = directions
        self.inventory = inventory

    def describe(self):
        print self.name
        print
        print self.description

    def take(self, item):
        self.inventory -= item

class GameEngine(object):
    def input_format(self):
        user_input = raw_input(">").lower().split(" ")

        if "." in user_input[-1]:
            detail = user_input.pop().split(".").pop(0)
            user_input.append(detail)

        if len(user_input) > 2:
            print 'I do better with just one or two words. Type "help" for some commands you can use.'
            game.play()

        return user_input

    def invalid_input(self):
        print "I'm sorry, I don't understand that command."
        game.play()

    def command(self, user_input):
        global game
        #For restarting.

        if len(user_input) == 1:
            #Easter Eggs
            if 'hello' in user_input or 'hi' in user_input: print "Hullo!"
            #Commands
            elif 'help' in user_input:
                print '''
My commands are like a traditional text adventure\'s. To move, use the cardinal directions ("n", "s", "e", or "w")
or "up" and "down". Other commands you can use: "look" (describes the room to you), "examine [object]", "exit" or
"quit" (exits the game), or "restart" (restarts the game).'''
            elif 'exit' in user_input or 'quit' in user_input: sys.exit()
            elif 'restart' in user_input:
                print "Are you sure you want to restart? Y/N"
                user_input = game.input_format()
                if "y" in user_input or "yes" in user_input:
                    game = GameEngine()
                    game.play()
                elif "n" in user_input or "no" in user_input: game.play()
                else: game.invalid_input()
            elif 'look' in user_input: player.location.describe()
            elif 'inventory' in user_input or 'i' in user_input: player.inventory()
            elif user_input[0] in moves:
                #is there a better way to do this/standardize it with the rest of the commands?
                if user_input[0] in player.location.directions:
                    player.move()
                else:
                    print "You can't go that way!"
            else: game.invalid_input()
        else:
            if user_input[0] == 'examine':
                if user_input[1] in player.inventory or user_input[1] in player.location.inventory:
                    items[user_input[1]].examine()
                else: print "I'm sorry, I don't see that item."
            elif user_input[0] == 'take':
                if user_input[1] in player.location.inventory:
                    player.take(items[user_input[1]])
                    player.location.take(items[user_input[1]])
                else: print "I don't see that item."
            else: game.invalid_input()

    def play(self):
        while True:
            game.command(game.input_format())

game = GameEngine()
mona_lisa = Item("Mona Lisa copy", "It's a copy of the Mona Lisa. It's a pretty decent copy, except for the clown hat on her head.")
pizza = Item("pizza", "It's a pepperoni pizza. It used to be whole, but entropy has done its job and only half remains.")
test_room = Room("Test Room", "This is a test room.\n\nThere is half of a pizza and a copy of the Mona Lisa lying on the ground.", {}, [pizza, mona_lisa])
player = Player()
player.location = test_room
player.location.describe()
items = {'pizza': pizza, 'Mona Lisa': mona_lisa} #is there a way I can 'predefine' these items so I can put them up with the other lists?
game.play()

#To do:
#Generic "I'm sorry, I don't know what you mean" error method. Need an allowed list of commands.
#Standardize the command list somehow? The giant if statement seems sloppy.
#Taking an item puts it in your inventory and removes it from the room, but doesn't change the room description.

#Bug: couldn't do class Player(object, location) to automatically init the location correctly.
#Bug: bottom code is super sloppy. It was in GameEngine's init, but it complained about variables being defined (global/local issues).
#Bug: can't take things.
