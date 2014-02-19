import time

import rooms
import people

home = rooms.reading_room

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
        if direction == 'e' and self.location == rooms.reading_room:
            print "No, I really don't think you want to go that way. Why don't you stick to the library?"
        elif direction == 'd' and (self.location == rooms.uu_library1 or
            self.location == rooms.uu_library2):
            print '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
and down is up. But now it's gone, so you don't trouble yourself over it.'''
            print
            self.location = self.location.directions[direction]
            time.sleep(3)
            self.location.describe()
        elif direction not in self.location.directions:
            print "You can't go that way, stupid."
        elif (direction in self.location.directions
            and self.location.directions[direction].locked) == True:
            print '''That door's locked. And it'll stay locked no matter how many
times you tug on the handle, so stop trying.'''
        # elif direction in rooms.self.location.directions and...:
        #     print "That opening is too small for a full-sized person. Perhaps something smaller, like a cat or otter, could get through."
        #need a way to ID a DOOR (as opposed to a room, which I did for the locked rooms above),
        #since a door goes both ways and a key is one-time in one direction.
        elif direction in self.location.directions:
            self.location = self.location.directions[direction]
            self.location.describe()
        else:
            print "I didn't understand that direction, sorry."

    def teleport(self):
        if self.location in rooms.labyrinths:
            self.location = rooms.labyrinth1
            self.location.describe()
        else:
            self.location = home
            self.location.describe()

player = Player()
