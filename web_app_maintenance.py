from flask import Flask, render_template, request, session, jsonify

from library import web_game_wrapper
from game import Game, simplify, reconstitute

app = Flask(__name__)

@app.route('/library_world')
def down_time():
    return render_template('maintenance.html')

@app.route('/')
def redirect_from_main_page():
    return redirect(url_for('start_game'))

app.secret_key = '00000'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # app.run(debug=True)