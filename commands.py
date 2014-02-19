import sys
import pickle
import random

import items
import people
import rooms
import spells

#I really like that the HP text adventure has a thesaurus. How do I make one?

moves = {'u': 'u', 'up': 'u', 'd': 'd', 'down': 'd', 'n': 'n', 'north': 'n',
'e': 'e', 'east': 'e', 'w': 'w', 'west': 'w', 's': 's', 'south': 's',
'northwest': 'nw', 'nw': 'nw', 'southwest': 'sw', 'sw': 'sw', 'southeast': 'se',
'se': 'se', 'northeast': 'ne', 'ne': 'ne'}

def input_format():
    user_input = raw_input(">").lower().split(" ", 1)

    if "." in user_input[-1]:
        detail = user_input.pop().split(".").pop(0)
        user_input.append(detail)

    return user_input

def command(user_input, player, game):
    verb = user_input[0]
    noun = ''
    if len(user_input) > 1: noun = user_input[1]

    #Helper functions so I can add all methods to the verbs dictionary:
    def save():
        #Currently saves/loads player's location and sets correct item locations.
        #Doesn't save other player/room status info (alive/dead, opened doors, etc).
        print "Save file name:"
        save_name = input_format()[0] + '.txt'
        #can i ask about overwriting a previous save file?
        with open(save_name, 'wb') as save_file:
            pickle.dump(player, save_file)
            pickle.dump(rooms.directory, save_file)
        #recommended by Dive Into Python 3 (excellent explanation of
        #serialization and how to use pickle).
        #with open() ensures that the file is closed. Pickle only reads/writes
        #binary, so 'wb' is needed.
        print "File saved."

    def load():
        print "What's the file name?"
        save_name = input_format()[0] + '.txt'
        #how to search for file, so it doesn't try to open a non-existent file?
        with open(save_name, 'rb') as save_file:
            player = pickle.load(save_file)
            rooms.directory = pickle.load(save_file)
        game.start()

    def restart():
        print "Are you sure you want to restart? Y/N"
        user_input = verbs_list.input_format()
        if user_input == "y" or user_input == "yes":
            game.start()
        elif user_input == "n" or user_input == "no": game.play()
        else: print 'I\'m sorry, I don\'t understand that command.'

    def help_command():
        print '''My commands are like a traditional text adventure\'s. To move, use cardinal or ordinal directions
or "up" and "down". Other commands you can use: "look" (describes the room to you), "examine [object]", "inventory"
or "i" (lists your inventory), "take [object]" or "take all", "drop [object]" or "drop all", "cast [Charter spell]",
"spells" (lists the spells you know), "teleport" (sends you back to the Reading Room, or the labyrinth
stairs if you're in the labyrinth), "talk [character]", "read [book]" or "open [book]", "shelve [book]",
"exit" or "quit" (exits the game), or "restart" (restarts the game).

Please keep in mind that commands can only be one word, but nouns can be more than one. Don't bother with
articles (the, a, an, etc).'''

    #Easter Eggs
    def say_hi():
        print "Hullo!"

    def break_thing():
        pass

    def swear():
        responses = ["Do you kiss your mother with your mouth?!",
        "That's not appropriate vocabulary for an adventurer."]
        print responses[random.randint(0, len(responses) - 1)]

    def zork():
        print "At your service!"

    def xyzzy():
        print 'A hollow voice says "fool."'

    def examine():
        items.item_list[noun].examine()

    def take():
        if noun == 'all':
            if player.location.inventory:
                temp = player.location.inventory[:]
                for item in temp:
                    items.item_list[item].take(player.location.inventory)
            else: print "There's nothing here to take."
        else:
            try: items.item_list[noun].take(player.location.inventory)
            except: print "I don't see that item."

    def drop():
        if noun == 'all':
            if player.inventory:
                temp = player.inventory[:]
                for item in temp:
                    items.item_list[item].drop(player.location.inventory)
            else: player.inventory_check()
        else:
            try: items.item_list[noun].drop(player.location.inventory)
            except: print "You're not carrying that item."

    def read():
        if noun == 'book':
            print 'Which book?'
        else:
            try: items.item_list[noun].open()
            except: print "You can't read that. Try reading a book."

    def shelve():
        try: items.item_list[noun].shelve(player.location)
        except: print "You can't shelve that."

    def cast():
        spells.spells[noun].use_spell()

    def talk():
        if player.location.npc == noun:
            if noun == 'vancelle':
                people.vancelle.talk(player)
            else: people.npc_list[noun].talk()
        else: print "I don't see that person here."

    verbs = {'hello': say_hi, 'hi': say_hi, 'help': help_command,
    'look': player.location.describe, 'z': player.location.describe,
    'inventory': player.inventory_check, 'xyzzy': xyzzy, 'zork': zork,
    'i': player.inventory_check, 'spells': player.spell_check,
    'teleport': player.teleport, 'x': examine, 'take': take, 'examine': examine,
    'drop': drop, 'restart': restart, 'read': read, 'open': read,
    'save': save, 'load': load, 'shelve': shelve, 'cast': cast, 'talk': talk}

    try:
        verbs[verb]()
    except:
        #sys.exit() doesn't work within a try.
        if verb == 'exit' or verb == 'quit': sys.exit()
        #is there a way to put the part below in the dictionary as well? would
        #have to nest dictionaries, which gave me an unhashable type error.
        elif verb in moves: player.move(moves[verb])
        else: print 'I\'m sorry, I don\'t understand that command. Try typing "help" if you need some guidance.'

