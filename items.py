import player
import rooms

item_list = {}

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        item_list[name] = self

    def examine(self, player_location):
        if (self.name in player.player.inventory or
            self.name in player.location.inventory):
            print self.description
        else: print "I'm sorry, I don't see that item."

    def take(self, player_inventory, location_inventory):
        try:
            player_inventory.append(self.name)
            location_inventory.remove(self.name)
            print player_inventory
            print "You take the %s." % (self.name)
        except: print "I don't see that item."

    def drop(self, player_inventory, location_inventory):
        try:
            player_inventory.remove(self.name)
            location_inventory.append(self.name)
            print player_inventory
            print "You drop the %s." % (self.name)
        except: print "You're not carrying that!"

class Key(Item):
    def level_up(self, player_level):
        numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six'}

        if player_level == 1:
            num = numbers[player_level].capitalize() + ' is'
        else:
            num = numbers[player_level].capitalize() + ' are'
        self.description = '''It's a silver bracelet, set with seven emeralds. %s glowing.''' % (num)


class Book(Item):
    def __init__(self, name, description, inside, home=None, spell=None):
        self.inside = inside
        self.home = home
        self.spell = spell
        super(Book, self).__init__(name, description)

    def open(self):
        if self.name in player.player.inventory:
            print self.inside
            if self.spell: player.player.known_spells.append(self.spell)
        else: print "You have to pick it up first!"

    def shelve(self, player_location, player_inventory, shelved_books):
        if player_location in self.home:
            player_inventory.remove(self.name)
            shelved_books.add(self.name,)
            print "You shelve the %s." % (self.name)
        else: print "You can only shelve books where they belong!"

#Items
# pan_pipes = Item('pipes', '''It's a set of pan pipes. There are seven total. They're plain wood,
# bound together with leather, and inscribed with Charter marks.''')
# bells = Item('bells', '''A set of seven bells hang on a bandolier, meant to be worn across the chest. Their leather pouches are
# etched with Charter marks and the bells' mahogany handles stick out of the top of the pouches.''')

mouse = Item('mouse', '''It's a small clockwork mouse, about the size of your fist. There's a turnkey sticking out of the back.
Interestingly, it also buzzes in your hand, like it's connected to the Charter somehow.''')
key = Key('key', '''It's a silver bracelet, set with seven emeralds. One is glowing.''')
waistcoat = Item('waistcoat', '''A yellow waistcoat. It flatters you quite nicely. And so professional!
There's a whistle clipped to the lapel.''')
dagger = Item('dagger', '''A silver dagger in a leather scabbard, attached to a belt. The blade looks quite sharp
and there are Charter marks etched on the hilt.''')
dog_statue = Item('statue', '''It's a small soapstone statue of a dog. The nose is rubbed smooth.''')
phial = Item('phial', '''A small crystal phial. It's sealed with powerful Charter magic.''')

#Books (Subclass of Items)
ledger = Book('ledger',
'''It's a large leather ledger. It's incredibly heavy, and when you open it you feel as though it
contains every piece of equipment checked out by every librarian in the history of the Clayr. It's that big. You probably don't want
to carry it around.''',
'''As you expected, the book is full of lists of equipment checked out to past librarians. And there's your name,
at the very bottom! There's a list of equipment for you, including a dagger, a clockwork mouse, a key, and
a yellow waistcoat. Now, I wonder where those things could be. (You didn't lose them already, did you?)''')

#Level 1 Books
belle_et_bete = Book('french book',
    '''The book has a plain brown cloth cover that says, "La Belle et la Bete." The only other
adornment is a red rose on the spine.''',
'''It's beautifully illustrated, with gold leaf covering the hand-drawn pictures of Belle and the beast.
It looks like this book belongs in the Beast's library.''',
rooms.beast_library)


#Level 2 Books
grimms_fairy_tales = Book('fairy tale book',
    '''It has a brown leather cover, embossed with the title: "Grimm's Fairy Tales." There is a
red rose stamped on the spine.''',
'''These stories seem kind of gruesome, you note as you flip through the book. There seem to be an
awful lot of people getting eaten and/or stabbing each other.''',
rooms.beast_library)

jack_beanstalk = Book('floral book',
    '''There's a patterened motif of vines and flowers covering this book, which is a copy of "Jack and
the Beanstalk." There's also a red rose stamped on the spine.''',
'''It looks like someone's run rampant with the story here; this is a full novelisation
of Jack and the Beanstalk.''', rooms.beast_library)

princess_bride = Book('princess book',
    '''This book has a red cover. The title is "The Princess Bride," and there's a red rose on the spine.''',
    '''Far-off places, daring swordfights, magic spells, and a prince in disguise!''',
    rooms.beast_library)

spell_book = Book('charter book',
    'It\'s a plain brown book, small enough to fit in the palm of your hand.',
    '''It's full of spells! There's one that looks right at your level. You read it, and suddenly feel like you've been totally
immersed in the Charter. ''', None, 'otter')
