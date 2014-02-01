directory = []

class Room(object):
    def __init__(self, name, description, locked=False):
        self.name = name
        self.description = description
        self.directions = {}
        self.inventory = []
        self.locked = locked
        directory.append(self)

    def add_directions(self, directions):
        self.directions = directions

    def describe(self):
        print self.name
        print
        print self.description
        if len(self.inventory) == 1:
            print "\nThere's a %s here." % (self.inventory[0])
        elif len(self.inventory) == 2:
            print "\nThere are a %s and %s here." % (self.inventory[0], self.inventory[1])
        #how to make this flexible, no matter how many items in the room?
        elif len(self.inventory) == 3:
            print '\nThere are a %s, %s, and %s here.' % (self.inventory[0], self.inventory[1], self.inventory[2])
        elif len(self.inventory) == 4:
            print '\nThere are a %s, %s, %s, and %s here.' % (self.inventory[0], self.inventory[1], self.inventory[2], self.inventory[3])

#Rooms Inits
reading_room = Room("Reading Room", '''You're in the Main Reading Room. Large wooden tables fill the room. Clayr sit
at some of the tables, reading. There are exits to the south and west. The main doors are open to the east.''')
librarian_alcove = Room("Librarian Alcove", '''This is the librarian alcove, the main hub of their behind-the-scenes library management.
There are exits to the north, south, east, and west. There is a small roller-top desk in the corner.''')
#possibly open the desk?
binding_room = Room("Binding Room", '''This is the room where the librarians repair damaged books. There are books covering
every flat surface, and a giant press in the back corner. The only exit is to the east.''')
robing_room = Room("Robing Room", '''You're in a room full of miscellaneous useful things. Boat hooks, climbing ropes,
and weapons line the walls. The only exit is to the west.''')
upper_librarian_hallway = Room("Hallway", '''You're standing in a hallway, in the employees-only librarians' wing of the library. Painted blue doors
line the hallway, but they're all closed and locked. There's another door at the south end of the hallway.
There's an exit to the north, and steps leading down.''')
chiefs_office = Room("Chief Librarian Vancelle's Office", '''This is Chief Librarian Vancelle's office. It's a roomy, wood-panelled office.
Chief Librarian Vancelle is obviously not the tidiest person; papers and books are stacked willy-nilly on her desk. She's nice
enough, but I wouldn't like to get caught in her office without her permission. The only exit is to the north.''', True)
middle_librarian_hallway = Room("Hallway", '''You're standing in a hallway. All of the doors are painted red. They're all closed and locked.
There are stairs leading up and down.''')
second_assistant_study = Room("Second Assistant Study", '''This is your new study, the room of a Second Assistant Librarian. There's enough
room for a desk and not one but two chairs (what luxury!), and there's a door ajar that leads to a tiny bathroom, all your own. The only exit
is to the west. ''', True)
#need items in her studies. dog statuette?
lower_librarian_hallway = Room("Hallway", '''You're standing in a hallway. There are many doors adjacent to this hallway, more than the two
upper floors. The doors are all painted yellow. They're all closed, except for the one in the far eastern corner.''')
third_assistant_study = Room("Third Assistant Study", '''This is your study. It's very cramped; there's barely room for the desk and
single chair that are here. The only exit is to the west.''')

hall1 = Room("Hallway", '''You're in a hallway. There are archways to the east and west.
Through the eastern archway, you can see the Main Reading Room.''')
hall2 = Room("Hallway", '''You're in a hallway. There are archways to the east and west.''')
hall3 = Room("Hallway", '''You're in a hallway. There are archways to the east and south.''')

hall4 = Room("Hallway", '''You're in a hallway. There are archways to the north and south.''')
hall5 = Room("Hallway", '''You're in a hallway. There are archways to the north and south.''')
hall6 = Room("Hallway", '''You're in a hallway. There are archways to the north and east.''')

hall7 = Room("Hallway", '''You're in a hallway. There are archways to the east and west.''')
hall8 = Room("Hallway", '''You're in a hallway. There are archways to the east and west.''')
hall9 = Room("Hallway", '''You're in a hallway. There are archways to the north and west.''')

hall10 = Room("Hallway", '''You're in a hallway. There are archways to the north and south.''')
hall11 = Room("Hallway", '''You're in a hallway. There are archways to the north and south.''')
hall12 = Room("Hallway", '''You're in a hallway. There are archways to the west and south.''')

hall13 = Room("Hallway", '''You're in a hallway. There are archways to the east and west.''')
hall14 = Room("Hallway", '''You're in a hallway. There are archways to the east and south.''')

hall15 = Room("Hallway", '''You're in a hallway. There are archways to the north and south.''')
hall16 = Room("Hallway", '''You're in a hallway. There are archways to the north and east.''')

hall17 = Room("Hallway", '''You're in a hallway. There are archways to the east and west.''')
hall18 = Room("Hallway", '''You're in a hallway. There are archways to the north and west.''')

hall19 = Room("Hallway", '''You're in a hallway. There are archways to the north and south.''')
hall20 = Room("Hallway", '''You're in a hallway. There are archways to the west and south.''')

hall21 = Room("Hallway", '''You're in a hallway. There are archways to the east and south.''')

hall22 = Room("Hallway", '''You're in a hallway. There are archways to the north and east.''')

hall23 = Room("Hallway", '''You're in a hallway. There are archways to the north and west.''')

hall24 = Room("Hallway", '''You're in a hallway. There's an archway to the south.
On the west wall, there's a hole, far too small for a human to pass through.''')

#Room Directions
reading_room.add_directions({'s': librarian_alcove, 'w': hall1})
#I need a "You don't really want to go that way" for when people try to go east.
librarian_alcove.add_directions({'n': reading_room, 'w': binding_room, 'e': robing_room, 's': upper_librarian_hallway})
binding_room.add_directions({'e': librarian_alcove})
robing_room.add_directions({'w': librarian_alcove})
upper_librarian_hallway.add_directions({'s': chiefs_office, 'n': librarian_alcove, 'd': middle_librarian_hallway})
middle_librarian_hallway.add_directions({'u': upper_librarian_hallway, 'd': lower_librarian_hallway, 'e': second_assistant_study})
second_assistant_study.add_directions({'w': middle_librarian_hallway})
lower_librarian_hallway.add_directions({'u': middle_librarian_hallway, 'e': third_assistant_study})
third_assistant_study.add_directions({'w': lower_librarian_hallway})

hall1.add_directions({'e': reading_room, 'w': hall2})
hall2.add_directions({'e': hall1, 'w': hall3})
hall3.add_directions({'e': hall2, 's': hall4})
hall4.add_directions({'n': hall3, 's': hall5})
hall5.add_directions({'n': hall4, 's': hall6})
hall6.add_directions({'e': hall7, 'n': hall5})
hall7.add_directions({'e': hall8, 'w': hall6})
hall8.add_directions({'e': hall9, 'w': hall7})
hall9.add_directions({'n': hall10, 'w': hall8})
hall10.add_directions({'n': hall11, 's': hall9})
hall11.add_directions({'n': hall12, 's': hall10})
hall12.add_directions({'w': hall13, 's': hall11})
hall13.add_directions({'e': hall12, 'w': hall14})
hall14.add_directions({'e': hall13, 's': hall15})
hall15.add_directions({'n': hall14, 's': hall16})
hall16.add_directions({'n': hall15, 'e': hall17})
hall17.add_directions({'e': hall18, 'w': hall16})
hall18.add_directions({'n': hall19, 'w': hall17})
hall19.add_directions({'n': hall20, 's': hall18})
hall20.add_directions({'w': hall21, 's': hall19})
hall21.add_directions({'e': hall20, 's': hall22})
hall22.add_directions({'e': hall23, 'n': hall21})
hall23.add_directions({'w': hall22, 'n': hall24})
hall24.add_directions({'s': hall23})

