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

#Main Ramp Rooms (Clayr Library Spiral)
hall1 = Room("Hallway", '''You're in a hallway with gently sloping floors. Through the eastern archway, you can see the Main
Reading Room. The walls here are blue. There are archways to the east and west.''')
hall2 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the east and west.''')
hall3 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the east and south.''')

hall4 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall5 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall6 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and east.''')

hall7 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the east and west.''')
hall8 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the east and west.''')
hall9 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and west.''')

hall10 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall11 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall12 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are purple.
There are archways to the west and south.''')

hall13 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the east and west.''')
hall14 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the east and south.''')

hall15 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and south.''')
hall16 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and east.''')

hall17 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the east and west.''')
hall18 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and west.''')

hall19 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and south.''')
hall20 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are orange.
There are archways to the west and south.''')

hall21 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are yellow.
There are archways to the east and south. There's a closed door to the west.''')

hall22 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are yellow.
There are archways to the north and east.''')

hall23 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are yellow.
There are archways to the north and west.''')

hall24 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are yellow. There's an archway to the south.
On the west wall, there's a hole, far too small for a human to pass through.''')

#Name of the Rose Labyrinth
#Eastern Tower
labyrinth1 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is heptagonal, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north, east, and south, and stairs leading down.''')
labyrinth2 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular. There's an
altar below the window. There are doors to the north and west.''')
labyrinth3 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Obscuratus est sol et aer." There are doors to the west and south.''')
labyrinth4 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Facta est grandi et ignis." There are doors to the east, west, and south.''')
labyrinth5 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "U*." There are doors to the east and west.''') #unfinished inscription (U)
labyrinth6 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "D*." There are doors to the east, west, and south.''') #unfinished inscription (D)
labyrinth7 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Super thronos viginti quatuor." There are doors to the east and west.''')
labyrinth8 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "V*." There are doors to the north and west.''') #unfinished inscription (V)
labyrinth12 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north and east.''')
labyrinth13 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the north, east, and south.''')

#Between East and South
labyrinth9 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Gratia vobis et pax." There are doors to the north, west, and south.''')
labyrinth10 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Y*." There is a door to the north.''') #unfinished inscription (Y)
labyrinth11 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the east and south.''')
labyrinth14 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Primogenitus mortuorum." There are doors to the north and south.''')

#Southern Tower
labyrinth15 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Tertia pars terrae combusta est." There are doors to the east and south.''')
labyrinth16 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "U*." There are doors to the north, west, and south.''') #unfinished inscription (U)
labyrinth17 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "L*." There are doors to the north and south.''') #unfinished inscription (L)
labyrinth18 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the north and west.''')
labyrinth19 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Obscuratus est sol et aer." There are doors to the east and west.''')
labyrinth20 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Nomen illi mors." There are doors to the north and east.''')
labyrinth21 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the north and south.''')
labyrinth22 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "Super thronos viginti quatuor." There are doors to the north, east, west, and south.''')
labyrinth23 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Y*." There is a door to the south.''') #unfinished inscription (Y)
finis_africae = Room("Hidden Room", '''You're in a room in the labyrinth. This one is heptagonal. There's a door to the north.''')

#Between South and West
labyrinth24 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Primogenitus mortuorum." There are doors to the north and east.''')
labyrinth25 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Requiescant a laboribus suis." There are doors to the west and south.''')
labyrinth26 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Obscuratus est sol et aer." There are doors to the east and south.''')
labyrinth27 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north and west.''')

#West Tower
labyrinth28 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "Nomen illi mors." There are doors to the north, east, west, and south.''')
labyrinth29 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Requiescant a laboribus suis." There are doors to the east and west.''')
labyrinth30 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the north and east.''')
labyrinth31 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is heptagonal, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There is a door to the south.''')
labyrinth32 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "In diebu illis." There are doors to the west and south.''')
labyrinth33 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "H*." There are doors to the east and west.''') #unfinished inscription (H)
labyrinth34 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the east and south.''')
labyrinth35 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "B*." There is a door to the north.''') #unfinished inscription (B)
labyrinth36 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "M*." There are doors to the north and west.''') #unfinished inscription (M)
labyrinth37 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north and south.''')

#Between West and North
labyrinth38 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the north, west, and south.''')
labyrinth39 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "L*." There is a door to the east.''') #unfinished inscription (L)
labyrinth40 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north, west, and south.''')
labyrinth41 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "L*." There is a door to the east.''') #unfinished inscription (L)

#North Tower
labyrinth42 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Gratia vobis et pax." There are doors to the north and west.''')
labyrinth43 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "M*." There are doors to the north, east, west, and south.''') #unfinished inscription (M)
labyrinth44 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the north and south.''')
labyrinth45 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "L*." There is a door to the south.''') #unfinished inscription (L)
labyrinth46 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is heptagonal, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north, east, and south.''')
labyrinth47 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Gratia vobis et pax." There is a door to the south.''')
labyrinth48 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the north and west.''')
labyrinth49 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Nomen illi mors." There is a door to the south.''')
labyrinth50 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "Requiescant a laboribus suis." There are doors to the east and west.''')
labyrinth51 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There is a door to the east.''')

#Between North and East
labyrinth52 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the east, west, and south.''')
labyrinth53 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Cecidit de cielo stella magna." There are doors to the north and west.''')
labyrinth54 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the west and south.''')
labyrinth55 = Room("Labyrinth Room", '''You're in a room in the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north and east.''')


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
hall21.add_directions({'e': hall20, 's': hall22, 'w': labyrinth1})
hall22.add_directions({'e': hall23, 'n': hall21})
hall23.add_directions({'w': hall22, 'n': hall24})
hall24.add_directions({'s': hall23})

labyrinth1.add_directions({'e': labyrinth2, 'n': labyrinth4, 's': labyrinth8, 'd': hall21})
labyrinth2.add_directions({'w': labyrinth1, 'n': labyrinth3})
labyrinth3.add_directions({'s': labyrinth3, 'w': labyrinth4})
labyrinth4.add_directions({'e': labyrinth3, 's': labyrinth1, 'w': labyrinth5})
labyrinth5.add_directions({'e': labyrinth4, 'w': labyrinth13})
labyrinth6.add_directions({'e': labyrinth7, 'w': labyrinth12, 's': labyrinth9})
labyrinth7.add_directions({'w': labyrinth6, 'e': labyrinth8})
labyrinth8.add_directions({'w': labyrinth7, 'n': labyrinth1})
labyrinth9.add_directions({'n': labyrinth6, 'w': labyrinth11, 's': labyrinth10})
labyrinth10.add_directions({'n': labyrinth9})
labyrinth11.add_directions({'e': labyrinth9, 's': labyrinth14})
labyrinth12.add_directions({'e': labyrinth6, 'n': labyrinth13})
labyrinth13.add_directions({'n': labyrinth55, 's': labyrinth12, 'e': labyrinth5})
labyrinth14.add_directions({'n': labyrinth11, 's': labyrinth15})
labyrinth15.add_directions({'e': labyrinth14, 's': labyrinth16})
labyrinth16.add_directions({'n': labyrinth15, 'w': labyrinth22, 's': labyrinth17})
labyrinth17.add_directions({'n': labyrinth16, 's': labyrinth18})
labyrinth18.add_directions({'n': labyrinth17, 'w': labyrinth19})
labyrinth19.add_directions({'e': labyrinth18, 'w': labyrinth20})
labyrinth20.add_directions({'e': labyrinth19, 'n': labyrinth21})
labyrinth21.add_directions({'s': labyrinth20, 'n': labyrinth22})
labyrinth22.add_directions({'n': labyrinth23, 'e': labyrinth16, 's': labyrinth21, 'w': labyrinth24})
labyrinth23.add_directions({'s': labyrinth22})
labyrinth24.add_directions({'e': labyrinth22, 'n': labyrinth25})
labyrinth25.add_directions({'s': labyrinth24, 'w': labyrinth26})
labyrinth26.add_directions({'e': labyrinth25, 's': labyrinth27})
labyrinth27.add_directions({'n': labyrinth26, 'w': labyrinth28})
labyrinth28.add_directions({'e': labyrinth36, 's': labyrinth27, 'n': labyrinth32, 'w': labyrinth29})
labyrinth29.add_directions({'e': labyrinth28, 'w': labyrinth30})
labyrinth30.add_directions({'e': labyrinth29, 'n': labyrinth31})
labyrinth31.add_directions({'s': labyrinth30})
finis_africae.add_directions({'n': labyrinth22})
labyrinth32.add_directions({'s': labyrinth28, 'w': labyrinth33})
labyrinth33.add_directions({'e': labyrinth32, 'w': labyrinth34})
labyrinth34.add_directions({'e': labyrinth33, 's': labyrinth35})
labyrinth35.add_directions({'n': labyrinth34})
labyrinth36.add_directions({'w': labyrinth28, 'n': labyrinth37})
labyrinth37.add_directions({'s': labyrinth36, 'n': labyrinth38})
labyrinth38.add_directions({'s': labyrinth37, 'n': labyrinth40, 'w': labyrinth39})
labyrinth39.add_directions({'e': labyrinth38})
labyrinth40.add_directions({'s': labyrinth38, 'w': labyrinth41, 'n': labyrinth42})
labyrinth41.add_directions({'e': labyrinth40})
labyrinth42.add_directions({'w': labyrinth40, 'n': labyrinth43})
labyrinth43.add_directions({'s': labyrinth42, 'e': labyrinth50, 'n': labyrinth46, 'e': labyrinth44})
labyrinth44.add_directions({'s': labyrinth43, 'n': labyrinth45})
labyrinth45.add_directions({'s': labyrinth44})
labyrinth46.add_directions({'s': labyrinth43, 'n': labyrinth47, 'e': labyrinth48})
labyrinth47.add_directions({'s': labyrinth46})
labyrinth48.add_directions({'w': labyrinth46, 'n': labyrinth49})
labyrinth49.add_directions({'s': labyrinth48})
labyrinth50.add_directions({'w': labyrinth43, 'e': labyrinth52})
labyrinth51.add_directions({'e': labyrinth53})
labyrinth52.add_directions({'w': labyrinth50, 'e': labyrinth54, 's': labyrinth53})
labyrinth53.add_directions({'n': labyrinth52, 'w': labyrinth51})
labyrinth54.add_directions({'w': labyrinth52, 's': labyrinth55})
labyrinth55.add_directions({'n': labyrinth54, 'e': labyrinth13})
