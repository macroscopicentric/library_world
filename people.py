import random

from import_from_json import import_from_json
import formatting
import rooms
from items import item_list

class NPC(object):
    def __init__(self, name=None, dialogue=None, want=''):
        self.name = name
        if dialogue == None:
            self.dialogue = []
        else:
            self.dialogue = dialogue
        self.want = want
        self.wish_come_true = False

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

        try:
            return self.dialogue[random.randint(0, len(self.dialogue) - 1)]
        except:
            return "%s doesn't say anything." % (self.name.capitalize())

    def wish_fulfillment(self, item, player):
        if self.name == 'orangutan':
            if self.want == item:
                reward = 'charter book'
                player.drop(item)
                player.take(reward)
                self.wish_come_true = True
                self.new_dialogue(['The orangutan smiles contentedly at you.']) 
                return (formatting.print_npc(self.name,
                    'give') + " takes the " + item + " from you and gives you a " + reward + " in return.")          
            elif item == 'banana':
                return formatting.print_npc(self.name,
                    'give') + " looks at you in disgust."
        else:
            return formatting.print_npc(self.name,
            'give') + " doesn't want that."


class Librarian(NPC):
    def __init__(self, *args):
        super(Librarian, self).__init__(*args)
        self.levels = {}

    def add_levels(self, book_dict):
        for level, books in book_dict.iteritems():
            self.levels[level] = books
            
    def level_up(self, player):
        level_dialogue = {'text': []}
        str_level = str(player.level)
        for level in self.levels:
            if (set(self.levels[level]) <= set(player.shelved_books)) and player.invent_test('key'):
                player.level_up()
                item_list['key'].level_up(player.level)
                level_dialogue['event'] = '''Level up! You're now level %s.''' % (player.level)

                #How to print the following only the first time, when they level up?
                if player.level == 2:
                    level_dialogue['header'] = '"Congratulations, you\'ve shelved your first book. Now go do the rest."'
                if player.level == 4:
                    level_dialogue['header'] = '''"Congratulations, I\'ve decided to promote you to Second-Assistant
Librarian! You now have a new study off of the Second-Assistant Hallway
downstairs."'''
        return level_dialogue

    def talk(self, player):
        level_dialogue = self.level_up(player)
        goal = '''"You need to shelve these books to get to level %i:"''' % (player.level + 1)

        #for proper formatting of dialogue ("") and adding space between potential dialogue from level_up.
        if 'header' in level_dialogue.keys():
            level_dialogue['header'] = level_dialogue['header'][0:-1] + ' ' + goal[1:]
        else:
            level_dialogue['header'] = goal

        for book in self.levels[str(player.level)]:
            level_dialogue['text'] += [book]

        return level_dialogue

npc_list = import_from_json('people', NPC, Librarian)
