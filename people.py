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

    def talk(self):
        try: print self.dialogue[random.randint(0, len(self.dialogue) - 1)]
        except: print "%s doesn't say anything." % (self.name.capitalize())

class Librarian(NPC):
    def __init__(self, *args):
        super(Librarian, self).__init__(*args)

    def add_levels(self, **kwargs):
        for level, book_list in kwargs.items():
            setattr(self, level, book_list)
            
    def level_up(self, player_level, shelved_books):
        if self.level1 <= shelved_books:
            player_level += 1
            print '''Level up! You're now level 2.'''
            self.new_dialogue(['''"Congratulations, you've shelved your first book."'''])


    def talk(self, player_level, shelved_books):
        self.level_up(player_level, shelved_books)
        try: print self.dialogue[random.randint(0, len(self.dialogue) - 1)]
        except: print "%s doesn't say anything." % (self.name.capitalize())
        


vancelle = Librarian('vancelle', rooms.chiefs_office, ['Vancelle ignores you.'])
vancelle.add_levels(level1=set(('fairy tale book',)))

uu_librarian = NPC('orangutan', rooms.uu_library1, ['"Ooook ook."', '"Eeek eek!"',
    '"Ook eek." >:('])
imshi = NPC('imshi', rooms.middle_librarian_hallway, ['"Go shelve a book, then come back and talk to Vancelle."'])
clippy = NPC('clippy', rooms.binding_room,
    ['''"It looks like you're trying to become a first-assistant librarian!... I'm sorry, I can't help with that."''',
'''"I'm sorry, I've been ordered to ignore all attempts to hide my super useful awesome tips."''',
'''"Why would you want to disable me? I'm so helpful." :( :( :(''',
'''"YES HELPFUL I AM HELPING SO HELPFUL."'''])
jorge = NPC('jorge', rooms.labyrinth1,
    ['''"Laughter kills fear, and without fear there can be no faith, because without
fear of the Devil, there is no need of God."''', '"Christ never laughed and nor should you."',
'"Laughter is a devilish wind which deforms the lineaments of the face and makes men look like monkeys."',
'Jorge frowns at you severely.'])
lumiere = NPC('lumiere', rooms.beast_library3, ['''"You shouldn't believe anything that overgrown pocketwatch says."''',
    '''"Ma chere mademoiselle, I hope you enjoy our mountains of books!"''',
    '''"It is with deepest pride and greatest pleasure that we welcome you... to the library!"'''])
cogsworth = NPC('cogsworth', rooms.beast_library5, ['''"You shouldn't listen to that paraffin-headed peabrain!"''',
    '''"I hope you enjoy our library; there are more books than you'll be able to read in a lifetime!"''',
    '''"This is an example of the late neoclassic Baroque period. And, as I always say, 'If it's not Baroque, don't fix it!'"'''])