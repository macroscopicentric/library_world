

def list_items(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return article(items[0])
    elif len(items) == 2:
        return article(items[0]) + ' and ' + article(items[1])
    else:
        description = ''
        for item in items[1: -1]:
            description += ', ' + article(item)
        return article(items[0]) + description + ', and ' + article(items[-1])

def article(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    if word[0] in consonants:
        return 'a ' + word
    else:
        return 'an ' + word
