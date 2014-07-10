import random

moves = {'u': 'u', 'up': 'u', 'd': 'd', 'down': 'd', 'n': 'n', 'north': 'n',
'e': 'e', 'east': 'e', 'w': 'w', 'west': 'w', 's': 's', 'south': 's',
'northwest': 'nw', 'nw': 'nw', 'southwest': 'sw', 'sw': 'sw',
'southeast': 'se', 'se': 'se', 'northeast': 'ne', 'ne': 'ne'}

#def command(user_input, player, play) to allow restart/load
def command(user_input, game):
    player = game.player_state
    item_list = game.item_list
    directory = game.directory
    npc_list = game.npc_list
    spells = game.spells

    verb = user_input[0]
    if len(user_input) > 1: direct_object = user_input[1]
    if len(user_input) > 2: indirect_object = user_input[2]

    #Helper functions so I can add all methods to the verbs dictionary:
    def help_command():
        return {'header':'''My commands are like a traditional text adventure\'s.
To move, use cardinal or ordinal directions or "up" and "down". Other commands
you can use:''', 'text': ['* "look", "l", or "z" (describes the room to you)',
'* "examine [object]" or "x [object]"',
'* "inventory" or "i" (lists your inventory)',
'* "take [object]" or "take all"',
'* "drop [object]" or "drop all"',
'* "give [object]" (to) [person]"',
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

    #Actual Commands
    def examine():
        return item_list[direct_object].examine(game,
            directory[player['location']])

    def inventory():
        return game.inventory_check()

    def take():
        if direct_object == 'all':
            if directory[player['location']].inventory:
                temp = directory[player['location']].inventory[:]
                item_pickup = {'text': []}
                for item in temp:
                    item_pickup['text'] += [item_list[item].take(game,
                        directory[player['location']])]
                return item_pickup
            else:
                return "There's nothing here to take."
        elif direct_object == 'book':
            return "I need something more specific. Which book do you want me to take?"
        else:
            try:
                return item_list[direct_object].take(game,
                    directory[player['location']])
            except:
                return "I don't see that item."

    def drop():
        if direct_object == 'all':
            if player['inventory']:
                temp = player['inventory'][:]
                item_drop = {'text': []}
                for item in temp:
                    item_drop['text'] += [item_list[item].drop(game,
                        directory[player['location']])]
                return item_drop
            else:
                return game.inventory_check()
        elif direct_object == 'book':
            return "I need something more specific. What book do you want me to drop?"
        else:
            try:
                return item_list[direct_object].drop(game,
                    directory[player['location']])
            except:
                return "You're not carrying that item."

    def break_thing():
        if direct_object in ['seal', 'rope'] and game.location_test('hall15'):
            if game.invent_test('wire'):
                directory['restricted'].unlock()
                directory['hall15'].add_counter()
                return '''You carefully peel Vancelle's seal off of the rope at both ends
using the piece of wire. You set the rope and seals in the corner.'''
            elif game.invent_test('dagger'):
                temp = player['inventory'][:]
                for item in temp:
                    if ('book' in item and item != "translation book") or item == 'diary':
                        item_list[item].drop(game, directory['restricted'])
                message = game.teleport()
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
        if indirect_object == directory[player['location']].npc:
            if direct_object in player['inventory']:
                return npc_list[indirect_object].wish_fulfillment(game, direct_object)
            else:
                return "You're not carrying that!"
        else:
            return "That person isn't here!"

    def read():
        if direct_object == 'book':
            return 'Which book?'
        else:
            try:
                return item_list[direct_object].open(game,
                    player['inventory'])
            except:
                return "You can't read that. Try reading a book."

    def shelve():
        try:
            return item_list[direct_object].shelve(game,
                directory[player['location']])
        except:
            return "You can't shelve that."

    def cast():
        return spells[direct_object].use_spell(game, player, directory)

    def level_check():
        message = {'header': (("You are level %s. " % (player['level']))
            + "You have shelved these books:"), 'text': []}
        if not player['shelved_books']:
            message['text'] += ["Fail. You haven't shelved any books!"]
            return message
        for book in player['shelved_books']:
            message['text'] += [book]
        return message

    def talk():
        if directory[player['location']].npc == direct_object:
            return npc_list[direct_object].talk(game, player)
        else:
            return "I don't see that person here."

    def look():
        return directory[player['location']].describe()

    def move():
        try:
            #if direction in rooms.self.location.directions and...:
            #     print "That opening is too small for a full-sized person.
            #Perhaps something smaller, like a cat or otter, could get through."
            #need a way to ID a DOOR (as opposed to a room, which I did for the locked rooms above),
            #since a door goes both ways and a key is one-time in one direction.
            if moves[verb] == 'd' and (game.location_test('uu_library1') or
                game.location_test('uu_library2')):
                directory['uu_library1'].add_counter()
                action = game.move(moves[verb])
                action['event'] = '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
and down is up. But now it's gone, so you don't trouble yourself over it.'''
                return action
            else:
                return game.move(moves[verb])
        except:
            return "You can't go that way, stupid."


    verbs = {'hello': say_hi, 'hi': say_hi, 'help': help_command,
    'look': look, 'z': look, 'l': look, 'inventory': inventory, 'xyzzy': xyzzy,
    'zork': zork, 'i': inventory, 'spells': game.spell_check,
    'teleport': game.teleport, 'x': examine, 'take': take, 'level': level_check,
    'examine': examine, 'drop': drop, 'read': read,
    'open': read, 'shelve': shelve, 'cast': cast,
    'fuck': swear, 'damn': swear, 'shit': swear, 'give': give, 'talk': talk,
    'cut': break_thing, 'break': break_thing}

    try:
        return verbs[verb]()
    except:
        #is there a way to put the part below in the dictionary as well? created
        #a tuple from the keys but then it's NESTED and the search (try above) only
        #goes one level deep.
        if verb in moves.keys():
            output = move()
            if ('banana' in directory['hall15'].inventory and
                    directory[player['location']].check_banana):
                output['event'] = directory[player['location']].go_to_hospital(directory)
                return output
            else:
                return output
        else:
            return 'I\'m sorry, I don\'t understand that command. Try typing "help" if you need some guidance.'

