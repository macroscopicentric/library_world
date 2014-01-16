import sys

moves = ["up", "down", "n", "e", "w", "s"]
one_liners = ['hello', 'hi', 'quit', 'exit', 'help', 'restart']
dictionary = moves + one_liners
#I really like that the HP text adventure has a thesaurus. Also, the above lists don't do 

class Player(object):
    def __init__(self):
        self.alive = True
        self.location = "Library Entrance" #placeholder
        self.inventory = []

    def Move(self, room):
        self.location = "New Room" #placeholder

class Room(object):
    def __init__(self):
        self.description = "This room is a work in progress." #placeholder
        self.directions = []
        self.inventory = []

class GameEngine(object):
    def __init__(self):
        player = Player()

    def input_format(self):
        user_input = raw_input(">").lower().split(" ")

        if "." in user_input[-1]:
            detail = user_input.pop().split(".").pop(0)
            user_input.append(detail)

        if len(user_input) > 2:
            print 'I do better with just one or two words. Type "help" for some commands you can use.'
            game.play()

        return user_input

    def invalid_input(self):
        print "I'm sorry, I don't understand that command."
        game.play()

    def command(self, user_input):
        global game
        #For restarting.

        if len(user_input) == 1:
            #Easter Eggs
            if 'hello' in user_input or 'hi' in user_input: print "Hullo!"
            #Commands
            elif 'help' in user_input:
                print '''
My commands are like a traditional text adventure\'s. To move, use the cardinal directions ("n", "s", "e", or "w")
or "up" and "down". Other commands you can use: "look" (describes the room to you), "examine [object]", "exit" or
"quit" (exits the game), or "restart" (restarts the game).'''
            elif 'exit' in user_input or 'quit' in user_input: sys.exit()
            elif 'restart' in user_input:
                print "Are you sure you want to restart? Y/N"
                user_input = game.input_format()
                if "y" in user_input or "yes" in user_input:
                    game = GameEngine()
                    game.play()
                elif "n" in user_input or "no" in user_input: game.play()
                else: game.invalid_input()
            elif user_input[0] in moves:
                #is there a better way to do this/standardize it with the rest of the commands?
                if user_input[0] in player.location.directions:
                    player.location = "New Room" #placeholder
            else: game.invalid_input()

    def play(self):
        while True:
            game.command(game.input_format())

game = GameEngine()
game.play()

#To do:
#Generic "I'm sorry, I don't know what you mean" error method. Need an allowed list of commands.
#Standardize the command list somehow? The giant if statement seems sloppy.