import json

def import_from_json(filename, ObjName, SecondaryObj=None, TertiaryObj=None):
    """
    ObjName = the type of object things are turned into. Passed in by the game
    object init.
    """
    object_dict = {}
    json_dict = json.load(open(filename + '.json'))
    for name, individual_object in json_dict.iteritems():
        if filename == 'people' and name == 'vancelle':
            object_dict[name] = SecondaryObj()
            object_dict[name].__dict__.update(individual_object)
        elif filename == 'people' and name == 'doctor':
            object_dict[name] = TertiaryObj()
            object_dict[name].__dict__.update(individual_object)
        elif filename == 'items' and name == 'key':
            object_dict[name] = SecondaryObj()
            object_dict[name].__dict__.update(individual_object)
        else:
            object_dict[name] = ObjName()
            object_dict[name].__dict__.update(individual_object)
    return object_dict