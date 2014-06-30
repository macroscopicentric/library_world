from flask import Flask, render_template, request
import pdb
import json

from library import start_web, play_web

anything_butt_butts = Flask(__name__)

@anything_butt_butts.route('/library_world')
def start_game():
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

    return room_name + json.dumps(description)


if __name__ == '__main__':
    anything_butt_butts.run(debug=True)