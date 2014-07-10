"""
Used every time a new game is initialized.
"""

import json

def import_from_json(filename, ObjName, SecondaryObj=None):
    object_dict = {}
    with open(filename + '.json') as f:
        json_dict = json.load(f)
    for name, individual_object in json_dict.iteritems():
        if filename == 'people' and name == 'vancelle':
            object_dict[name] = SecondaryObj()
            object_dict[name].__dict__.update(individual_object)
        elif filename == 'items' and name == 'key':
            object_dict[name] = SecondaryObj()
            object_dict[name].__dict__.update(individual_object)
        else:
            object_dict[name] = ObjName()
            object_dict[name].__dict__.update(individual_object)
    return object_dict