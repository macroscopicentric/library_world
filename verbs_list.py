import items
import library

moves = {'u': 'u', 'up': 'u', 'd': 'd', 'down': 'd', 'n': 'n', 'north': 'n',
'e': 'e', 'east': 'e', 'w': 'w', 'west': 'w', 's': 's', 'south': 's',
'northwest': 'nw', 'nw': 'nw', 'southwest': 'sw', 'sw': 'sw', 'southeast': 'se',
'se': 'se', 'northeast': 'ne', 'ne': 'ne'}

#For testing legit nouns:
nouns = library.spells.keys() + items.items_list.keys()

def input_format(self):
    user_input = raw_input(">").lower().split(" ", 1)

    if "." in user_input[-1]:
        detail = user_input.pop().split(".").pop(0)
        user_input.append(detail)

    return user_input

def command(user_input):
    verb = user_input[0]
    noun = ''
    if len(user_input) < 1: noun = user_input[1]

    #Helper functions so I can add all methods to the verbs dictionary:
    def help_command():
        print '''My commands are like a traditional text adventure\'s. To move, use the cardinal directions ("n", "s", "e", or "w")
or "up" and "down". Other commands you can use: "look" (describes the room to you), "examine [object]", "inventory"
or "i" (lists your inventory), "take [object]", "drop [object]", "cast [Charter spell]", "spells" (lists the
spells you know), "teleport" (sends you back to the Reading Room, or the labyrinth stairs if you're in the labyrinth),
"talk [character]", "exit" or "quit" (exits the game), or "restart" (restarts the game).'''

    def say_hi():
        print "Hullo!"

    def examine():
        items.item_list[noun].examine(library.player.location)

    def take():
        print 'test'
        if noun == 'all':
            if library.player.location.inventory:
                temp = library.player.location.inventory[:]
                for item in temp:
                    items.item_list[item].take(library.player.inventory, library.player.location.inventory)
            else: print "There's nothing here to take."
        else:
            try: items.item_list[noun].take()
            except: print "I don't see that item."

    def drop():
        if noun == 'all':
            if library.player.inventory:
                temp = library.player.inventory[:]
                for item in temp:
                    items.item_list[item].drop(library.player.inventory, library.player.location.inventory)
            else: library.player.inventory_check()
        else:
            try: items.item_list[noun].drop()
            except: print "I don't see that item."

    def read():
        try: items.item_list[noun].open(library.player.known_spells)
        except: print "You can't read that. Try reading a book."

    def cast():
        library.spells[noun].use_spell()

    verbs = {'hello': say_hi, 'hi': say_hi, 'help': help_command,
    'restart': restart, 'look': library.player.location.describe,
    'inventory': library.player.inventory_check,
    'i': library.player.inventory_check, 'save': save, 'load': load,
    'spells': library.player.spell_check, 'teleport': library.player.teleport,
    'examine': examine, 'take': take, 'drop': drop, 'open': read, 'read': read,
    'cast': cast}

    try: verbs[verb]()
    except:
        #sys.exit() doesn't work within a try.
        if verb == 'exit' or verb == 'quit': sys.exit()
        #is there a way to put the part below in the dictionary as well? would
        #have to nest dictionaries, which gave me an unhashable type error.
        if verb in moves: library.player.move(moves[verb])
        else: print 'I\'m sorry, I don\'t understand that command. Try typing "help" if you need some guidance.'

