from flask import Flask, render_template, request, session, jsonify, redirect, url_for
import pdb

from library import web_game_wrapper
from game import Game, simplify, reconstitute

app = Flask(__name__)

@app.route('/library_world')
def start_game():
    if 'saved_game' in session:
        description, room_name, game_hash = web_game_wrapper('start_web', session['saved_game'])
        session['saved_game'] = game_hash
    else:
        description, room_name, game_hash = web_game_wrapper('start_web')
        session['saved_game'] = game_hash
    return render_template('game.html', room=room_name,
        output=description)

@app.route('/update', methods=['POST'])
def play_game():
    app.response = request.data

    description, room_name = web_game_wrapper('play_web', app.response, session['saved_game'])
    #As is, this autosaves the game instead of allowing them to save at certain points. Is that a problem?
    #Restarting won't work.
    return jsonify(room=room_name, output=description)

@app.route('/')
def redirect_from_main_page():
    return redirect(url_for('start_game'))

app.secret_key = '00000'

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)