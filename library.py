from player import player
from rooms import directory
import commands

def from_terminal_play():
    print terminal_formatting(directory[player.location].describe())
    while True:
        output = commands.command(commands.input_format(raw_input(">")), player)
        print terminal_formatting(output)

def terminal_formatting(output):
    #I'm really specific about the number of line breaks I want okay.
    #Two possible outputs: a string or a dictionary.
    if type(output) == str:
        return output

    description = output['text'][0]
    if len(output['text']) > 1:
        for item in output['text'][1:]:
            description += '\n' + item

    formatted_output = ''
    if 'event' in output.keys():
        formatted_output += output['event'] + '\n\n'
    if 'header' in output.keys():
        formatted_output += output['header'] + '\n\n'

    formatted_output += description

    if 'inventory' in output.keys():
        formatted_output += '\n\n' + output['inventory']
    if 'npc' in output.keys() and 'inventory' in output.keys():
        formatted_output += '\n' + output['npc']
    elif 'npc' in output.keys() and 'inventory' not in output.keys():
        formatted_output += '\n\n' + output['npc']

    return formatted_output

def start_web():
    return player.location.describe(), player.location.name

def play_web(flask_input):
    return commands.command(commands.input_format(flask_input), player), player.location.name

if __name__ == "__main__":
    from_terminal_play()

#To do:
#Currently manually entering line breaks. (HP doesn't have line breaks, so breaks at the end of the window,
#often in the middle of a word. Would also need to delete extra spaces if I can do automatic line breaks.)
#Add in more Clayr hallway landmarks as I add other libraries.
#Add Dream's library?, DW, Ghostbusters?
#Levels 1-3, 4-5, 6 >> third, second, first. Second and first get new offices with new books (so access to new spells).
#Remove some of the circularity? Commands go everywhere and branch into multiple modules.
#How to unlock finis Africae?
#End game: promoted to level 7, Vancelle gives you the charter book that allows you to turn into an otter,
#   so you can slip through the crack and find the pipes, crown, and trowel.
#Add NV Librarians, banana peel for Madame Pince, Vashta Nerada, Ghostbusters ghost, Stilken?
#Alan suggested taking all inits out of their respective modules (since while in the modules they're only run once during import).
#   Difficult for modules with more inits (ie, rooms). How to compartmentalize those?
#Allow interactions with book/waistcoat just by "book"/"waistcoat" if there's only one.
#Do anything with disreputable dog statue?
#Move archbishop book to DW library.
#Pay attention to HTML headers in web app template, need to be HTML/JSON for jQuery.

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
#SOLVED: two-word commands throw a fatal error if used without a "noun."
#Bug: glitches (can be delayed) after saving/loading and then trying to exit. ("I'm sorry, I don't understand that command...")
#Bug: save/load having a lot of issues.
#SOLVED: list spells doesn't work. Open ledger works, but then prints that you can't open that.
#Bug: when you talk to Vancelle after leveling up, it goes through all the level-up dialogue again (and it'll go through ALL of
#it everytime you level up.)
#SOLVED: prints "none" when moving between rooms.
#Bug: need to prevent leveling up out of order.
