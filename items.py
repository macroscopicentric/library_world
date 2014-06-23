class Item(object):
    def __init__(self):
        self.name = ''
        self.description = None

    def examine(self, game, location):
        if (game.invent_test(self.name) or
            self.name in location.inventory):
            return self.description
        else:
            return "I'm sorry, I don't see that item."

    def take(self, game, location):
        try:
            game.take(self.name)
            location.remove_invent(self.name)
            return "You take the %s." % (self.name)
        except:
            return "I don't see that item."

    def drop(self, game, location):
        try:
            game.drop(self.name)
            location.add_invent(self.name)
            return "You drop the %s." % (self.name)
        except:
            return "You're not carrying that!"


class Key(Item):
    def level_up(self, game, player_level):
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
                game.directory[room].unlock()
        if player_level == 4:
            for room in level4_unlocks:
                game.directory[room].unlock()
                game.directory['third_assistant_study'].add_counter()
        self.description = '''It's a silver bracelet, set with seven emeralds. %s glowing.''' % (num)


class Book(Item):
    def __init__(self):
        self.inside = None
        self.home = None
        self.spell = None
        super(Book, self).__init__()

    def open(self, game, player_inventory):
        if self.name in player_inventory:
            if self.spell:
                game.add_spell(self.spell)
            return self.inside
        else:
            return "You have to pick it up first!"

    def shelve(self, game, location):
        if location in self.home:
            game.shelve_book(self.name)
            return "You shelve the %s." % (self.name)
        else:
            return "You can only shelve books where they belong!"
