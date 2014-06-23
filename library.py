from game import game
from commands import command

def from_terminal_play():
    print terminal_formatting(game.directory[game.player_state['location']].describe())
    while True:
        output = command(raw_input(">"), game)
        print terminal_formatting(output)

def terminal_formatting(output):
    #Two possible outputs: unicode/string or a dictionary.
    if isinstance(output, basestring):
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
    return (game.directory[game.player_state['location']].describe(),
        game.directory[game.player_state['location']].name)

def play_web(flask_input):
    return (command(flask_input, game),
        game.directory[game.player_state['location']].name)

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
#Allow interactions with book/waistcoat just by "book"/"waistcoat" if there's only one.
#Do anything with disreputable dog statue?
#Move archbishop book to DW library.
#Pay attention to HTML headers in web app template, need to be HTML/JSON for jQuery.

#Bug: glitches (can be delayed) after saving/loading and then trying to exit. ("I'm sorry, I don't understand that command...")
#Bug: save/load having a lot of issues.
#SOLVED: prints "none" when moving between rooms.
