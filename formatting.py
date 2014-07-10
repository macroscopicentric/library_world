"""
Because I'm an English major and have standards for natural English language
printouts for items/NPCS.
"""

def list_items(items):
    singular = "There is "
    plural = 'There are '

    if len(items) == 1:
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
    if word[-1] == 's':
        return word
    else:
        if word[0] in consonants:
            return 'a ' + word
        else:
            return 'an ' + word

def print_npc(npc, function):
    if function == 'room':
        article = 'An'
    elif function == 'give':
        article = 'The'

    if npc == 'orangutan':
        return "%s %s" % (article, npc)
    else: return "%s" % (npc.capitalize())