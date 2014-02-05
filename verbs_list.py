import items

moves = {'u': 'u', 'up': 'u', 'd': 'd', 'down': 'd', 'n': 'n', 'north': 'n', 'e': 'e', 'east': 'e',
'w': 'w', 'west': 'w', 's': 's', 'south': 's', 'northwest': 'nw', 'nw': 'nw', 'southwest': 'sw',
'sw': 'sw', 'southeast': 'se', 'se': 'se', 'northeast': 'ne', 'ne': 'ne'}

def command(user_input):
    import library
    verb = user_input[0]
    noun = ''
    if len(user_input) == 2: noun = user_input[1]
    elif len(user_input) > 2: print "Whoops! That's too challenging for me. Please try again."

    #For testing legit nouns:
    nouns = library.spells.keys() + items.item_list.keys()

    #Helper functions so I can add all methods to the verbs dictionary:
    def save():
        #Currently saves/loads player's location and sets correct item locations.
        #Doesn't save other player/room status info (alive/dead, opened doors, etc).
        print "Save file name:"
        save_name = library.game.input_format()[0] + '.txt'
        #can i ask about overwriting a previous save file?
        with open(save_name, 'wb') as save_file:
            pickle.dump(library.player.location, save_file)
            pickle.dump(items.item_list, save_file)
        #recommended by Dive Into Python 3 (excellent explanation of serialization and how to use pickle).
        #with open() ensures that the file is closed. Pickle only reads/writes binary, so 'wb' is needed.
        print "File saved."

    def load():
        print "What's the file name?"
        save_name = library.game.input_format()[0] + '.txt'
        #how to search for file, so it doesn't try to open a non-existant file?
        with open(save_name, 'rb') as save_file:
            library.player.location = pickle.load(save_file)
            items.item_list = pickle.load(save_file)
        library.game.start()

    def help_command():
        print '''My commands are like a traditional text adventure\'s. To move, use the cardinal directions ("n", "s", "e", or "w")
or "up" and "down". Other commands you can use: "look" (describes the room to you), "examine [object]", "inventory"
or "i" (lists your inventory), "take [object]", "drop [object]", "cast [Charter spell]", "spells" (lists the
spells you know), "teleport" (sends you back to the Reading Room, or the labyrinth stairs if you're in the labyrinth),
"talk [character]", "exit" or "quit" (exits the game), or "restart" (restarts the game).'''

    def restart():
        print "Are you sure you want to restart? Y/N"
        user_input = library.game.input_format()
        if "y" or "yes":
            library.game.start()
        elif "n" or "no": library.game.play()
        else: print 'I\'m sorry, I don\'t understand that command.'

    def say_hi():
        print "Hullo!"

    def examine():
        items.item_list[noun].examine()

    def take():
        if noun == 'all':
            if library.player.location.inventory:
                temp = library.player.location.inventory[:]
                for item in temp:
                    items.item_list[item].take()
            else: print "There's nothing here to take."
        else:
            try: items.item_list[noun].take()
            except: print "I don't see that item."

    def drop():
        if noun == 'all':
            if library.player.inventory:
                temp = library.player.inventory[:]
                for item in temp:
                    items.item_list[item].drop()
            else: library.player.inventory_check()
        else:
            try: items.item_list[noun].drop()
            except: print "I don't see that item."

    def read():
        try: items.item_list[noun].open()
        except: print "You can't read that. Try reading a book."

    def cast():
        library.spells[noun].use_spell()

    verbs = {'hello': say_hi, 'hi': say_hi, 'help': help_command,'restart': restart,
    'look': library.player.location.describe, 'inventory': library.player.inventory_check, 'i': library.player.inventory_check,
    'save': save, 'load': load, 'spells': library.player.spell_check, 'teleport': library.player.teleport,
    'examine': examine, 'take': take, 'drop': drop, 'open': read, 'read': read, 'cast': cast}

    try: verbs[verb]()
    except:
        #sys.exit() doesn't work within a try.
        if verb == 'exit' or verb == 'quit': sys.exit()
        #is there a way to put the part below in the dictionary as well? would have to nest dictionaries, which gave me an unhashable type error.
        if verb in moves: library.player.move(moves[verb])
        else: print 'I\'m sorry, I don\'t understand that command. Try typing "help" if you need some guidance.'

