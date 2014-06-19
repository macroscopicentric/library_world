from import_from_json import import_from_json
from player import player
import rooms

class Item(object):
    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def examine(self):
        if (player.invent_test(self.name) or
            self.name in directions[player.location].inventory):
            return self.description
        else:
            return "I'm sorry, I don't see that item."

    def take(self, location):
        try:
            player.take(self.name)
            location.remove_invent(self.name)
            return "You take the %s." % (self.name)
        except:
            return "I don't see that item."

    def drop(self, location):
        try:
            player.drop(self.name)
            location.add_invent(self.name)
            return "You drop the %s." % (self.name)
        except:
            return "You're not carrying that!"

    def give(self, person):
        if person.name == rooms.directory[player.location].npc:
            try:
                person.wish_fulfillment(self.name, player)
            except:
                return "You're not carrying that!"
        else:
            return "That person isn't here!"


class Key(Item):
    def level_up(self, player_level):
        numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six'}

        level2_unlocks = ['uu_library1', 'wtnv_library1', 'labyrinth1',
            'alexandria1']
        level4_unlocks = ['stilken_room1', 'second_assistant_study']

        if player_level == 1:
            num = numbers[player_level].capitalize() + ' is'
        else:
            num = numbers[player_level].capitalize() + ' are'

        if player_level == 2:
            for room in level2_unlocks:
                rooms.directory[room].unlock()
        if player_level == 4:
            for room in level4_unlocks:
                rooms.directory[room].unlock()
                rooms.directory['third_assistant_study'].add_counter()
        self.description = '''It's a silver bracelet, set with seven emeralds. %s glowing.''' % (num)

        return self.description


class Book(Item):
    def __init__(self, name=None, description=None, inside=None, home=None, spell=None):
        self.inside = inside
        self.home = home
        self.spell = spell
        super(Book, self).__init__(name, description)

    def open(self):
        if self.name in player.player.inventory:
            if self.spell:
                player.player.add_spell(self.spell)
            return self.inside
        else:
            return "You have to pick it up first!"

    def shelve(self):
        if player.location in self.home:
            player.shelve_book(self.name)
            return "You shelve the %s." % (self.name)
        else:
            return "You can only shelve books where they belong!"

item_list = import_from_json('items', Item, Key)
item_list.update(import_from_json('items_books', Book))
