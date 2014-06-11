from flask import Flask, render_template, request, redirect
#Not sure if I need all of these, just copying from the tutorial for now.
from library import start_web, play_web

anything_butt_butts = Flask(__name__)

description, room_name = start_web()

@anything_butt_butts.route('/library_world', methods=['GET','POST'])
def game_function():
    global description, room_name
    if request.method == 'GET':
        return render_template('game_call.html', room=room_name,
            printout=description)
    else:
        anything_butt_butts.response = request.form['response']

        description, room_name = play_web(anything_butt_butts.response)

        return render_template('game_call.html', room=room_name,
            printout=description)

if __name__ == '__main__':
    anything_butt_butts.run(debug=True)