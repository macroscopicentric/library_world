from flask import Flask, render_template, request, session, jsonify
import pdb

from library import start_web, play_web
from game import Game

anything_butt_butts = Flask(__name__)

@anything_butt_butts.route('/library_world')
def start_game():
    if 'saved_game' in session:
        game = Game()
        #To do:
        web_load(game)
    #To restart game when browser refreshes:
    global description, room_name, game
    description, room_name, game = start_web()
    return render_template('game.html', room=room_name,
        output=description)

@anything_butt_butts.route('/update', methods=['POST'])
def play_game():
    global description, room_name, game
    # pdb.set_trace()
    anything_butt_butts.response = request.data

    description, room_name = play_web(anything_butt_butts.response, game)

    return jsonify(room=room_name, output=description)

@anything_butt_butts.route('/')
def testing():
    return "Hello world! (Go to /library_world if you're looking for the text adventure.)"

anything_butt_butts.secret_key = '00000'

if __name__ == '__main__':
    anything_butt_butts.run(host='0.0.0.0')