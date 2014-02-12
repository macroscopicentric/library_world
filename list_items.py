

def list_items(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return 'a ' + items[0]
    elif len(items) == 2:
        return 'a ' + items[0] + ' and a ' + items[1]
    else:
        description = ''
        for item in items[1: -1]:
            description += ', a ' + item
        return 'a ' + items[0] + description + ', and a ' + items[-1]
