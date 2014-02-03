import sys
import pickle
import rooms
# import items

moves = {'u': 'u', 'up': 'u', 'd': 'd', 'down': 'd', 'n': 'n', 'north': 'n', 'e': 'e', 'east': 'e',
'w': 'w', 'west': 'w', 's': 's', 'south': 's', 'northwest': 'nw', 'nw': 'nw', 'southwest': 'sw',
'sw': 'sw', 'southeast': 'se', 'se': 'se', 'northeast': 'ne', 'ne': 'ne'}
#need direction synonyms and "pick up."
spells = {}
#not used for anything yet. need to be able to respond to commands and use different forms for different things. things other than small spaces?
#I really like that the HP text adventure has a thesaurus. How do I make one?
item_list = {}
# book_list = {}

class Player(object):
    def __init__(self):
        self.alive = True
        self.location = None
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
        if self.location in rooms.labyrinths:
            self.location = rooms.labyrinth1
            self.location.describe()
        else:
            self.location = rooms.reading_room
            self.location.describe()


class Item(object):
    def __init__(self, name, description, location=None):
        self.name = name
        self.description = description
        self.location = location
        item_list[name] = self

    def examine(self):
        if self.location == player.location or self.location == 'player':
            print self.description
        else: print "I'm sorry, I don't see that item."

    def take(self):
        try:
            player.inventory.append(self.name)
            self.location = 'player'
            player.location.inventory.remove(self.name)
            print "You take the %s." % (self.name)
        except: print "I don't see that item."

    def drop(self):
        try:
            player.inventory.remove(self.name)
            self.location = player.location
            player.location.inventory.append(self.name)
            print "You drop the %s." % (self.name)
        except: print "You're not carrying that!"


class Book(Item):
    def __init__(self, inside, spell=None, *args):
        self.inside = inside
        self.spell = spell
        # book_list[name] = self
        super(Book, self).__init__(*args)

    def open(self):
        if self.location == 'player':
            print self.inside
            if self.spell != None: player.known_spells.append(self.spell)
        else: print "You have to pick it up first!"


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
    def input_format(self):
        user_input = raw_input(">").lower().split(" ")

        if "." in user_input[-1]:
            detail = user_input.pop().split(".").pop(0)
            user_input.append(detail)

        return user_input

    def start(self):
        if player.location == None:
            player.location = rooms.reading_room
        for item in item_list:
            if item_list[item].location == 'player':
                player.inventory.append(item)
            elif item_list[item].location in rooms.directory:
                item_list[item].location.inventory.append(item)

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
            pickle.dump(item_list, save_file)
        #recommended by Dive Into Python 3 (excellent explanation of serialization and how to use pickle).
        #with open() ensures that the file is closed. Pickle only reads/writes binary, so 'wb' is needed.
        print "File saved."

    def load(self):
        print "What's the file name?"
        save_name = self.input_format()[0] + '.txt'
        #how to search for file, so it doesn't try to open a non-existant file?
        with open(save_name, 'rb') as save_file:
            player.location = pickle.load(save_file)
            item_list = pickle.load(save_file)
        self.start()

    def help_command(self):
        print '''My commands are like a traditional text adventure\'s. To move, use the cardinal directions ("n", "s", "e", or "w")
or "up" and "down". Other commands you can use: "look" (describes the room to you), "examine [object]", "inventory"
or "i" (lists your inventory), "take [object]", "drop [object]", "cast [Charter spell]", "spells" (lists the
spells you know), "teleport" (sends you back to the Reading Room, or the labyrinth stairs if you're in the labyrinth),
"exit" or "quit" (exits the game), or "restart" (restarts the game).'''

    def restart(self):
        print "Are you sure you want to restart? Y/N"
        user_input = self.input_format()
        if "y" or "yes":
            global game, player
            game = GameEngine()
            player = Player()
            self.start()
        elif "n" or "no": self.play()
        else: self.invalid_input()

    def command(self, user_input):
        verb = user_input[0]
        if len(user_input) == 2: noun = user_input[1]
        elif len(user_input) > 2: print "Whoops! That's too challenging for me. Please try again."

        #Helper functions so I can add all methods to the verbs dictionary:
        def examine():
            item_list[noun].examine()

        def take():
            if noun == 'all':
                if player.location.inventory:
                    temp = player.location.inventory[:]
                    for item in temp:
                        item_list[item].take()
                else: print "There's nothing here to take."
            else:
                item_list[noun].take()

        def drop():
            if noun == 'all':
                if player.inventory:
                    temp = player.inventory[:]
                    for item in temp:
                        item_list[item].drop()
                else: player.inventory_check()
            else:
                item_list[noun].drop()

        def open():
            try: item_list[noun].open()
            except: print "You can't read that. Try reading a book."

        def cast():
            spells[noun].use_spell()

        verbs = {'help': self.help_command, 'exit': sys.exit, 'quit': sys.exit, 'restart': self.restart,
        'look': player.location.describe, 'inventory': player.inventory_check, 'i': player.inventory_check,
        'save': self.save, 'load': self.load, 'spells': player.spell_check, 'teleport': player.teleport,
        'examine': self.examine, 'take': self.take, 'drop': self.drop, 'cast': self.cast}

        #the following verbs entries are within a try because they require noun to be defined.
        # try:
        #     verbs['examine'] = item_list[noun].examine
        #     verbs['take'] = item_list[noun].take
        #     verbs['drop'] = item_list[noun].drop
        # except: pass

        #can't *try* here because sys.exit() doesn't work within a try.
        if verb in verbs:
            verbs[verb]()
        else:
            if verb == 'hello' or verb == 'hi': print "Hullo!"
            elif verb in moves: player.move(moves[verb])
            else: print 'I\'m sorry, I don\'t understand that command. Try typing "help" if you need some guidance.'

    def play(self):
        while True:
            self.command(self.input_format())

game = GameEngine()

#Player init
player = Player()

#Items
pan_pipes = Item('pipes', '''It's a set of pan pipes. There are seven total. They're plain wood,
bound together with leather, and inscribed with Charter marks.''')
bells = Item('bells', '''A set of seven bells hang on a bandolier, meant to be worn across the chest. Their leather pouches are
etched with Charter marks and the bells' mahogany handles stick out of the top of the pouches.''')
mouse = Item('mouse', '''It's a small clockwork mouse, about the size of your fist. There's a turnkey sticking out of the back.
Interestingly, it also buzzes in your hand, like it's connected to the Charter somehow.''', rooms.third_assistant_study)
key = Item('key', '''It's a silver bracelet, set with seven emeralds. One is glowing.''', rooms.third_assistant_study)
waistcoat = Item('waistcoat', '''A yellow waistcoat. It flatters you quite nicely. And so professional!
There's a whistle clipped to the lapel.''', rooms.third_assistant_study)
dagger = Item('dagger', '''A silver dagger in a leather scabbard, attached to a belt. The blade looks quite sharp
and there are Charter marks etched on the hilt.''', rooms.third_assistant_study)

#Books (Subclass of Items)
ledger = Book('''As you expected, the book is full of lists of equipment checked out to past librarians. And there's your name,
at the very bottom! There's a list of equipment for you, including a dagger, a clockwork mouse, a key, and
a yellow waistcoat. Now, I wonder where those things could be. (You didn't lose them already, did you?)''', None, 'ledger',
'''It's a large leather ledger. It's incredibly heavy, and when you open it you feel as though it
contains every piece of equipment checked out by every librarian in the history of the Clayr. It's that big. You probably don't want
to carry it around.''', rooms.librarian_alcove)
spell_book = Book('''It's full of spells! There's one that looks right at your level. You read it, and suddenly feel like you've been totally
immersed in the Charter. ''', 'otter', 'book', 'It\'s a plain brown book, small enough to fit in the palm of your hand.')
#Have to define ledger's spell as none in order for it to not get confused re where the super variables start.

#Spells
otter = Spell('otter', 'small')
human = Spell('human')

game.start()

#To do:
#Standardize the command list somehow? The giant if statement seems sloppy. >> verb/noun dictionaries.
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)
#Sloppy code, incl. initializations at the bottom and the multiple lists and items dict.
#Bells (item) need to be a recursive so you can call each bell by name.
#Automate descriptions based on paths (ie, like the items are only described in the rooms they're in, if there's a path
#in a specific direction, automatically describe that path).
#Make room states that can change over time (locked doors, etc). Also need to prevent going through the hole at the bottom of the tunnel.
#   Could also use this to create different room descriptions if you get promoted and get a new study, etc.
#NPCs.
#"Alignment" changes due to choices made in dialogue, etc.
#Need to note somewhere that you can use 'human' to change back.
#Add remaining commands to verbs dict.
#Fix labyrinth (secondary cardinal directions and label towers.)

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
#Bug: two-word commands throw a fatal error if used without a "noun">
