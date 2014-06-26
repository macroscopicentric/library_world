from flask import Flask, render_template, request, redirect
#Not sure if I need all of these, just copying from the tutorial for now.
from library import start_web, play_web

anything_butt_butts = Flask(__name__)

description, room_name, game = start_web()

@anything_butt_butts.route('/library_world')
def start_game():
    global description, room_name
    return render_template('game.html', room=room_name,
        output=description)

@anything_butt_butts.route('/update')
def play_game():
    global description, room_name
    anything_butt_butts.response = request.input['term']

    description, room_name = play_web(anything_butt_butts.response, game)
    print description

    return render_template('game.html', room=room_name,
        output=description)

if __name__ == '__main__':
    anything_butt_butts.run(debug=True)