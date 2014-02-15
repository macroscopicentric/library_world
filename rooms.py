from list_items import list_items

directory = []
labyrinths = []

class Room(object):
    def __init__(self, name, description, locked=False, secondary_description=None):
        self.name = name
        self.description = description
        self.directions = {}
        self.inventory = []
        self.npc = None
        self.locked = locked
        self.counter = 0
        self.secondary_description = secondary_description
        directory.append(self)

    def add_directions(self, directions):
        self.directions = directions

    def describe(self):
        print self.name
        print
        print self.description

        if self.counter == 1 and self.secondary_description:
            print self.secondary_description

        if self.inventory: print list_items(self.inventory)

        if self.npc != None:
            if not self.inventory: print
            if self.npc == 'orangutan':
                print "An %s is here." % (self.npc)
            else: print "%s is here." % (self.npc.capitalize())

    def change_counter(self, counter):
        self.counter = counter

class Labyrinth(Room):
    def __init__(self, *args):
        super(Labyrinth, self).__init__(*args)
        self.labyrinth = True

#Rooms Inits
#Main Clayr Library
reading_room = Room("Reading Room", '''You're in the Main Reading Room. Large wooden tables fill the room. Clayr sit at some of the tables,
reading. There are exits to the south and west. The main doors are open to the east.''')
librarian_alcove = Room("Librarian Alcove", '''This is the librarian alcove, the main hub of their behind-the-scenes library management.
There are exits to the north, south, east, and west. There is a small roller-top desk in the corner.''')
#possibly open the desk?
binding_room = Room("Binding Room", '''This is the room where the librarians repair damaged books. There are books covering
every flat surface, and a giant press in the back corner. The only exit is to the east.''')
robing_room = Room("Robing Room", '''You're in a room full of miscellaneous useful things. Boat hooks, climbing ropes,
and weapons line the walls. The only exit is to the west.''')
upper_librarian_hallway = Room("Hallway", '''You're standing in a hallway, in the employees-only librarians' wing of the library. Painted blue doors
line the hallway, but they're all closed and locked. There's another locked door at the south end of the hallway.
There's an exit to the north, and steps leading down.''')
chiefs_office = Room("Chief Librarian Vancelle's Office", '''This is Chief Librarian Vancelle's office. It's a roomy, wood-panelled office.
Chief Librarian Vancelle is obviously not the tidiest person; papers and books are stacked willy-nilly on her desk. She's nice
enough, but I wouldn't like to get caught in her office without her permission. The only exit is to the north.''')
middle_librarian_hallway = Room("Hallway", '''You're standing in a hallway. All of the doors are painted red. They're all closed and locked.
There are stairs leading up and down.''')
second_assistant_study = Room("Second Assistant Study", '''This is your new study, the room of a Second Assistant Librarian. There's enough
room for a desk and not one but two chairs (what luxury!), and there's a door ajar that leads to a tiny bathroom, all your own. The only exit
is to the west. ''', True)
lower_librarian_hallway = Room("Hallway", '''You're standing in a hallway. There are many doors adjacent to this hallway, more than the two
upper floors. The doors are all painted yellow. They're all closed, except for the one in the southeastern corner.''')
third_assistant_study = Room("Third Assistant Study", '''This is your study. It's very cramped; there's barely room for the desk and
single chair that are here. The only exit is to the west.''')

#Main Ramp Rooms (Clayr Library Spiral)
hall1 = Room("East-West Hallway", '''You're in a hallway with gently sloping floors. Through the eastern archway, you can see the Main
Reading Room. The walls here are blue. There are archways to the east and west.''')
hall2 = Room("East-West Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the east and west.''')
hall3 = Room("East-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There is a table in the corner with a rose lying on it. There are archways to the east
and south, and a stained-glass door to the west.''')

hall4 = Room("North-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall5 = Room("North-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall6 = Room("North-East Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and east.''')

hall7 = Room("East-West Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the east and west.''')
hall8 = Room("East-West Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There is an empty soap dispenser on the wall labeled "Librarian Repellent." There are archways
to the east and west, and a door to the south.''')
hall9 = Room("North-West Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and west.''')

hall10 = Room("North-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall11 = Room("North-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall12 = Room("West-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are purple.
There is a large statue of a turtle in the corner. There are archways to the west and south.''')

hall13 = Room("East-West Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There is a strange painting on the wall of faceless people going up and down impossible
stairways. There are archways to the east and west, and a door to the north.''')
hall14 = Room("East-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There is a large statue of an elephant in the corner. There are archways to the east and south.''')

hall15 = Room("North-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and south.''')
hall16 = Room("North-East Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and east.''')

hall17 = Room("East-West Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the east and west.''')
hall18 = Room("North-West Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and west.''')

hall19 = Room("North-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and south.''')
hall20 = Room("West-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are orange.
There are archways to the west and south.''')

hall21 = Room("East-South Hallway", '''You're in a hallway with gently sloping floors. The walls here are yellow.
On the wall, there's a very old and very inaccurate world map. (Who ever heard of a place called
Leones?!) There are archways to the east and south. There's an open door, with stairs beyond, to the west.''')

hall22 = Room("North-East Hallway", '''You're in a hallway with gently sloping floors. The walls here are yellow.
There are archways to the north and east.''')

hall23 = Room("North-West Hallway", '''You're in a hallway with gently sloping floors. The walls here are yellow.
There are archways to the north and west. There's a locked door with a sunburst
painted on it to the east.''')

hall24 = Room("Hallway", '''You're in a hallway with gently sloping floors. The walls here are yellow. There's an archway to the south.
On the west wall, there's a hole, far too small for a human to pass through.''')


#Beast's Library
beast_library1 = Room("Beast's Library", '''You're in a huge room filled floor to 50-foot ceiling with books, with tall windows in the southwest
and northwest corners. The room extends to the north and south, and there's a door to the east.''')
beast_library2 = Room("Beast's Library", '''You're in the southern end of a massive library. It extends to the north, and there's
a staircase in the corner.''')
beast_library3 = Room("Beast's Library - Walkway", '''You're standing on a walkway about halfway up the southern wall of a massive library.
There are stairs leading down.''')
beast_library4 = Room("Beast's Library", '''You're in the northern end of a massive library. It extends to the south, and there's
a staircase in the corner.''')
beast_library5 = Room("Beast's Library - Walkway", '''You're standing on a walkway about halfway up the northern wall of a massive library.
There are stairs leading down.''')
beast_library = [beast_library1, beast_library2, beast_library3, beast_library4, beast_library5]


#Unseen University Library
uu_library1 = Room('Unseen University Library', '''You're in the prestigiously distinguished and esteemed Unseen University Library.
It is just as officious-looking as you'd expect of such a prestigiously distinguished and esteemed library;
the walls are covered with cherry panelling, in the rare instances that they aren't covered in books.
The floor is glass, or possibly glass. At any rate, you can see people below you walking around, although,
strangely, they seem to be walking upside down. You're in the reading hall, which extends to the
north before ending in a massive window that takes up the entire northen wall. There are also stairs
leading up and down, and a door to the south.''')
uu_library2 = Room('Unseen University Library', '''You're in the Unseen University Library.
The floor is glass, or possibly glass. At any rate, you can see people below you walking around, although,
strangely, they seem to be walking upside down. You're in the reading hall, which extends to the
south. There are also stairs leading up and down.''')
uu_library3 = Room('Unseen University Library - Walkway', '''You're on the upper walkway of the Unseen University Library.
The walkway extends all the way around the walls of the southern end where you're standing, and into the
northern end of the hall beyond. There are stairs leading down.''')
uu_library4 = Room('Unseen University Library - Walkway', '''You're on the upper walkway of the Unseen University Library.
The walkway extends all the way around the walls of the northern end where you're standing, and into the
southern end of the hall beyond. There are stairs leading down.''')


#WTNV Library
wtnv_library1 = Room("Night Vale Public Library", '''You're in a long, narrow, dimly-lit room with immensely high bookshelves. You seem to be in the
biography section, as on the nearest shelf you can see three shelves full of copies of the official biography
of Helen Hunt. Tragically, this section of the library seems to lack both librarian repellant dispensers
and trees. I would get out of here as soon as possible if I were you, as you probably don't want to meet the
librarians in this particular library. There is a door to the north.''')
wtnv_library2 = Room("Night Vale Public Library", '''Phew! You've cleverly avoided the librarians by climbing the stacks. They'll *never* look for you
up here, I'm sure. This is quite a comfy perch, really. You could theoretically see quite far over the
stacks, if the lighting weren't so terrible. Unfortunately, you'll have to go down at some point, as there
is nowhere else to go.''')


#Stilken Room
stilken_room1 = Room("Oak Room", '''This is an immensely peaceful room, without a book in sight. The floor is tiled, except for the center,
which is home to a pleasant (if small) meadow and a large oak tree, as well as a small silver pool. A narrow
gate is open to the east (too small for a human), and a door to the west.''', True)
stilken_room2 = Room("Glass Floor Room", '''There is a glass floor in this room, and a low stone table in the middle. The only exit is a
narrow gate to the west, too small for a human.''')


#Name of the Rose Labyrinth
#Eastern Tower
labyrinth1 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is heptagonal, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the northwest, east, and south, and stairs leading down.''')
labyrinth2 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is roughly rectangular. There's an
altar below the window. There are doors to the northwest and west.''')
labyrinth3 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Obscuratus est sol et aer." There are doors to the west and southeast.''')
labyrinth4 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Facta est grandi et ignis." There are doors to the east, southeast, and southwest.''')
labyrinth5 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "U*." There are doors to the northeast and west.''') #unfinished inscription (U)
labyrinth6 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "D*." There are doors to the west, southeast, and south.''') #unfinished inscription (D)
labyrinth7 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Super thronos viginti quatuor." There are doors to the east and northwest.''')
labyrinth8 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "V*." There are doors to the north and west.''') #unfinished inscription (V)
labyrinth12 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north and east.''')
labyrinth13 = Labyrinth("Labyrinth Room - Eastern Tower", '''You're in a room in the eastern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the north, east, and south.''')

#Between East and South
labyrinth9 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the east and south towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Gratia vobis et pax." There are doors to the north, northwest, and southwest.''')
labyrinth10 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the east and south towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Y*." There is a door to the northeast.''') #unfinished inscription (Y)
labyrinth11 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the east and south towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the southeast and southwest.''')
labyrinth14 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the east and south towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Primogenitus mortuorum." There are doors to the northeast and south.''')

#Southern Tower
labyrinth15 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Tertia pars terrae combusta est." There are doors to the east and south.''')
labyrinth16 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "U*." There are doors to the north, west, and southeast.''') #unfinished inscription (U)
labyrinth17 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "L*." There are doors to the northwest and south.''') #unfinished inscription (L)
labyrinth18 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the north and southwest.''')
labyrinth19 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Obscuratus est sol et aer." There are doors to the northeast and northwest.''')
labyrinth20 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Nomen illi mors." There are doors to the north and southeast.''')
labyrinth21 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the northeast and south.''')
labyrinth22 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "Super thronos viginti quatuor." There are doors to the north, east, west, and southwest,
and a mirror on the southeast wall with the same inscription written over it.''')
labyrinth23 = Labyrinth("Labyrinth Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Y*." There is a door to the south.''') #unfinished inscription (Y)
finis_africae = Labyrinth("Hidden Room - Southern Tower", '''You're in a room in the southern tower of the labyrinth. This one is heptagonal. There's a door to the northwest.''', True)

#Between South and West
labyrinth24 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the south and west towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Primogenitus mortuorum." There are doors to the northeast and east.''')
labyrinth25 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the south and west towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Requiescant a laboribus suis." There are doors to the northwest and southwest.''')
labyrinth26 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the south and west towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Obscuratus est sol et aer." There are doors to the southeast and southwest.''')
labyrinth27 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the south and west towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north and northeast.''')

#West Tower
labyrinth28 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "Nomen illi mors." There are doors to the north, east, west, and southwest.''')
labyrinth29 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Requiescant a laboribus suis." There are doors to the northeast and west.''')
labyrinth30 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There are doors to the northeast and east.''')
labyrinth31 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is heptagonal, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There is a door to the southwest.''')
labyrinth32 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "In diebu illis." There are doors to the northwest and south.''')
labyrinth33 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "H*." There are doors to the southeast and west.''') #unfinished inscription (H)
labyrinth34 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the east and southwest.''')
labyrinth35 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "B*." There is a door to the northeast.''') #unfinished inscription (B)
labyrinth36 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "M*." There are doors to the north and west.''') #unfinished inscription (M)
labyrinth37 = Labyrinth("Labyrinth Room - Western Tower", '''You're in a room in the western tower of labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north and south.''')

#Between West and North
labyrinth38 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the west and north towers. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the northeast, northwest, and south.''')
labyrinth39 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the west and north towers. This one is roughly rectangular, and the inscription above
one of the archways reads "L*." There is a door to the southeast.''') #unfinished inscription (L)
labyrinth40 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the west and north towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north, northwest, and southwest.''')
labyrinth41 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the west and north towers. This one is roughly rectangular, and the inscription above
one of the archways reads "L*." There is a door to the southeast.''') #unfinished inscription (L)

#North Tower
labyrinth42 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Gratia vobis et pax." There are doors to the north and west.''')
labyrinth43 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "M*." There are doors to the northeast, northwest, east, and south.''') #unfinished inscription (M)
labyrinth44 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the north and southeast.''')
labyrinth45 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "L*." There is a door to the south.''') #unfinished inscription (L)
labyrinth46 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is heptagonal, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the north, east, and southwest.''')
labyrinth47 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Gratia vobis et pax." There is a door to the south.''')
labyrinth48 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the north and west.''')
labyrinth49 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Nomen illi mors." There is a door to the south.''')
labyrinth50 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is pentagonal, and the inscription above
one of the archways reads "Requiescant a laboribus suis." There are doors to the east and west.''')
labyrinth51 = Labyrinth("Labyrinth Room - Northern Tower", '''You're in a room in the northern tower of the labyrinth. This one is roughly rectangular, and the inscription above
one of the archways reads "Equus albus." There is a door to the east.''')

#Between North and East
labyrinth52 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the north and east towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the west, southeast, and southwest.''')
labyrinth53 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the north and east towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Cecidit de cielo stella magna." There are doors to the northeast and west.''')
labyrinth54 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the north and east towers. This one is roughly rectangular, and the inscription above
one of the archways reads "In diebu illis." There are doors to the northwest and southwest.''')
labyrinth55 = Labyrinth("Labyrinth Room", '''You're in a room in the labyrinth between the north and east towers. This one is roughly rectangular, and the inscription above
one of the archways reads "Apocalypsis Iesu Christi." There are doors to the northeast and south.''')


#Room Directions
reading_room.add_directions({'s': librarian_alcove, 'w': hall1})
librarian_alcove.add_directions({'n': reading_room, 'w': binding_room, 'e': robing_room, 's': upper_librarian_hallway})
binding_room.add_directions({'e': librarian_alcove})
robing_room.add_directions({'w': librarian_alcove})
upper_librarian_hallway.add_directions({'s': chiefs_office, 'n': librarian_alcove, 'd': middle_librarian_hallway})
middle_librarian_hallway.add_directions({'u': upper_librarian_hallway, 'd': lower_librarian_hallway, 'e': second_assistant_study})
second_assistant_study.add_directions({'w': middle_librarian_hallway})
lower_librarian_hallway.add_directions({'u': middle_librarian_hallway, 'se': third_assistant_study})
third_assistant_study.add_directions({'w': lower_librarian_hallway})

hall1.add_directions({'e': reading_room, 'w': hall2})
hall2.add_directions({'e': hall1, 'w': hall3})
hall3.add_directions({'e': hall2, 's': hall4, 'w':beast_library1})
hall4.add_directions({'n': hall3, 's': hall5})
hall5.add_directions({'n': hall4, 's': hall6})
hall6.add_directions({'e': hall7, 'n': hall5})
hall7.add_directions({'e': hall8, 'w': hall6})
hall8.add_directions({'e': hall9, 'w': hall7, 's': wtnv_library1})
hall9.add_directions({'n': hall10, 'w': hall8})
hall10.add_directions({'n': hall11, 's': hall9})
hall11.add_directions({'n': hall12, 's': hall10})
hall12.add_directions({'w': hall13, 's': hall11})
hall13.add_directions({'e': hall12, 'w': hall14, 'n': uu_library1})
hall14.add_directions({'e': hall13, 's': hall15})
hall15.add_directions({'n': hall14, 's': hall16})
hall16.add_directions({'n': hall15, 'e': hall17})
hall17.add_directions({'e': hall18, 'w': hall16})
hall18.add_directions({'n': hall19, 'w': hall17})
hall19.add_directions({'n': hall20, 's': hall18})
hall20.add_directions({'w': hall21, 's': hall19})
hall21.add_directions({'e': hall20, 's': hall22, 'w': labyrinth1})
hall22.add_directions({'e': hall23, 'n': hall21})
hall23.add_directions({'w': hall22, 'n': hall24, 'e': stilken_room1})
hall24.add_directions({'s': hall23})

beast_library1.add_directions({'e': hall3, 's': beast_library2, 'n': beast_library4})
beast_library2.add_directions({'n': beast_library1, 'u': beast_library3})
beast_library3.add_directions({'d': beast_library2})
beast_library4.add_directions({'s': beast_library1, 'u': beast_library5})
beast_library5.add_directions({'d': beast_library4})

uu_library1.add_directions({'s': hall13, 'n': uu_library2, 'u': uu_library3, 'd': uu_library1})
uu_library2.add_directions({'s': uu_library1, 'u': uu_library4, 'd': uu_library2})
uu_library3.add_directions({'d': uu_library1, 'n': uu_library4})
uu_library4.add_directions({'d': uu_library2, 's': uu_library3})

wtnv_library1.add_directions({'n': hall8, 'u': wtnv_library2})
wtnv_library2.add_directions({'d': wtnv_library1})

stilken_room1.add_directions({'w': hall23, 'e': stilken_room2})
stilken_room2.add_directions({'w': stilken_room1})

labyrinth1.add_directions({'e': labyrinth2, 'nw': labyrinth4, 's': labyrinth8, 'd': hall21})
labyrinth2.add_directions({'w': labyrinth1, 'nw': labyrinth3})
labyrinth3.add_directions({'se': labyrinth2, 'w': labyrinth4})
labyrinth4.add_directions({'e': labyrinth3, 'se': labyrinth1, 'sw': labyrinth5})
labyrinth5.add_directions({'ne': labyrinth4, 'w': labyrinth13})
labyrinth6.add_directions({'se': labyrinth7, 'w': labyrinth12, 's': labyrinth9})
labyrinth7.add_directions({'nw': labyrinth6, 'e': labyrinth8})
labyrinth8.add_directions({'w': labyrinth7, 'n': labyrinth1})
labyrinth9.add_directions({'n': labyrinth6, 'nw': labyrinth11, 'sw': labyrinth10})
labyrinth10.add_directions({'ne': labyrinth9})
labyrinth11.add_directions({'se': labyrinth9, 'sw': labyrinth14})
labyrinth12.add_directions({'e': labyrinth6, 'n': labyrinth13})
labyrinth13.add_directions({'n': labyrinth55, 's': labyrinth12, 'e': labyrinth5})
labyrinth14.add_directions({'ne': labyrinth11, 's': labyrinth15})
labyrinth15.add_directions({'e': labyrinth14, 's': labyrinth16})
labyrinth16.add_directions({'n': labyrinth15, 'w': labyrinth22, 'se': labyrinth17})
labyrinth17.add_directions({'nw': labyrinth16, 's': labyrinth18})
labyrinth18.add_directions({'n': labyrinth17, 'sw': labyrinth19})
labyrinth19.add_directions({'ne': labyrinth18, 'nw': labyrinth20})
labyrinth20.add_directions({'se': labyrinth19, 'n': labyrinth21})
labyrinth21.add_directions({'s': labyrinth20, 'ne': labyrinth22})
labyrinth22.add_directions({'n': labyrinth23, 'e': labyrinth16, 'sw': labyrinth21, 'w': labyrinth24, 'se': finis_africae})
labyrinth23.add_directions({'s': labyrinth22})
labyrinth24.add_directions({'e': labyrinth22, 'ne': labyrinth25})
labyrinth25.add_directions({'sw': labyrinth24, 'nw': labyrinth26})
labyrinth26.add_directions({'se': labyrinth25, 'sw': labyrinth27})
labyrinth27.add_directions({'ne': labyrinth26, 'n': labyrinth28})
labyrinth28.add_directions({'e': labyrinth36, 's': labyrinth27, 'n': labyrinth32, 'sw': labyrinth29})
labyrinth29.add_directions({'ne': labyrinth28, 'w': labyrinth30})
labyrinth30.add_directions({'e': labyrinth29, 'ne': labyrinth31})
labyrinth31.add_directions({'sw': labyrinth30})
finis_africae.add_directions({'nw': labyrinth22})
labyrinth32.add_directions({'s': labyrinth28, 'nw': labyrinth33})
labyrinth33.add_directions({'se': labyrinth32, 'w': labyrinth34})
labyrinth34.add_directions({'e': labyrinth33, 'sw': labyrinth35})
labyrinth35.add_directions({'ne': labyrinth34})
labyrinth36.add_directions({'w': labyrinth28, 'n': labyrinth37})
labyrinth37.add_directions({'s': labyrinth36, 'n': labyrinth38})
labyrinth38.add_directions({'s': labyrinth37, 'ne': labyrinth40, 'nw': labyrinth39})
labyrinth39.add_directions({'se': labyrinth38})
labyrinth40.add_directions({'sw': labyrinth38, 'nw': labyrinth41, 'n': labyrinth42})
labyrinth41.add_directions({'se': labyrinth40})
labyrinth42.add_directions({'w': labyrinth40, 'n': labyrinth43})
labyrinth43.add_directions({'s': labyrinth42, 'e': labyrinth50, 'ne': labyrinth46, 'nw': labyrinth44})
labyrinth44.add_directions({'se': labyrinth43, 'n': labyrinth45})
labyrinth45.add_directions({'s': labyrinth44})
labyrinth46.add_directions({'sw': labyrinth43, 'n': labyrinth47, 'e': labyrinth48})
labyrinth47.add_directions({'s': labyrinth46})
labyrinth48.add_directions({'w': labyrinth46, 'n': labyrinth49})
labyrinth49.add_directions({'s': labyrinth48})
labyrinth50.add_directions({'w': labyrinth43, 'e': labyrinth52})
labyrinth51.add_directions({'e': labyrinth53})
labyrinth52.add_directions({'w': labyrinth50, 'se': labyrinth54, 'sw': labyrinth53})
labyrinth53.add_directions({'ne': labyrinth52, 'w': labyrinth51})
labyrinth54.add_directions({'nw': labyrinth52, 'sw': labyrinth55})
labyrinth55.add_directions({'ne': labyrinth54, 's': labyrinth13})
