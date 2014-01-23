class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.directions = {}
        self.inventory = []

    def add_directions(self, directions):
        self.directions = directions

    def describe(self):
        print self.name
        print
        print self.description
        if len(self.inventory) == 1:
            print "\nThere's a %s here." % (self.inventory[0])
        elif len(self.inventory) > 1:
            print "\nThere are a %s and %s here." % (self.inventory[0], self.inventory[1])
            #how to make this flexible for more than two items in the room?

#Rooms Inits
reading_room = Room("Reading Room", '''You're in the Main Reading Room. Large wooden tables fill the room. Clayr sit
at some of the tables, reading. There are exits to the south and west. The main doors are open to the east.''')
librarian_alcove = Room("Librarian Alcove", '''This is the librarian alcove, the main hub of their behind-the-scenes
library management. There are exits to the north, south, east, and west. There is a small roller-top desk in the corner.''')
#possibly open the desk?
binding_room = Room("Binding Room", '''This is the room where the librarians repair damaged books. There are books covering
every flat surface, and a giant press in the back corner. The only exit is to the east.''')
robing_room = Room("Robing Room", '''You're in a room full of miscellaneous useful things. Boat hooks, climbing ropes,
and weapons line the walls. The only exit is to the west.''')
upper_librarian_hallway = Room("Hallway", '''You're standing in a hallway, in the private librarians' wing of the library. Painted blue doors
line the hallway, but they're all closed and locked. There's another door at the south end of the hallway. There's an exit to the north, and
steps leading down.''')
#need to lock doors
chiefs_office = Room("Chief Librarian Vancelle's Office", '''This is Chief Librarian Vancelle's office. It's a roomy, wood-panelled office.
Chief Librarian Vancelle is obviously not the tidiest person; papers and books are stacked willy-nilly on her desk. She's nice
enough, but I wouldn't like to get caught in her office without her permission. The only exit is to the north.''')
middle_librarian_hallway = Room("Hallway", '''You're standing in a hallway. All of the doors are painted red. They're all closed and locked,
except one. The far door on the east side is open. There are stairs leading up and down.''')
second_assistant_study = Room("Second Assistant Study", '''This is your new study, the room of a Second Assistant Librarian. There's enough
room for a desk and not one but two chairs (what luxury!), and there's a door ajar that leads to a tiny bathroom, all your own. The only exit
is to the west. ''')
#need items in her studies. dog statuette?
lower_librarian_hallway = Room("Hallway", '''You're standing in a hallway. There are many doors adjacent to this hallway, more than the two
upper floors. The doors are all painted yellow. They're all closed, except for the one in the far eastern corner.''')
third_assistant_study = Room("Third Assistant Study", '''This is your old study, the one you used for four years. It's much more cramped than
your new study upstairs; there's barely room for the desk and single chair that are here. You can't imagine how you managed to fit all of your
illicit "borrowed" books in this tiny room. The only exit is to the west.''')

#Room Directions
reading_room.add_directions({'s': librarian_alcove})
#I need a "You don't really want to go that way" for when people try to go east.
librarian_alcove.add_directions({'n': reading_room, 'w': binding_room, 'e': robing_room, 's': upper_librarian_hallway})
binding_room.add_directions({'e': librarian_alcove})
robing_room.add_directions({'w': librarian_alcove})
upper_librarian_hallway.add_directions({'s': chiefs_office, 'n': librarian_alcove, 'd': middle_librarian_hallway})
middle_librarian_hallway.add_directions({'u': upper_librarian_hallway, 'd': lower_librarian_hallway, 'e': second_assistant_study})
second_assistant_study.add_directions({'w': middle_librarian_hallway})
lower_librarian_hallway.add_directions({'u': middle_librarian_hallway, 'e': third_assistant_study})
third_assistant_study.add_directions({'w': lower_librarian_hallway})

directory = [reading_room, librarian_alcove, binding_room, robing_room, upper_librarian_hallway, middle_librarian_hallway, lower_librarian_hallway, chiefs_office]
