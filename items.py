import rooms

item_list = {}

class Item(object):
    def __init__(self, name, description, location=None):
        self.name = name
        self.description = description
        self.location = location
        item_list[name] = self

    def examine(self, player_location):
        if self.location == player_location or self.location == 'player':
            print self.description
        else: print "I'm sorry, I don't see that item."

    def take(self, player_inventory, location_inventory):
        try:
            player_inventory.append(self.name)
            self.location = 'player'
            location_inventory.remove(self.name)
            print "You take the %s." % (self.name)
        except: print "I don't see that item."

    def drop(self, player_inventory, location_inventory):
        try:
            player_inventory.remove(self.name)
            self.location = player.location
            location_inventory.append(self.name)
            print "You drop the %s." % (self.name)
        except: print "You're not carrying that!"


class Book(Item):
    def __init__(self, inside, spell=None, *args):
        self.inside = inside
        self.spell = spell
        super(Book, self).__init__(*args)

    def open(self, player_spells):
        if self.location == 'player':
            print self.inside
            if self.spell: player_spells.append(self.spell)
        else: print "You have to pick it up first!"

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
dog_statue = Item('statue', '''It's a small soapstone statue of a dog. The nose is rubbed smooth.''', rooms.second_assistant_study)
phial = Item('phial', '''A small crystal phial. It's sealed with powerful Charter magic.''', rooms.stilken_room2)

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
