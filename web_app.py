from flask import Flask, render_template, request, session, jsonify
import pdb

from library import start_web, play_web
from game import Game, simplify, reconstitute

app = Flask(__name__)

@app.route('/library_world', methods=['GET', 'POST'])
def start_game():
    if request.method == 'GET':
        if 'saved_game' in session:
            description, room_name, game = start_web(session['saved_game'])
        else:
            description, room_name, game = start_web()
            session['saved_game'] = simplify(game)
        return render_template('game.html', room=room_name,
            output=description)
    else:
        print session.keys()
        game = reconstitute(session['saved_game'])
        app.response = request.data
        print app.response

        description, room_name = play_web(app.response, game)
        #As is, this autosaves the game instead of allowing them to save at certain points. Is that a problem?
        #Restarting won't work.
        session['saved_game'] = simplify(game)
        return render_template('game.html', room=room_name,
            output=description)

@app.route('/')
def testing():
    return "Go to /library_world if you're looking for the text adventure."

app.secret_key = '00000'

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    app.run(debug=True)