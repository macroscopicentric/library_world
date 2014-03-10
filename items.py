import player
import rooms

item_list = {}

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        item_list[name] = self

    def examine(self):
        if (self.name in player.player.inventory or
            self.name in player.player.location.inventory):
            print self.description
        else: print "I'm sorry, I don't see that item."

    def take(self, location):
        try:
            player.player.take(self.name)
            location.remove_invent(self.name)
            print "You take the %s." % (self.name)
        except: print "I don't see that item."

    def drop(self, location):
        try:
            player.player.drop(self.name)
            location.add_invent(self.name)
            print "You drop the %s." % (self.name)
        except: print "You're not carrying that!"

    def give(self, person):
        if person.name == player.player.location.npc:
            try:
                person.wish_fulfillment(self.name, player.player)
            except: print "You're not carrying that!"
        else: print "That person isn't here!"


class Key(Item):
    def level_up(self, player_level):
        numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six'}

        level2_unlocks = [uu_library1, wtnv_library1, labyrinth1, alexandria1]
        level4_unlocks = [stilken_room1, second_assistant_study]

        if player_level == 1:
            num = numbers[player_level].capitalize() + ' is'
        else:
            num = numbers[player_level].capitalize() + ' are'

        if player_level == 2:
            for room in rooms.level2_unlocks:
                rooms.room.unlock()
        if player_level == 4:
            for room in rooms.level4_unlocks:
                rooms.room.unlock()
                rooms.third_assistant_study.add_counter()
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
            if self.spell: player.player.add_spell(self.spell)
        else: print "You have to pick it up first!"

    def shelve(self, player_location):
        if player_location in self.home:
            player.player.shelve_book(self.name)
            print "You shelve the %s." % (self.name)
        else: print "You can only shelve books where they belong!"

#Items
# pan_pipes = Item('pipes',
#    '''It's a set of pan pipes. There are seven total. They're plain wood,
# bound together with leather, and inscribed with Charter marks.''')
# bells = Item('bells',
#    '''A set of seven bells hang on a bandolier, meant to be worn across the
# chest. Their leather pouches are etched with Charter marks and the bells'
# mahogany handles stick out of the top of the pouches.''')
charter_book = Book('charter book',
    'It\'s a plain brown book, small enough to fit in the palm of your hand.',
    '''It's full of spells! There's one that looks right at your level. You
read it, and suddenly feel like you've been totally immersed in the
Charter.''', spell='water')

mouse = Item('mouse',
    '''It's a small clockwork mouse, about the size of your fist. There's a
turnkey sticking out of the back. Interestingly, it also buzzes in your hand,
like it's connected to the Charter somehow.''')
key = Key('key',
    '''It's a silver bracelet, set with seven emeralds. One is glowing.''')
waistcoat = Item('yellow waistcoat',
    '''A yellow waistcoat. It flatters you quite nicely. And so professional!
There's a whistle clipped to the lapel.''')
dagger = Item('dagger',
    '''A silver dagger in a leather scabbard, attached to a belt. The blade
looks quite sharp and there are Charter marks etched on the hilt.''')
dog_statue = Item('statue',
    '''It's a small soapstone statue of a dog. The nose is rubbed smooth.''')
phial = Item('phial',
    '''A small crystal phial. It's sealed with powerful Charter magic.''')

waistcoat2 = Item('red waistcoat',
    '''A red waistcoat. Looking down, you decide that red is a much better
color on you than yellow. There's a whistle clipped to the lapel.''')

banana = Item('banana', '''It's a banana. Why are you examining it.''') #red herring for Librarian (UU), way to get past Madame Pince.
chalk = Item('chalk', 'A piece of chalk. Pretty boring, really.')

wire = Item('wire', "A piece of wire about a foot long.")
scissors = Item('scissors', 'A pair of scissors.') #red herring for Restricted Section.

#Books (Subclass of Items)
ledger = Book('ledger',
'''It's a large leather ledger. It's incredibly heavy, and when you open it you
feel as though it contains every piece of equipment checked out by every
librarian in the history of the Clayr. It's that big. You probably don't want
to carry it around.''',
'''As you expected, the book is full of lists of equipment checked out to past
librarians. And there's your name, at the very bottom! There's a list of
equipment for you, including a dagger, a clockwork mouse, a key, and a yellow
waistcoat. Now, I wonder where those things could be. (You didn't lose them
already, did you?)''')

translation_book = Book('translation book',
    '''It's an orangutan-to-English translation book, printed by the Unseen
University Press.''',
'''The first entry indicates that "Ooook ook." means "I am filled with
existential angst."''')

#Level 1 Books
belle_et_bete = Book('french book',
    '''The book has a plain brown cloth cover that says, "La Belle et la Bete."
The only other adornment is a red rose on the spine.''',
'''It's beautifully illustrated, with gold leaf covering the hand-drawn
pictures of Belle and the beast.''', rooms.beast_library)


#Level 2 Books
grimms_fairy_tales = Book('fairy tale book',
    '''It has a brown leather cover, embossed with the title: "Grimm's Fairy
Tales." There is a red rose stamped on the spine.''',
'''These stories seem kind of gruesome, you note as you flip through the book.
There seem to be an awful lot of people getting eaten and/or stabbing each
other.''', rooms.beast_library)

jack_beanstalk = Book('floral book',
    '''There's a patterened motif of vines and flowers covering this book,
which is a copy of "Jack and the Beanstalk." There's also a red rose stamped on
the spine.''',
'''It looks like someone's run rampant with the story here; this is a full
novelisation of Jack and the Beanstalk.''', rooms.beast_library)

princess_bride = Book('princess book',
    '''This book has a red cover. The title is "The Princess Bride," and
there's a red rose on the spine.''',
    '''Far-off places, daring swordfights, magic spells, and a prince in
disguise!''', rooms.beast_library)

#Level 3 Books
astronomy_book = Book('astronomy book',
    '''The title of the book, and the rest of it, seem to be entirely in
Latin. There's a cross stamped on the spine.''',
'''The book is in Latin, so you can't read it. But it looks as though it's
about astronomy, as there are pages full of astronomical tables.''',
rooms.labyrinths)

potions_book = Book('potions book',
    '''It's titled "Most Potente Potions" by Phineas Bourne. The cover is
leather, but looks strangely oily and almost appears to be moving. There are
three small stars stamped on the spine.''',
'''There are directions in here for all sorts of strange potions; you managed
to open it to the page about brewing a Laxative Potion.''', rooms.restricted)

harry_potter = Book('fantasy book',
    '''This book MAY be even heavier than the librarians' ledger. There's a
picture of a boy with black hair and glasses on the cover, and three small
stars stamped on the spine.''',
'''It seems like this is another novel. This one is a fantasy novel about a
wizard and his two friends and the dark wizard they fight.''',
rooms.restricted)

colour_magic = Book('magic book', '''This book is called "The Colour of Magic"
by Terry Pratchett. There's a turtle stamped on the spine.''',
'''It's another novel. This time it's about an incompetent wizard who falls off
the edge of the world.''', rooms.uu_libraries)

#Level 4 Books
odyssey = Book('odyssean book', '''A copy of Homer's "Odyssey." There is a
scroll stamped on the spine.''',
'''When you open it, you notice that the book is heavily marked in many
different handwritings.''', rooms.alexandria)

#Level 5 Books
labyrinth_book = Book('labyrinth book',
    '''This book is titled "The Name of the Rose." There's a cross stamped on
the spine.''',
    '''The book seems to be a novel about two monks, set in a strange world
without magic.''', rooms.labyrinths)

#Level 6 Books
poetics = Book('drama book', '''It seems to be a translated copy of Poetics II,
the lost Aristotelian essay on comedic drama. There is a cross stamped on the
spine.''',
'''It's just Aristotle's theories on Greek comedic drama. Boring. Go read
something with magic in it.''', rooms.labyrinths)
