import json
from rooms import directory
from items import item_list
from spells import spells
from people import npc_list

def dump_things_to_json(object_dictionary, filename):
    json_dict = {}
    for name, ind_object in object_dictionary.iteritems():
        json_dict[name] = {a:b for a, b in ind_object.__dict__.iteritems() if b}

    json.dump(json_dict, open(filename + '.json', 'w'), indent=2)


if __name__ == '__main__':
    dump_things_to_json(directory, 'rooms')
    dump_things_to_json(item_list, 'items')
    dump_things_to_json(spells, 'spells')
    dump_things_to_json(npc_list, 'people')