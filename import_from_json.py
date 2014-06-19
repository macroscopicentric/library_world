import json

def import_from_json(filename, ObjName, SecondaryObj=None):
    object_dict = {}
    json_dict = json.load(open(filename + '.json'))
    for name, ind_object in json_dict.iteritems():
        if filename == 'people' and name == 'vancelle':
            object_dict[name] = SecondaryObj()
            object_dict[name].__dict__.update(ind_object)
        elif filename == 'items' and name == 'key':
            object_dict[name] = SecondaryObj()
            object_dict[name].__dict__.update(ind_object)
        else:
            object_dict[name] = ObjName()
            object_dict[name].__dict__.update(ind_object)
    return object_dict