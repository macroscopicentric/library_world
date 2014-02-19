from player import player
import people #to set level at bottom
import commands

class GameEngine(object):
    def start(self):
        # player = Player()
        player.location.describe()
        self.play()

    def play(self):
        while True:
            commands.command(commands.input_format(), player, game)

game = GameEngine()

# people.vancelle.level_up(player)

game.start()

#To do:
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)
#Sloppy code, incl. initializations at the bottom.
#Bells (item) need to be a recursive so you can call each bell by name.
#Make room states that can change over time (locked doors, etc). Also need to prevent going through the hole at the bottom of the tunnel.
#   Could also use this to create different room descriptions if you get promoted and get a new study, etc.
#Need to note somewhere that you can use 'human' to change back.
#Only describe the room the first time through? This would also cause issues with the way the save function is currently written.
#   (Would also have to divide the directions from the description.)
#Add in more Clayr hallway landmarks as I add other libraries.
#Sequester code. Stop calling class attributes directly; create new methods instead.
#Add Alexandria, expand WTNV, Dream's library, Restricted Section, Pagemaster, DW?, Powell's.
#Levels up, but doesn't change access. Also need to edit Vancelle's dialogue so that she indicates which books you need to shelve,
#   and perhaps a hint in the beginning that you need to get your key before you can level up.
#Levels 1-3, 4-5, 6 >> third, second, first. Second and first get new offices with new books (so access to new spells).
#Increase number/type of spells. Some spells not for changing into animals, but things like "charter water" for Alexandria.
#Lock function in rooms, pull out of player and test there. Change responses to account for things like Alexandria.

#Bug: since the rooms all call each other, they give errors when other rooms haven't been initialized.
#       Is there a way to initialize without a value, non-descructively?
#       HP solved this by NOT initializing with the paths, but adding them second. (Current workaround.)
#SOLVED: save isn't working. Having the same issue that I was earlier with the item dictionary, where it records an object's
#       location but not its data. (Calling by name gives location, not data.)
#SOLVED: save isn't working. Remembers player's location but not their inventory, and doesn't do anything about items that have been taken/
#moved from their original location.
#SOLVED: #Taking an item puts it in your inventory and removes it from the room, but doesn't change the room description.
#SOLVED: moving not working since dividing into multiple files. The "self" part of the location is confusing it.
#SOLVED: 'take all' only takes the first two items. Trying 'take all' again then only takes the next one item (in a room with four items).
#(Due to iteration over a changing list. Created a temp list to solve this.)
#Solved?: two-word commands throw a fatal error if used without a "noun."
#Bug: glitches (can be delayed) after saving/loading and then trying to exit. ("I'm sorry, I don't understand that command...")
#Bug: save/load having a lot of issues.
#Solved: list spells doesn't work. Open ledger works, but then prints that you can't open that.
#Bug: when you talk to Vancelle after leveling up, it goes through all the level-up dialogue again (and it'll go through ALL of
#it everytime you level up.)
