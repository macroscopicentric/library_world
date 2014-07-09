from import_from_json import import_from_json
from rooms import Room
from people import NPC, Librarian
from items import Item, Key, Book
from spells import Spell

home = 'reading_room'

class Game(object):
    def __init__(self):
        self.player_state = {
            'alive': True,
            'location'      : home,
            'shape'         : 'human',
            'size'          : 'medium',
            'flying'        : False,
            'known_spells'  : ['human'],
            'spell_counter' : 0,
            'inventory'     : [],
            'shelved_books' : [],
            'level'         : 1
            }

        self.npc_list = import_from_json('people', NPC, Librarian)

        self.spells = import_from_json('spells', Spell)

        self.item_list = import_from_json('items', Item, Key)
        self.item_list.update(import_from_json('items_books', Book))

        self.directory = import_from_json('rooms', Room)
        self.directory[home].check_banana = True
        self.room_invent({
            'labyrinth1': ['chalk', 'potions book'],
            'second_assistant_study': ['statue', 'red waistcoat'],
            'labyrinth46': ['epic book'],
            # 'binding_room': ['wire'],
            'finis_africae': ['drama book'],
            'librarian_alcove': ['ledger'],
            'hall24': ['floral book'],
            'third_assistant_study': ['mouse', 'key', 'yellow waistcoat', 'dagger'],
            'restricted': ['diary', 'western book'],
            'labyrinth31': ['fantasy book'],
            'uu_library4': ['princess book'],
            'labyrinth22': ['south african book'],
            'wtnv_library6': ['astronomy book'],
            'alexandria1': ['translation book'],
            'alexandria2': ['magic book'],
            'hall3': ['french book'],
            'stilken_room2': ['phial'],
            'stilken_room1': ['odyssean book'],
            'wtnv_library1': ['dark history book'],
            'wtnv_library7': ['labyrinth book'],
            'beast_library2': ['banana'],
            'robing_room': ['fairy tale book'],
            'little_shop': ['wire']
            })

    #less than thrilled that this relies on side effects. solution?
    def room_invent(self, invent_dict):
        for room, items in invent_dict.iteritems():
            self.directory[room].inventory = items

    def level_up(self, level):
        self.player_state['level'] = level

    #increases spell_counter so I can give a warning on how to change back:
    def first_spell(self):
        self.player_state['spell_counter'] = 1
        return ''''You've used your first spell! To change back to human, just type "cast human".'''

    #for checking inventory from other modules:
    def invent_test(self, item):
        return item in self.player_state['inventory']

    #for testing location from other modules:
    def location_test(self, location):
        return location == self.player_state['location']

    def inventory_check(self):
        if self.player_state['inventory'] == []:
            check_result = "You're not holding anything!"
        else:
            check_result = {'header': "You're holding:", 'text': []}
            for thing in self.player_state['inventory']:
                check_result['text'] += [thing]

        return check_result

    def take(self, item):
        self.player_state['inventory'].append(item)

    def drop(self, item):
        self.player_state['inventory'].remove(item)

    def shelve_book(self, book):
        self.drop(book)
        self.player_state['shelved_books'].append(book)

    def spell_check(self):
        if self.player_state['known_spells'] == ['human']:
            spells_inventory = "You don't know any spells."
        else:
            spells_inventory = {'header': "You know these spells:", 'text': []}
            for spell in self.player_state['known_spells']:
                if spell != 'human':
                    spells_inventory['text'] += [spell]

        return spells_inventory

    def add_spell(self, spell):
        self.player_state['known_spells'].append(spell)

    def spell_change(self, spell):
        player_state['shape'] = spell.name
        player_state['size'] = spell.size
        player_state['flying'] = spell.flying

    def move(self, direction):
        current_location_object = self.directory[self.player_state['location']]
        next_location_object = self.directory[current_location_object.directions[direction]]
        if next_location_object.locked:
            if self.player_state['alive'] == False:
                self.player_state['location'] = next_location_object.short_name
                return next_location_object.describe()
            else:
                return next_location_object.locked_description
        else:
            self.player_state['location'] = next_location_object.short_name
            return next_location_object.describe()

    def teleport(self):
        if 'labyrinth' in self.player_state['location']:
            self.player_state['location'] = 'labyrinth1'
            return self.directory[self.player_state['location']].describe()
        else:
            self.player_state['location'] = home
            return self.directory[self.player_state['location']].describe()



#Save/load helpers for converting to json (Tom's code):
def simplify(game_object):
    if isinstance(game_object, (int, basestring, list, type(None), bool)):
        return game_object
    elif isinstance(game_object, dict):
        return {k: simplify(v) for k, v in game_object.iteritems()}
    else:
        custom_type = type(game_object).__name__
        d = simplify(game_object.__dict__)
        d['custom_type'] = custom_type
        return d

def reconstitute(json_dict):
    "Returns actual game object."
    if isinstance(json_dict, (int, basestring, list, type(None), bool)):
        return json_dict
    elif isinstance(json_dict, dict):
        if 'custom_type' in json_dict:
            game_object = globals()[json_dict.pop('custom_type')]()
            for name, value in json_dict.iteritems():
                #below to convert Vancelle's dict to new list format.
                if (game_object != 'vancelle' and name != 'levels'):
                    game_object.__dict__[name] = reconstitute(value)
            return game_object
        else:
            return {k: reconstitute(v) for k, v in json_dict.iteritems()}
    else:
        raise ValueError('Object of type %s found, shouldn\'t occur in json dict.' % type(json_dict))







