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
'northwest': 'nw', 'nw': 'nw', 'southwest': 'sw', 'sw': 'sw',
'southeast': 'se', 'se': 'se', 'northeast': 'ne', 'ne': 'ne'}

arts_and_preps = ['to', 'the', 'a', 'an']

def input_format():
    user_input = raw_input(">").lower().split(" ", 1)

    if "." in user_input[-1]:
        detail = user_input.pop().split(".").pop(0)
        user_input.append(detail)

    #allows splitting for compound sentences ("give __ to __") while still
    #retaining book items as one word.
    if len(user_input) > 1:
        if 'book' in user_input[1]:
            user_input = [user_input[0]] + user_input[1].split('book ', 1)
            try: user_input = user_input[0:2] + user_input[2].split(' ')
            except: pass
        else:
            user_input = [user_input[0]] + user_input[1].split(' ')

    for word in arts_and_preps:
        if word in user_input:
            user_input.remove(word)

    return user_input

def command(user_input, player, game):
    # print user_input

    verb = user_input[0]
    if len(user_input) > 1: direct_object = user_input[1]
    if len(user_input) > 2: indirect_object = user_input[2]

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
        print '''My commands are like a traditional text adventure\'s. To move,
use cardinal or ordinal directions or "up" and "down". Other commands you can
use: "look" (describes the room to you), "examine [object]", "inventory" or "i"
(lists your inventory), "take [object]" or "take all", "drop [object]" or "drop
all", "give [object] (to) [person]", "cast [Charter spell]", "spells" (lists
the spells you know), "teleport" (sends you back to the Reading Room, or the
labyrinth stairs if you're in the labyrinth), "talk (to) [character]",
"read [book]" or "open [book]", "shelve [book]", "exit" or "quit" (exits the
game), or "restart" (restarts the game).

Please keep in mind that commands and people names can only be one word, but
direct objects can be more than one. Don't bother with articles (the, a, an,
etc).'''

    #Easter Eggs
    def say_hi():
        print "Hullo!"

    def break_thing():
        pass

    def swear():
        responses = ["Do you kiss your mother with that mouth?!",
        "That's not appropriate vocabulary for an adventurer."]
        print responses[random.randint(0, len(responses) - 1)]

    def zork():
        print "At your service!"

    def xyzzy():
        print 'A hollow voice says, "fool."'

    def examine():
        items.item_list[direct_object].examine()

    def take():
        if direct_object == 'all':
            if player.location.inventory:
                temp = player.location.inventory[:]
                for item in temp:
                    items.item_list[direct_object].take(player.location)
            else: print "There's nothing here to take."
        else:
            try: items.item_list[direct_object].take(player.location)
            except: print "I don't see that item."

    def drop():
        if direct_object == 'all':
            if player.inventory:
                temp = player.inventory[:]
                for item in temp:
                    items.item_list[direct_object].drop(player.location)
            else: player.inventory_check()
        else:
            try: items.item_list[direct_object].drop(player.location)
            except: print "You're not carrying that item."

    def give():
        try:
            items.item_list[direct_object].give(people.npc_list[indirect_object])
        except: print '''I didn't quite get that. Did you use the format "give
[object] to [person]"?'''

    def read():
        if direct_object == 'book':
            print 'Which book?'
        else:
            try: items.item_list[direct_object].open()
            except: print "You can't read that. Try reading a book."

    def shelve():
        try: items.item_list[direct_object].shelve(player.location)
        except: print "You can't shelve that."

    def cast():
        spells.spells[direct_object].use_spell()

    def talk():
        if player.location.npc == direct_object:
            if direct_object == 'vancelle':
                people.vancelle.talk(player)
            else: people.npc_list[direct_object].talk(player)
        else: print "I don't see that person here."

    def move():
        new_direction = player.location.directions[direction]

        try:
            #if direction in rooms.self.location.directions and...:
            #     print "That opening is too small for a full-sized person. Perhaps something smaller, like a cat or otter, could get through."
            #need a way to ID a DOOR (as opposed to a room, which I did for the locked rooms above),
            #since a door goes both ways and a key is one-time in one direction.
            if new_direction.lock_test:
                print new_direction.lock_desc
                if new_direction == rooms.restricted:
                    for item in player.inventory:
                        if 'book' in item:
                            items.item_list[item].drop(rooms.restricted)
                    player.teleport()
            elif moves[verb] == 'd' and (player.location_test(rooms.uu_library1) or
                player.location_test(rooms.uu_library2)):
                print '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
and down is up. But now it's gone, so you don't trouble yourself over it.'''
                print
                time.sleep(3)
                print player.move(moves[verb])
            else: print player.move(moves[verb])
        except: print "You can't go that way, stupid."


    verbs = {'hello': say_hi, 'hi': say_hi, 'help': help_command,
    'look': player.location.describe, 'z': player.location.describe,
    'l': player.location.describe,
    'inventory': player.inventory_check, 'xyzzy': xyzzy, 'zork': zork,
    'i': player.inventory_check, 'spells': player.spell_check,
    'teleport': player.teleport, 'x': examine, 'take': take,
    'examine': examine, 'drop': drop, 'restart': restart, 'read': read,
    'open': read, 'save': save, 'load': load, 'shelve': shelve, 'cast': cast,
    'talk': talk, 'fuck': swear, 'damn': swear, 'shit': swear, 'give': give}

    try:
        verbs[verb]()
    except:
        #sys.exit() doesn't work within a try.
        if verb == 'exit' or verb == 'quit': sys.exit()
        #is there a way to put the part below in the dictionary as well? would
        #have to nest dictionaries, which gave me an unhashable type error.
        elif verb in moves: self.move(moves[verb])
        else: print 'I\'m sorry, I don\'t understand that command. Try typing "help" if you need some guidance.'

