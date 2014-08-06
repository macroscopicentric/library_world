import json
import random

from rooms import Room
from people import NPC, Librarian, Baddie
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
        with open('people.json') as f:
            self.npc_list = reconstitute(json.load(f))

        with open('spells.json') as f:
            self.spells = reconstitute(json.load(f))

        with open('items.json') as f:
            self.item_list = reconstitute(json.load(f))

        with open('rooms.json') as f:
            self.directory = reconstitute(json.load(f))
        self.directory[home].check_banana = True
        self.add_to_room({
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
            'dw_library': ['archbishop book'],
            'little_shop': ['wire']
            })
        self.add_npcs({
            'chiefs_office': 'vancelle',
            'labyrinth1': 'jorge',
            'binding_room': 'clippy',
            'uu_library1': 'orangutan',
            'upper_librarian_hallway': 'imshi',
            'beast_library5': 'cogsworth',
            'beast_library3': 'lumiere',
            'dw_library': 'vashta-nerada',
            })

    #less than thrilled that this relies on side effects. solution? also repetitive w/ below.
    def add_to_room(self, thing_dict):
        for room, items in thing_dict.iteritems():
            self.directory[room].inventory = items

    def add_npcs(self, npc_dict):
        for room, character in npc_dict.iteritems():
            self.directory[room].npc = character

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

    def check_move(self, direction):
        try:
            current_location_object = self.directory[self.player_state['location']]
            next_location_object = self.directory[current_location_object.directions[direction]]

            def move(direction):
                    if next_location_object.locked:
                        if self.player_state['alive'] == False:
                            self.player_state['location'] = next_location_object.short_name
                            return next_location_object.describe()
                        else:
                            return next_location_object.locked_description
                    else:
                        self.player_state['location'] = next_location_object.short_name
                        return next_location_object.describe()

            #if direction in rooms.self.location.directions and...:
            #     print "That opening is too small for a full-sized person.
            #Perhaps something smaller, like a cat or otter, could get through."
            if direction == 'd' and (self.player_state['location'] in
                ['uu_library1', 'uu_library2']):
                    self.directory['uu_library1'].add_counter()
                    action = move(direction)
                    action['event'] = '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
        and down is up. But now it's gone, so you don't trouble yourself over it.'''
                    return action

            if next_location_object.npc:
                next_location_npc_object = self.npc_list[next_location_object.npc]
                if type(next_location_npc_object) == type(self.npc_list['vashta-nerada']):
                    #Need to make bad_thing number (int between 0 and 100) modifiable.
                    #bad_thing range: 0 = guaranteed to avoid do_bad_thing, 100 = guaranteed to happen
                    if (random.random() * 100) < next_location_npc_object.bad_thing:
                        return next_location_npc_object.do_bad_thing(self, player)

            return move(direction)

        except KeyError:
            return "You can't go that way, stupid."

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
                game_object.__dict__[name] = reconstitute(value)
            return game_object
        else:
            return {k: reconstitute(v) for k, v in json_dict.iteritems()}
    else:
        raise ValueError('Object of type %s found, shouldn\'t occur in json dict.' % type(json_dict))







