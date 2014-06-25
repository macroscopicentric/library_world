import json
import sys

from game import Game, simplify, reconstitute, home
from commands import command

def save(game, save_name):
    try:
        json_dict = simplify(game)
        json.dump(json_dict, open((save_name + '.txt'), 'w'), separators=(',', ':'))
        return "File saved."
    except:
        return '''I didn't understand that. Did you use the format "save [filename]?"'''

def load(game, save_name):
    try:
        json_dict = json.load(open(save_name + '.txt'))
        game = Game()
        game = reconstitute(json_dict)
        new_game_output = {'event': 'Loading...'}
        new_game_output += game.directory[game.player_state['location']].describe()
        return new_game_output
    except: return '''I didn't understand that. Did you use the format "load [filename]?"'''

def restart(game):
    new_game_output = {'event': 'Restarting...'}
    game = Game()
    new_game_output += game.directory[game.player_state['location']].describe()
    return new_game_output


#Helper function that takes user input and returns parsed list.
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
        elif 'waistcoat' in user_input[1]: #Can't give waistcoat like this.
            pass
        else:
            user_input = [user_input[0]] + user_input[1].split(' ')

    #removing articles/prepositions from user input:
    arts_and_preps = ['to', 'the', 'a', 'an', 'with']
    for word in arts_and_preps:
        if word in user_input:
            user_input.remove(word)

    return user_input

#Helper function for terminal/flask repeating code.
def play_game(user_input):
    player_response = input_format(user_input)
    if player_response[0] == 'load':
        return load(game, player_response[1])
    elif player_response[0] == 'save':
        return save(game, player_response[1])
    elif player_response[0] == 'restart':
        return restart(game)
    elif player_response[0] in ['exit', 'quit']:
        #Need softer exit here.
        sys.exit()
    else:
        return command(player_response, game)

def from_terminal_play():
    game = Game()
    print terminal_formatting(game.directory[game.player_state['location']].describe())
    while True:
        print terminal_formatting(play_game(raw_input('>')))


def terminal_formatting(output):
    #Two possible outputs: unicode/string or a dictionary.
    if isinstance(output, basestring):
        return output

    description = output['text'][0]
    if len(output['text']) > 1:
        for item in output['text'][1:]:
            description += '\n' + item

    formatted_output = ''
    if 'event' in output.keys():
        formatted_output += output['event'] + '\n\n'
    if 'header' in output.keys():
        formatted_output += output['header'] + '\n\n'

    formatted_output += description

    if 'inventory' in output.keys():
        formatted_output += '\n\n' + output['inventory']
    if 'npc' in output.keys() and 'inventory' in output.keys():
        formatted_output += '\n' + output['npc']
    elif 'npc' in output.keys() and 'inventory' not in output.keys():
        formatted_output += '\n\n' + output['npc']

    return formatted_output

def start_web():
    game = Game()
    return (game.directory[game.player_state['location']].describe(),
        game.directory[game.player_state['location']].name, game)

def play_web(flask_input, game):
    return (play_game(flask_input),
        game.directory[game.player_state['location']].name)

if __name__ == "__main__":
    game = Game()
    from_terminal_play()

#To do:
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)
#Add in more Clayr hallway landmarks as I add other libraries.
#Add Dream's library?, DW, Ghostbusters?
#Levels 1-3, 4-5, 6 >> third, second, first. Second and first get new offices with new books (so access to new spells).
#Remove some of the circularity? Commands go everywhere and branch into multiple modules.
#How to unlock finis Africae?
#End game: promoted to level 7, Vancelle gives you the charter book that allows you to turn into an otter,
#   so you can slip through the crack and find the pipes, crown, and trowel.
#Add NV Librarians, banana peel for Madame Pince, Vashta Nerada, Ghostbusters ghost, Stilken?
#Allow interactions with book/waistcoat just by "book"/"waistcoat" if there's only one.
#Do anything with disreputable dog statue?
#Move archbishop book to DW library.
#Pay attention to HTML headers in web app template, need to be HTML/JSON for jQuery.
#"Quit/exit" = sys.exit(), so v. abrupt from web app.

#Bug: fix restart (get rid of dictionary), tests not working.
#Bug: glitches (can be delayed) after saving/loading and then trying to exit. ("I'm sorry, I don't understand that command...")
#Bug: save/load having a lot of issues.
#SOLVED: prints "none" when moving between rooms.
