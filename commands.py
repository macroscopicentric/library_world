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

arts_and_preps = ['to', 'the', 'a', 'an', 'with']

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
        print '''My commands are like a traditional text adventure\'s. To move, use
cardinal or ordinal directions or "up" and "down". Other commands you can use:
* "look", "l", or "z" (describes the room to you)
* "examine [object]" or "x [object]"
* "inventory" or "i" (lists your inventory)
* "take [object]" or "take all"
* "drop [object]" or "drop all"
* "give [object] (to) [person]"
* "cast [Charter spell]"
* "spells" (lists the spells you know)
* "teleport" (sends you back to the Reading Room, or the labyrinth stairs if
    you're in the labyrinth)
* "talk (to) [character]"
* "break [object]" or "cut [object]"
* "read [book]" or "open [book]"
* "shelve [book]"
* "exit" or "quit" (exits the game)
* "restart" (restarts the game)

Please keep in mind that commands and people names can only be one word, but
direct objects can be more than one. Don't bother with articles (the, a, an,
etc).'''

    #Easter Eggs
    def say_hi():
        print "Hullo!"

    def swear():
        responses = ["Do you kiss your mother with that mouth?!",
        "That's not appropriate vocabulary for an adventurer."]
        print responses[random.randint(0, len(responses) - 1)]

    def zork():
        print "At your service!"

    def xyzzy():
        print 'A hollow voice says, "fool."'

    #Actual commands
    def examine():
        items.item_list[direct_object].examine()

    def take():
        if direct_object == 'all':
            if player.location.inventory:
                temp = player.location.inventory[:]
                for item in temp:
                    items.item_list[item].take(player.location)
            else: print "There's nothing here to take."
        elif direct_object == 'book':
            print "I need something more specific. What book do you want me to take?"
        else:
            try: items.item_list[direct_object].take(player.location)
            except: print "I don't see that item."

    def drop():
        if direct_object == 'all':
            if player.inventory:
                temp = player.inventory[:]
                for item in temp:
                    items.item_list[item].drop(player.location)
            else: player.inventory_check()
        elif direct_object == 'book':
            print "I need something more specific. What book do you want me to drop?"
        else:
            try: items.item_list[direct_object].drop(player.location)
            except: print "You're not carrying that item."

    def break_thing():
        if (direct_object == 'seal' or
            direct_object == 'rope') and player.location_test(hall15):
            if player.invent_test('wire'):
                print '''You carefully peel Vancelle's seal off of the rope at both ends
using the piece of wire. You set the rope and seals in the corner.'''
                rooms.restricted.unlock()
                player.location.add_counter()
            elif player.invent_test('scissors'):
                print '''As you poise the scissors to cut through the rope, Madam Pince
appears seemingly out of nowhere, screeching at the top of her lungs. "WHAT DO
YOU THINK YOU'RE DOING?! Disrespecting library property! Out out out!" She
promptly confiscates all your books, and to add insult to injury, she escorts
you all the way back to the main reading room.'''
                for item in player.inventory:
                    if 'book' in item:
                        items.item_list[item].drop(rooms.restricted)
                player.teleport()
        else:
            if direct_object in items.item_list:
                print '''You try to break the %s, but it just bounces off the wall.
Disgusted, you put it back.''' % (direct_object)
            else: print '''It would take super-human strength to break that.
Spoiler: you're not super-human.'''

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
        try:
            #if direction in rooms.self.location.directions and...:
            #     print "That opening is too small for a full-sized person. Perhaps something smaller, like a cat or otter, could get through."
            #need a way to ID a DOOR (as opposed to a room, which I did for the locked rooms above),
            #since a door goes both ways and a key is one-time in one direction.
            if moves[verb] == 'd' and (player.location_test(rooms.uu_library1) or
                player.location_test(rooms.uu_library2)):
                print '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
and down is up. But now it's gone, so you don't trouble yourself over it.\n'''
                time.sleep(3)
                player.move(moves[verb])
            else: player.move(moves[verb])
        except: print "You can't go that way, stupid."


    verbs = {'hello': say_hi, 'hi': say_hi, 'help': help_command,
    'look': player.location.describe, 'z': player.location.describe,
    'l': player.location.describe,
    'inventory': player.inventory_check, 'xyzzy': xyzzy, 'zork': zork,
    'i': player.inventory_check, 'spells': player.spell_check,
    'teleport': player.teleport, 'x': examine, 'take': take,
    'examine': examine, 'drop': drop, 'restart': restart, 'read': read,
    'open': read, 'save': save, 'load': load, 'shelve': shelve, 'cast': cast,
    'talk': talk, 'fuck': swear, 'damn': swear, 'shit': swear, 'give': give,
    'cut': break_thing, 'break': break_thing}

    try:
        verbs[verb]()
    except:
        #sys.exit() doesn't work within a try.
        if verb == 'exit' or verb == 'quit': sys.exit()
        #is there a way to put the part below in the dictionary as well? created
        #a tuple from the keys but then it's NESTED and the search (try above) only
        #goes one level deep.
        elif verb in moves.keys(): move()
        else: print 'I\'m sorry, I don\'t understand that command. Try typing "help" if you need some guidance.'

