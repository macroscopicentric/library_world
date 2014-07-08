import random

import formatting

class NPC(object):
    def __init__(self):
        self.name = ''
        self.dialogue = []
        self.want = ''
        self.wish_come_true = False

    def new_dialogue(self, new_dialogue):
        self.dialogue = new_dialogue

    def talk(self, game, player_state):
        if self.name == 'orangutan' and self.wish_come_true == False:
            if game.invent_test('translation book'):
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

    def wish_fulfillment(self, game, item):
        if self.name == 'orangutan':
            if self.want == item:
                reward = 'charter book'
                game.drop(item)
                game.take(reward)
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
    def __init__(self):
        super(Librarian, self).__init__()
        #Storing levels here instead of in JSON with NPCs because keys need to be ints.
        self.levels = [
            ["french book"], 
            ["fairy tale book", "floral book", "princess book"],
            ["astronomy book", "potions book", "fantasy book",
                "dark history book", "diary"],
            ["odyssean book", "epic book", "western book", "magic book"],
            ["labyrinth book", "south african book"],
            ["drama book"]]
            
    def level_up(self, game, player):
        level_dialogue = {'text': []}
        if game.invent_test('key'):
            for level, books in enumerate(self.levels):
                for book in books:
                    if book not in player['shelved_books']:
                        return level_dialogue
                game.level_up(level + 2)
                print 'player level: %s' % (player['level'])
                game.item_list['key'].level_up(game, player['level'])
                level_dialogue['event'] = '''Level up! You're now level %s.''' % (player['level'])

                if player['level'] == 2:
                    level_dialogue['header'] = '"Congratulations, you\'ve shelved your first book. Now go do the rest."'
                if player['level'] == 4:
                    level_dialogue['header'] = '''"Congratulations, I\'ve decided to promote you to Second-Assistant
Librarian! You now have a new study off of the Second-Assistant Hallway
downstairs."'''
        return level_dialogue

    def talk(self, game, player):
        level_dialogue = self.level_up(game, player)
        goal = '''"You need to shelve these books to get to level %s:"''' % (player['level'] + 1)

        #for proper formatting of dialogue ("") and adding space between potential dialogue from level_up.
        if 'header' in level_dialogue.keys():
            level_dialogue['header'] = level_dialogue['header'][0:-1] + ' ' + goal[1:]
        else:
            level_dialogue['header'] = goal

        level_dialogue['text'] = self.levels[player['level'] - 1]

        return level_dialogue

