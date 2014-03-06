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

    def level_up(self):
        self.level += 1

    #for checking inventory from other modules
    def invent_test(self, item):
        return item in self.inventory

    #for testing location from other modules
    def location_test(self, location):
        return location == self.location

    def inventory_check(self):
        if self.inventory == []: print "You're not holding anything!"
        else:
            print "You're holding:\n"
            for thing in self.inventory:
                print "%s" % (thing)

    def take(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def shelve_book(self, book):
        self.drop(book)
        self.shelved_books.add(self.name,)

    def spell_check(self):
        if self.known_spells == ['human']: print "You don't know any spells."
        else:
            print "You know these spells:"
            print
            for spell in self.known_spells:
                if spell != 'human':
                    print spell

    def add_spell(self, spell):
        self.known_spells.append(spell)

    def move(self, direction):
        self.location = self.location.directions[direction]
        return self.location.describe()

    def teleport(self):
        if self.location in rooms.labyrinths:
            self.location = rooms.labyrinth1
            self.location.describe()
        else:
            self.location = home
            self.location.describe()

player = Player()
