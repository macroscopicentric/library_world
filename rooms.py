import formatting

class Room(object):
    def __init__(self):
        self.short_name = ''
        self.name = ''
        self.description = ''
        self.directions = {}
        self.inventory = []
        self.npc = None
        self.locked = False
        self.counter = 0
        self.locked_description = '''That door's locked. and it'll stay locked no
matter how many times you tug on the handle, so stop trying.'''
        #secondary_description = a full description of the room to replace it
        #when an event has happened (ex: putting out the Alexandria fire).
        self.secondary_description = None
        self.check_banana = False

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

    def go_to_hospital(self, directory):
        output = '''You hear a massive CRASH from the direction of the Restricted
Section. The next minute, a gurney rushes by you with Madame Pince lying on it,
her arm thrown dramatically over her eyes.'''
        directory['hall15'].counter = 1
        directory['restricted'].unlock()
        return output
