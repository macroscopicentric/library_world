import sys
import pickle
import random

from rooms import directory
from items import item_list
from people import npc_list
import spells

#Not sure how to implement this:
# game_state = {
#     rooms: the_rooms,
#     player: the_player
# }

moves = {'u': 'u', 'up': 'u', 'd': 'd', 'down': 'd', 'n': 'n', 'north': 'n',
'e': 'e', 'east': 'e', 'w': 'w', 'west': 'w', 's': 's', 'south': 's',
'northwest': 'nw', 'nw': 'nw', 'southwest': 'sw', 'sw': 'sw',
'southeast': 'se', 'se': 'se', 'northeast': 'ne', 'ne': 'ne'}

arts_and_preps = ['to', 'the', 'a', 'an', 'with']

def input_format(user_input):
    user_input = user_input.lower().split(" ", 1)

    if "." in user_input[-1]:
        detail = user_input.pop().split(".").pop(0)
        user_input.append(detail)

    #allows splitting for compound sentences ("give __ to __") while still
    #retaining book items as one word.
    if len(user_input) > 1:
        if 'book' in user_input[1]:
            user_input = [user_input[0]] + user_input[1].split('book ', 1)
            try:
                user_input = user_input[0:2] + user_input[2].split(' ')
            except:
                pass
        elif 'waistcoat' in user_input[1]:
            pass
        else:
            user_input = [user_input[0]] + user_input[1].split(' ')

    #removing articles/prepositions from user input:
    for word in arts_and_preps:
        if word in user_input:
            user_input.remove(word)

    return user_input

#def command(user_input, player, play) to allow restart/load
def command(user_input, player):
    verb = user_input[0]
    if len(user_input) > 1: direct_object = user_input[1]
    if len(user_input) > 2: indirect_object = user_input[2]

    #Helper functions so I can add all methods to the verbs dictionary:
    #save/load/restart not currently working
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
        return "File saved."

    def load():
        print "What's the file name?"
        save_name = input_format()[0] + '.txt'
        #how to search for file, so it doesn't try to open a non-existent file?
        #Alan's suggestion, to pull from the game state dict at top:
        #game_state.player = pickle.load(thePcileFile.txt)
        with open(save_name, 'rb') as save_file:
            player = pickle.load(save_file)
            rooms.directory = pickle.load(save_file)
        play()

    def restart():
        print "Are you sure you want to restart? Y/N"
        user_input = verbs_list.input_format()
        if user_input == "y" or user_input == "yes":
            play()
        elif user_input == "n" or user_input == "no":
            pass
        else:
            return 'I\'m sorry, I don\'t understand that command.'

    def help_command():
        return {'header':'''My commands are like a traditional text adventure\'s.
To move, use cardinal or ordinal directions or "up" and "down". Other commands
you can use:''', 'text': ['* "look", "l", or "z" (describes the room to you)',
'* "examine [object]" or "x [object]"',
'* "inventory" or "i" (lists your inventory)',
'* "take [object]" or "take all"',
'* "drop [object]" or "drop all"',
'* "give [object] (to) [person]"',
'* "cast [Charter spell]"',
'* "spells" (lists the spells you know)',
'''* "teleport" (sends you back to the Reading Room, or the labyrinth stairs if
    you're in the labyrinth)''',
'* "talk (to) [character]"',
'* "break [object]" or "cut [object]"',
'* "read [book]" or "open [book]"',
'* "shelve [book]"',
'''* "level" (tells you what level you are and what books you've already shelved)''',
'* "exit" or "quit" (exits the game)',
'* "restart" (restarts the game)', '',
'''Please keep in mind that commands and people names can only be one word, but
direct objects can be more than one. You don't need articles (the, a, an, etc).''']}

    #Easter Eggs
    def say_hi():
        return "Hullo!"

    def swear():
        responses = ["Do you kiss your mother with that mouth?!",
        "That's not appropriate vocabulary for an adventurer."]
        return responses[random.randint(0, len(responses) - 1)]

    def zork():
        return "At your service!"

    def xyzzy():
        return 'A hollow voice says, "fool."'

    #Actual commands
    def examine():
        return item_list[direct_object].examine()

    def inventory():
        return player.inventory_check()

    def take():
        if direct_object == 'all':
            if directory[player.location].inventory:
                temp = directory[player.location].inventory[:]
                item_pickup = {'text': []}
                for item in temp:
                    item_pickup['text'] += [item_list[item].take(directory[player.location])]
                return item_pickup
            else:
                return "There's nothing here to take."
        elif direct_object == 'book':
            return "I need something more specific. Which book do you want me to take?"
        else:
            try:
                return item_list[direct_object].take(directory[player.location])
            except:
                return "I don't see that item."

    def drop():
        if direct_object == 'all':
            if player.inventory:
                temp = player.inventory[:]
                item_drop = {'text': []}
                for item in temp:
                    item_drop['text'] += [item_list[item].drop(directory[player.location])]
                return item_drop
            else:
                return player.inventory_check()
        elif direct_object == 'book':
            return "I need something more specific. What book do you want me to drop?"
        else:
            try:
                return item_list[direct_object].drop(directory[player.location])
            except:
                return "You're not carrying that item."

    def break_thing():
        if direct_object in ['seal', 'rope'] and player.location_test('hall15'):
            if player.invent_test('wire'):
                directory['restricted'].unlock()
                directory[player.location].add_counter()
                return '''You carefully peel Vancelle's seal off of the rope at both ends
using the piece of wire. You set the rope and seals in the corner.'''
            elif player.invent_test('scissors') or player.invent_test('dagger'):
                temp = player.inventory[:]
                for item in temp:
                    if 'book' in item or 'diary' == item:
                        item_list[item].drop(directory['restricted'])
                message = player.teleport()
                message['event'] = '''As you poise to cut through the rope, Madam Pince
appears seemingly out of nowhere, screeching at the top of her lungs. "WHAT DO
YOU THINK YOU'RE DOING?! Disrespecting library property! Out out out!" She
promptly confiscates all your books, and to add insult to injury, she escorts
you all the way back to the main reading room.'''
                return message
        else:
            if direct_object in item_list:
                return '''You try to break the %s, but it just bounces off the wall.
Disgusted, you put it back.''' % (direct_object)
            else:
                return '''It would take super-human strength to break that.
Spoiler: you're not super-human.'''

    def give():
        try:
            return item_list[direct_object].give(npc_list[indirect_object],
                item_list['key'])
        except:
            return '''I didn't quite get that. Did you use the format "give
[object] to [person]"?'''

    def read():
        if direct_object == 'book':
            return 'Which book?'
        else:
            try:
                return item_list[direct_object].open()
            except:
                return "You can't read that. Try reading a book."

    def shelve():
        try:
            return item_list[direct_object].shelve()
        except:
            return "You can't shelve that."

    def cast():
        spells.spells[direct_object].use_spell()

    def level_check():
        message = {'header': (("You are level %s. " % (player.level)) +
            "You have shelved these books:"), 'text': []}
        for book in player.shelved_books:
            message['text'] += [book]
        return message

    def talk():
        if directory[player.location].npc == direct_object:
            return npc_list[direct_object].talk(player)
        else:
            return "I don't see that person here."

    def look():
        return directory[player.location].describe()

    def move():
        # try:
            #if direction in rooms.self.location.directions and...:
            #     print "That opening is too small for a full-sized person.
            #Perhaps something smaller, like a cat or otter, could get through."
            #need a way to ID a DOOR (as opposed to a room, which I did for the locked rooms above),
            #since a door goes both ways and a key is one-time in one direction.
        if moves[verb] == 'd' and (player.location_test('uu_library1') or
            player.location_test('uu_library2')):
            action = player.move(moves[verb])
            action['event'] = '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
and down is up. But now it's gone, so you don't trouble yourself over it.'''
            return action
        else:
            return player.move(moves[verb])
        # except:
        #     return "You can't go that way, stupid."


    verbs = {'hello': say_hi, 'hi': say_hi, 'help': help_command,
    'look': look, 'z': look, 'l': look, 'inventory': inventory, 'xyzzy': xyzzy,
    'zork': zork, 'i': inventory, 'spells': player.spell_check,
    'teleport': player.teleport, 'x': examine, 'take': take, 'level': level_check,
    'examine': examine, 'drop': drop, 'restart': restart, 'read': read,
    'open': read, 'save': save, 'load': load, 'shelve': shelve, 'cast': cast,
    'fuck': swear, 'damn': swear, 'shit': swear, 'give': give, 'talk': talk,
    'cut': break_thing, 'break': break_thing}

    try:
        return verbs[verb]()
    except:
        #sys.exit() doesn't work within a try.
        if verb == 'exit' or verb == 'quit':
            sys.exit()
        #is there a way to put the part below in the dictionary as well? created
        #a tuple from the keys but then it's NESTED and the search (try above) only
        #goes one level deep.
        elif verb == 'talk':
            return talk()
        elif verb in moves.keys():
            output = move()
            if ('banana' in directory['hall15'].inventory and
                    directory[player.location].check_banana):
                output['event'] = directory[player.location].go_to_hospital()
                return output
            else:
                return output
        else:
            return 'I\'m sorry, I don\'t understand that command. Try typing "help" if you need some guidance.'

