from flask import Flask, render_template, request, redirect
#Not sure if I need all of these, just copying from the tutorial for now.
#import library
#Import only happens once. Is that going to be a problem?

anything_butt_butts = Flask(__name__)

@anything_butt_butts.route('/library_world', methods=['GET','POST'])
def game_function():
    if request.method == 'GET':
        return render_template('game_call.html', room="Test 1",
            printout="This is the first test room.")
    else:
        anything_butt_butts.response = request.form['response']

        return render_template('game_response.html', response=anything_butt_butts.response)

if __name__ == '__main__':
    anything_butt_butts.run(debug=True)