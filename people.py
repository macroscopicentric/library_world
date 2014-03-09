import random

import formatting

import rooms
import items

npc_list = {}

class NPC(object):
    def __init__(self, name, dialogue=[], want=''):
        self.name = name
        self.dialogue = dialogue
        self.want = want
        self.wish_come_true = False
        npc_list[name] = self

    def new_dialogue(self, new_dialogue):
        self.dialogue = new_dialogue

    def talk(self, player):
        if self.name == 'orangutan' and self.wish_come_true == False:
            if player.invent_test('translation book'):
                self.new_dialogue(['''"Oh woe is me," says the Librarian forlornly, "I have lost my
chalk and cannot navigate the library, like Theseus in the
Minotaur's Labyrinth."'''])
            else:
                self.new_dialogue(['"Ooook ook."', '"Eeek eek!"',
                    '"Ook eek." >:('])

        try: print self.dialogue[random.randint(0, len(self.dialogue) - 1)]
        except: print "%s doesn't say anything." % (self.name.capitalize())

    def wish_fulfillment(self, item, player):
        if self.want == item:
            if self.name == 'orangutan':
                reward = 'charter book'
                print formatting.print_npc(self.name,
                    'give') + " takes the %s from you." % (item)
                player.drop(item)
                print "The Librarian gives you a %s." % (reward)
                player.take(reward)
                self.wish_come_true = True
                self.new_dialogue(['The orangutan smiles contentedly at you.'])            
        elif self.name == 'orangutan' and item == 'banana':
            print formatting.print_npc(self.name,
                'give') + " looks at you in disgust."
        else: print formatting.print_npc(self.name,
            'give') + " doesn't want that."


class Librarian(NPC):
    def __init__(self, *args):
        super(Librarian, self).__init__(*args)
        self.levels = {}

    def add_levels(self, *args):
        counter = 1
        for books in args:
            self.levels[counter] = books
            counter += 1
            
    def level_up(self, player):
        for level in self.levels:
            if self.levels[level] <= player.shelved_books and 'key' in player.inventory:
                player.level_up()
                items.key.level_up(player.level)
                print '''Level up! You're now level %s.''' % (player.level)

                #How to print the following only the first time, when they level up?
                if player.level == 2:
                    print '"Congratulations, you\'ve shelved your first book. Now go do the rest."'
                if player.level == 4:
                    print '''"Congratulations, I\'ve decided to promote you to Second-Assistant
Librarian! You now have a new study off of the Second-Assistant Hallway
downstairs."'''


    def talk(self, player):
        self.level_up(player)
        print "You need to shelve these books to get to level %i:" % (player.level + 1)
        print
        for book in self.levels[player.level]:
            print book
        


vancelle = Librarian('vancelle')
vancelle.add_levels(set(('french book',)), set(('fairy tale book',
    'floral book', 'princess book')), set(('astronomy book', 'potions book',
    'fantasy book')))

uu_librarian = NPC('orangutan', ['"Ooook ook."', '"Eeek eek!"',
    '"Ook eek." >:('], want='chalk')

imshi = NPC('imshi',
    ['''"Talk to Vancelle to learn what books you need to shelve. Make sure you
have your key though!"''',
    '"If you\'re looking for your key, have you checked your office?"'])

clippy = NPC('clippy',
    ['''"It looks like you're trying to become a first-assistant librarian!...
I'm sorry, I can't help with that."''',
'''"I'm sorry, I've been ordered to ignore all attempts to hide my super useful
awesome tips."''',
'''"Why would you want to disable me? I'm so helpful." :( :( :(''',
'''"YES HELPFUL I AM HELPING SO HELPFUL."'''])

jorge = NPC('jorge',
    ['''"Laughter kills fear, and without fear there can be no faith, because
without fear of the Devil, there is no need of God."''',
'"Christ never laughed and nor should you."',
'''"Laughter is a devilish wind which deforms the lineaments of the face and
makes men look like monkeys."''',
'Jorge frowns at you severely.'])

lumiere = NPC('lumiere',
    ['''"You shouldn't believe anything that overgrown pocketwatch says."''',
    '''"Ma chere mademoiselle, I hope you enjoy our mountains of books!"''',
    '''"It is with deepest pride and greatest pleasure that we welcome you...
to the library!"'''])

cogsworth = NPC('cogsworth',
    ['''"You shouldn't listen to that paraffin-headed peabrain!"''',
    '''"I hope you enjoy our library; there are more books than you'll be able
to read in a lifetime!"''',
    '''"This is an example of the late neoclassic Baroque period. And, as I
always say, 'If it's not Baroque, don't fix it!'"'''])
