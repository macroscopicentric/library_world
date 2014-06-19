import time

from rooms import directory

home = 'reading_room'
# home = 'chiefs_office'
directory[home].check_banana = True

class Player(object):
    def __init__(self, inventory=None):
        self.alive = True
        self.location = home
        self.shape = 'human'
        self.size = 'medium'
        self.flying = False
        self.known_spells = ['human']
        self.spell_counter = 0

        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

        self.shelved_books = []
        self.level = 1

    def level_up(self):
        self.level += 1

    #increases self.spell_counter so I can give a warning on how to change back:
    def first_spell(self):
        self.spell_counter += 1
        return ''''You've used your first spell! To change back to human, just type "cast human".'''

    #for checking inventory from other modules:
    def invent_test(self, item):
        return item in self.inventory

    #for testing location from other modules:
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
        self.shelved_books.append(book)

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
        current_location_object = directory[self.location]
        next_location_object = directory[current_location_object.directions[direction]]
        if next_location_object.locked:
            return next_location_object.locked_description
        else:
            self.location = next_location_object.short_name
            return directory[self.location].describe()

    def teleport(self):
        if 'labyrinth' in self.location:
            self.location = 'labyrinth1'
            return directory[self.location].describe()
        else:
            self.location = home
            return directory[self.location].describe()

player = Player()
