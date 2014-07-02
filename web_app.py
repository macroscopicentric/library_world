from flask import Flask, render_template, request, session, jsonify
import pdb

from library import web_game_wrapper
from game import Game, simplify, reconstitute

app = Flask(__name__)

@app.route('/library_world', methods=['GET', 'POST'])
def start_game():
    if request.method == 'GET':
        if 'saved_game' in session:
            description, room_name = web_game_wrapper('start_web', session['saved_game'])
        else:
            description, room_name, game_hash = web_game_wrapper('start_web')
            session['saved_game'] = game_hash
        return render_template('game.html', room=room_name,
            output=description)
    else:
        app.response = request.form['response']

        description, room_name = web_game_wrapper('play_web', app.response, session['saved_game'])
        return render_template('game.html', room=room_name,
            output=description)

@app.route('/')
def testing():
    print session.keys()
    return "Go to /library_world if you're looking for the text adventure."

app.secret_key = '00000'

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)