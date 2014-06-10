from player import player
import commands

class GameEngine(object):
    def start(self):
        # first_person = player.Player()
        #Why did I do that? It doesn't work.
        print player.location.describe()
        self.play()

    def play(self):
        while True:
            commands.command(commands.input_format(), player, game)

game = GameEngine()

game.start()

#To do:
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)
#Sloppy code, incl. initializations at the bottom.
#Need to note somewhere that you can use 'human' to change back.
#Only describe the room the first time through? This would also cause issues with the way the save function is currently written.
#   (Would also have to divide the directions from the description.)
#Add in more Clayr hallway landmarks as I add other libraries.
#Add Dream's library?, DW, Ghostbusters?
#Levels 1-3, 4-5, 6 >> third, second, first. Second and first get new offices with new books (so access to new spells).
#Lock function in rooms, pull out of player and test there. Change responses to account for things like Alexandria.
#Madame Pince: dropping banana and then leaving > Pince goes to hospital and door unlocks. WHERE to put code for testing the two conditions?
#       Way to send books back to their default locations? it would also be nice to have one place to set default settings
#       for items, rooms, players for testing etc.
#Standardize returns, remove some of the circularity? Commands go everywhere and branch into multiple modules.
#Add books to Vancelle level ups.
#How to unlock finis Africae?
#End game: promoted to level 7, Vancelle gives you the charter book that allows you to turn into an otter,
#   so you can slip through the crack and find the pipes, crown, and trowel.
#Add NV Librarians, banana peel for Madame Pince, Vashta Nerada, Ghostbusters ghost, Stilken?
#Alan suggested taking all inits out of their respective modules (since while in the modules they're only run once during import).
#   Difficult for modules with more inits (ie, rooms). How to compartmentalize those?

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
#SOLVED: prints "none" when moving between rooms.
