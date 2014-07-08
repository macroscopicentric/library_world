import json
import sys
import random
import string
import os
import psycopg2
import urlparse

from game import Game, simplify, reconstitute, home
from commands import command

def save(game, save_name):
    try:
        json_dict = simplify(game)
        try:
            save_file = open((save_name + '.txt'), 'w')
            json.dump(json_dict, save_file, separators=(',', ':'))
            return "File saved."
        finally:
            save_file.close()
    except:
        return '''I didn't understand that. Did you use the format "save [filename]?"'''

def load(save_name):
    try:
        game = reconstitute(json.load(open(save_name + '.txt')))
        new_game_output = game.directory[game.player_state['location']].describe()
        new_game_output['event'] = 'Loading...'
        return new_game_output, game
    except IOError:
        return '''I didn't understand that. Did you use the format "load [filename]?"'''

def restart():
    game = Game()
    new_game_output = game.directory[game.player_state['location']].describe()
    new_game_output['event'] = 'Restarting...'
    return new_game_output, game



#Helper function that takes user input and returns parsed list.
def input_format(user_input):
    user_input = user_input.lower().split(" ", 1)

    if "." in user_input[-1]:
        detail = user_input.pop().split(".").pop(0)
        user_input.append(detail)

    arts_and_preps = ['to', 'the', 'a', 'an', 'with']
    #allows splitting for compound sentences ("give __ to __") while still
    #retaining book items as one word.
    if len(user_input) > 1:
        for word in arts_and_preps:
            if word in user_input[1]:
                second_word = user_input.pop()
                second_word = second_word.split(' ', 1)[1]
                user_input.append(second_word)
        
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
    for word in arts_and_preps:
        if word in user_input:
            user_input.remove(word)

    return user_input

#Helper function for terminal. Stupidly redundant.
def play_term_game(user_input, game):
    player_response = input_format(user_input)
    if player_response[0] == 'load':
        return load(player_response[1])
    elif player_response[0] == 'save':
        return save(game, player_response[1])
    elif player_response[0] == 'restart':
        return restart()
    elif player_response[0] in ['exit', 'quit']:
        sys.exit()
    else:
        return command(player_response, game)

def from_terminal_play():
    game = Game()
    print terminal_formatting(game.directory[game.player_state['location']].describe())
    while True:
        print terminal_formatting(play_term_game(raw_input('>'), game))


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

#To avoid having a global web_games hash while still being able to access it
#from both start_web and play_web (can't pass it from route to route in flask).
def web_game_wrapper(function, *args):
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])

    def web_load(game_code):
        with psycopg2.connect(database=url.path[1:],
            user=url.username, password=url.password, host=url.hostname,
            port=url.port) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT game_json FROM saved_games WHERE session_name = %s;", [game_code])
                game = reconstitute(json.loads(cur.fetchone()[0]))

        new_game_output = game.directory[game.player_state['location']].describe()
        return new_game_output, game

    def start_web(session_game=None):
        def add_to_hash():
            def generate_code():
                character_pool = string.ascii_letters + string.digits
                random_string = ''.join(random.choice(character_pool) for i in range(10))
                return random_string

            game_code = generate_code()
            with psycopg2.connect(database=url.path[1:],
                user=url.username, password=url.password, host=url.hostname,
                port=url.port) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT session_name FROM saved_games;")
                    existing_sessions = cur.fetchall()
                    while True:
                        #cur.fetchall() returns a list of tuples. hence matching with a tuple below.
                        if tuple((game_code,)) not in existing_sessions:
                            game = Game()
                            cur.execute("INSERT INTO saved_games (session_name, game_json) VALUES (%s, %s);", (game_code, json.dumps(simplify(game))))
                            conn.commit()

                            return game_code, game
                        else:
                            game_code = generate_code()

        def new_game():
            game_code, game = add_to_hash()
            description = game.directory[game.player_state['location']].describe()
            return (description, game.directory[game.player_state['location']].name,
                        game_code)

        if session_game:
            description, game = web_load(session_game)
            return (description, game.directory[game.player_state['location']].name)
        else:
            return new_game()

    def play_web(flask_input, session_game):
        old_game_output, game = web_load(session_game)

        player_response = input_format(flask_input)

        if player_response[0] == 'restart':
            description, game = restart()
        else:
            description = command(player_response, game)

        with psycopg2.connect(database=url.path[1:],
            user=url.username, password=url.password, host=url.hostname,
            port=url.port) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE saved_games SET game_json=%s WHERE session_name=%s;", (json.dumps(simplify(game)), session_game))
                conn.commit()
        return (description,
            game.directory[game.player_state['location']].name)

    if function == 'start_web':
        return start_web(*args)
    else:
        return play_web(*args)

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
#Eliminate a lot of the repetitive code in this module.
#Max pointed out that it's vulnerable to cross-site scripting.

#Bug: can't level up past level 2?
