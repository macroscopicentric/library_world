

def list_items(items):
    singular = "\nThere is "
    plural = '\nThere are '

    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return singular + article(items[0]) + ' here.'
    elif len(items) == 2:
        return plural + article(items[0]) + ' and ' + article(items[1]) + ' here.'
    else:
        description = ''
        for item in items[1: -1]:
            description += ', ' + article(item)
        return plural + article(items[0]) + description + ', and ' + article(items[-1]) + ' here.'

def article(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    if word[0] in consonants:
        return 'a ' + word
    else:
        return 'an ' + word
