import time

import rooms
import people

home = rooms.reading_room
# home = rooms.uu_library1

class Player(object):
    def __init__(self, inventory=[]):
        self.alive = True
        self.location = home
        self.shape = 'human'
        self.size = 'medium'
        self.flying = False
        self.known_spells = ['human']
        self.inventory = inventory
        self.shelved_books = set()
        self.level = 1

    def level_check(self):
        return self.level

    def level_up(self):
        self.level += 1

    def book_progress(self):
        return self.shelved_books

    #for checking inventory from other modules
    def invent_test(self, item):
        return item in self.inventory

    #for testing location from other modules
    def location_test(self, location):
        return location == self.location

    def inventory_check(self):
        if self.inventory == []:
            check_result = "You're not holding anything!"
        else:
            check_result = {'header': "You're holding:", 'text': []}
            for thing in self.inventory:
                check_result['text'] += [thing]

        return check_result

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def shelve_book(self, book):
        self.drop(book)
        self.shelved_books.add(book,)

    def spell_check(self):
        if self.known_spells == ['human']:
            spells_inventory = "You don't know any spells."
        else:
            spells_inventory = {'header': "You know these spells:", 'text': []}
            for spell in self.known_spells:
                if spell != 'human':
                    spells_inventory['text'] += [spell]

        return spells_inventory

    def add_spell(self, spell):
        self.known_spells.append(spell)

    def move(self, direction):
        if self.location.directions[direction].lock_test():
            return self.location.directions[direction].lock_desc()
        else:
            self.location = self.location.directions[direction]
            return self.location.describe()

    def teleport(self):
        if self.location in rooms.labyrinths:
            self.location = rooms.labyrinth1
            return self.location.describe()
        else:
            self.location = home
            return self.location.describe()

player = Player()
