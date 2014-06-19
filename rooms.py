from import_from_json import import_from_json
import formatting

opposite_directions = {'e': 'w', 'w': 'e', 'n': 's', 's': 'n', 'u': 'd',
'd': 'u', 'ne': 'sw', 'sw': 'ne', 'nw': 'se', 'se': 'nw'}

class Room(object):
    def __init__(self, short_name=None, name=None, description=None,
        directions=None, inventory=None, npc=None, locked=False,
        locked_description='''That door's locked. And it'll stay locked no
matter how many times you tug on the handle, so stop trying.''',
        secondary_description=None, check_banana=False):
        self.short_name = short_name
        self.name = name
        self.description = description

        if directions == None:
            self.directions = {}
        else:
            self.directions = directions

        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

        self.npc = npc
        self.locked = locked
        self.counter = 0
        self.locked_description = locked_description
        self.secondary_description = secondary_description
        #secondary_description = a full description of the room to replace it
        #when an event has happened (ex: putting out the Alexandria fire).
        self.check_banana = check_banana

    #I can get rid of this now:
    def add_directions(self, **kwargs):
        for direction, room in kwargs.iteritems():
            self.directions[str(direction)] = room.short_name

        for direction in self.directions.keys():
            if self.name == 'Unseen University Library' and direction == 'd':
                pass
            else:
                next_room = directory[self.directions[direction]]
                opposite = opposite_directions[direction]
                next_room.directions[opposite] = self.short_name

    def describe(self):
        room_description = {'header':self.name, 'text': [self.description]}

        if self.counter == 1 and self.secondary_description:
            room_description['text'] = self.secondary_description

        if self.inventory:
            room_description['inventory'] = formatting.list_items(self.inventory)

        if self.npc != None:
            room_description['npc'] = formatting.print_npc(self.npc, 'room') + ' is here.'

        return room_description

    def unlock(self):
        self.locked = False

    def add_counter(self):
        self.counter = 1

    def add_invent(self, item):
        self.inventory.append(item)

    def remove_invent(self, item):
        self.inventory.remove(item)

    #unused:
    def go_to_hospital(self):
        output = '''You hear a massive CRASH from the direction of the Restricted
Section. The next minute, a gurney rushes by you with Madame Pince lying on it,
her arm thrown dramatically over her eyes.'''
        directory['hall15'].counter = 1
        directory['restricted'].unlock()
        return output

directory = import_from_json('rooms', Room)
