import formatting

directory = {}
labyrinths = []

opposite_directions = {'e': 'w', 'w': 'e', 'n': 's', 's': 'n', 'u': 'd',
'd': 'u', 'ne': 'sw', 'sw': 'ne', 'nw': 'se', 'se': 'nw'}

class Room(object):
    def __init__(self, short_name=None, name=None, description=None,
        directions=None, inventory=None, npc=None, locked=False,
        locked_description='''That door's locked. And it'll stay locked no
matter how many times you tug on the handle, so stop trying.''',
        secondary_description=None, check_banana=False):
        self.short_name = short_name
        self.name = name
        self.description = description

        if directions == None:
            self.directions = {}
        else:
            self.directions = directions

        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

        self.npc = npc
        self.locked = locked
        self.counter = 0
        self.locked_description = locked_description
        self.secondary_description = secondary_description
        #secondary_description = a full description of the room to replace it
        #when an event has happened (ex: putting out the Alexandria fire).
        self.check_banana = check_banana
        directory[short_name] = self

    #I can get rid of this now:
    def add_directions(self, **kwargs):
        for direction, room in kwargs.iteritems():
            self.directions[str(direction)] = room.short_name

        for direction in self.directions.keys():
            if self.name == 'Unseen University Library' and direction == 'd':
                pass
            else:
                next_room = directory[self.directions[direction]]
                opposite = opposite_directions[direction]
                next_room.directions[opposite] = self.short_name

    def describe(self):
        room_description = {'header':self.name, 'text': [self.description]}

        if self.counter == 1 and self.secondary_description:
            room_description['text'] = self.secondary_description

        if self.inventory:
            room_description['inventory'] = formatting.list_items(self.inventory)

        if self.npc != None:
            room_description['npc'] = formatting.print_npc(self.npc, 'room') + ' is here.'

        return room_description

    def unlock(self):
        self.locked = False

    def add_counter(self):
        self.counter = 1

    def add_invent(self, item):
        self.inventory.append(item)

    def remove_invent(self, item):
        self.inventory.remove(item)

    #unused:
    def go_to_hospital(self):
        output = '''You hear a massive CRASH from the direction of the Restricted
Section. The next minute, a gurney rushes by you with Madame Pince lying on it,
her arm thrown dramatically over her eyes.'''
        hall15.counter = 1
        restricted.unlock()
        return output


class Labyrinth(Room):
    def __init__(self, *args, **kwargs):
        super(Labyrinth, self).__init__(*args, **kwargs)
        labyrinths.append(self.short_name)


#Rooms Inits
#Main Clayr Library
outside_of_library = Room("outside_of_library", "Outside the Library", '', locked=True,
    locked_description='''No, I really don't think you want to go that way. Why
don't you stick to the library?''')
reading_room = Room('reading_room', "Reading Room",
    '''You're in the Main Reading Room. Large wooden tables fill the room.
There are exits to the south and west. The main doors are open to the east.''')
librarian_alcove = Room('librarian_alcove', "Librarian Alcove",
    '''This is the librarian alcove, the main hub of their behind-the-scenes
library management. There is a small roller-top desk in the corner. There are
exits to the north, south, east, and west.''', inventory=['ledger', 'scissors'])
#possibly open the desk?
binding_room = Room('binding_room', "Binding Room",
    '''This is the room where the librarians repair damaged books. There are
books covering every flat surface, and a giant press in the back corner. The
only exit is to the east.''', inventory=['wire'], npc='clippy')
robing_room = Room('robing_room', "Robing Room",
    '''You're in a room full of miscellaneous useful things. Boat hooks,
climbing ropes, and weapons line the walls. The only exit is to the west.''',
inventory=['fairy tale book'])
upper_librarian_hallway = Room('upper_librarian_hallway', "Upper Hallway",
    '''You're standing in a hallway, in the employees-only librarians' wing of
the library. Painted blue doors line the hallway, but they're all closed and
locked. There's a door at the south end of the hallway. There's an exit to the
north, and steps leading down.''')
chiefs_office = Room('chiefs_office', "Chief Librarian Vancelle's Office",
    '''This is Chief Librarian Vancelle's office. It's a roomy, wood-panelled
office. Chief Librarian Vancelle is obviously not the tidiest person; papers
and books are stacked willy-nilly on her desk. She's nice enough, but I
wouldn't like to get caught in her office without her permission. The only exit
is to the north.''', npc='vancelle')
middle_librarian_hallway = Room('middle_librarian_hallway', "Middle Hallway",
    '''You're standing in a hallway. All of the doors are painted red. They're
all closed and locked. There are stairs leading up and down.''', npc='imshi')
second_assistant_study = Room('second_assistant_study', "Second Assistant Study",
    '''This is your new study, the room of a Second Assistant Librarian.
There's enough room for a desk and not one but two chairs (what luxury!), and
there's a door ajar that leads to a tiny bathroom, all your own. The only exit
is to the west.''', inventory=['statue', 'red waistcoat'], locked=True)
lower_librarian_hallway = Room('lower_librarian_hallway', "Lower Hallway",
    '''You're standing in a hallway. There are many doors adjacent to this
hallway, more than the two upper floors. The doors are all painted yellow.
They're all closed, except for the one in the southeastern corner. There are
also stairs leading up.''')
third_assistant_study = Room('third_assistant_study', "Third Assistant Study",
    '''This is your study. It's very cramped; there's barely room for the desk
and single chair that are here. The only exit is to the northwest.''',
inventory=['mouse', 'key', 'yellow waistcoat', 'dagger'],
secondary_description='''This is your old study. It's quite cramped. Hard to believe that you spent
so much time in this tiny room! The only exit is to the northwest.''')

#Main Ramp Rooms (Clayr Library Spiral)
hall1 = Room('hall1', "East-West Hallway",
    '''You're in a hallway with gently sloping floors. Through the eastern
archway, you can see the Main Reading Room. The walls here are blue. There are
archways to the east and west.''')
hall2 = Room('hall2', "East-West Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the east and west.''')
hall3 = Room('hall3', "East-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There is a table in the corner with a rose lying on it. There are archways to
the east and south, and a stained-glass door to the west.''', inventory=['french book'])

hall4 = Room('hall4', "North-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall5 = Room('hall5', "North-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall6 = Room('hall6', "North-East Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There is a large statue of a turtle in the corner. There are archways to the
north and east.''')

hall7 = Room('hall7', "East-West Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the east and west.''')
hall8 = Room('hall8', "East-West Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There is a strange painting on the wall of faceless people going up and down
impossible stairways. There are archways to the east and west, and a door
with two emeralds over it to the south.''')
hall9 = Room('hall9', "North-West Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There is a large statue of an elephant in the corner. There are archways to the
north and west.''')

hall10 = Room('hall10', "North-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south. There is a door with two emeralds
over it to the west, flanked by two stone columns topped with papyrus-patterned
capitals.''')
hall11 = Room('hall11', "North-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are blue.
There are archways to the north and south.''')
hall12 = Room('hall12', "West-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are
purple. There are archways to the west and south.''')

hall13 = Room('hall13', "East-West Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the east and west.''')
hall14 = Room('hall14', "East-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the east and south.''', check_banana=True)

hall15 = Room('hall15', "North-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and south, and a velvet rope sealed with
Vancelle's official seal blocking a door to the west. Next to the door, there's
a sign posted: "RESTRICTED. Do not enter without Madame Pince's permission."''',
secondary_description='''You're in a hallway with gently sloping floors. The walls here are red.
There's a velvet rope piled neatly in the corner. There are archways to the
north and south, and a door to the west. Next to the door, there's a sign posted:
"RESTRICTED. Do not enter without Madame Pince's permission."''')
hall16 = Room('hall16', "North-East Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and east.''', check_banana=True)

hall17 = Room('hall17', "East-West Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the east and west.''')
hall18 = Room('hall18', "North-West Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are red.
There are archways to the north and west.''')

hall19 = Room('hall19', "North-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are red.
There is an empty soap dispenser on the wall labeled "Librarian Repellent."
There are archways to the north and south, and a door to the north with two
emeralds over it.''')
hall20 = Room('hall20', "West-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are
orange. There are archways to the west and south.''')

hall21 = Room('hall21', "East-South Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are
yellow. On the wall, there's a very old and very inaccurate world map. (Who
ever heard of a place called Leones?!) There are archways to the east and south
and stairs leading up. There are two emeralds set in the ceiling over the
stairs.''')

hall22 = Room('hall22', "North-East Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are
yellow. There are archways to the north and east.''')

hall23 = Room('hall23', "North-West Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are
yellow. There are archways to the north and west. There's a door with a
sunburst painted on it to the east, and four emeralds set in the wall above
it.''')

hall24 = Room('hall24', "Hallway",
    '''You're in a hallway with gently sloping floors. The walls here are
yellow. There's an archway to the south. On the west wall, there's a hole, far
too small for a human to pass through.''', inventory=['floral book'])


#Beast's Library
beast_library1 = Room('beast_library1', "Beast's Library",
    '''You're in a huge room filled floor to 50-foot ceiling with books, with
tall windows in the southwest and northwest corners. The room extends to the
north and south, and there's a door to the east.''')
beast_library2 = Room('beast_library2', "Beast's Library",
    '''You're in the southern end of a massive library. It extends to the
north, and there's a staircase going up in the corner.''', inventory=['banana'])
beast_library3 = Room('beast_library3', "Beast's Library - South Walkway",
    '''You're standing on a walkway about halfway up the southern wall of a
massive library. There are stairs leading down.''', npc='lumiere')
beast_library4 = Room('beast_library4', "Beast's Library",
    '''You're in the northern end of a massive library. It extends to the
south, and there's a staircase going up in the corner.''')
beast_library5 = Room('beast_library5', "Beast's Library - North Walkway",
    '''You're standing on a walkway about halfway up the northern wall of a
massive library. There are stairs leading down.''', npc='cogsworth')
beast_library = [beast_library1.short_name, beast_library2.short_name,
    beast_library3.short_name, beast_library4.short_name,
    beast_library5.short_name]


#Unseen University Library
uu_library1 = Room('uu_library1', 'Unseen University Library',
    '''You're in the prestigiously distinguished and esteemed Unseen University
Library. It is just as officious-looking as you'd expect of such a
prestigiously distinguished and esteemed library; the walls are covered with
cherry panelling, in the rare instances that they aren't covered in books. The
floor is glass, or possibly glass. At any rate, you can see people below you
walking around, although, strangely, they seem to be walking upside down.
You're in the reading hall, which extends to the north before ending in a
massive window that takes up the entire northen wall. There are also stairs
leading up and down, and a door to the south.''', npc='orangutan', locked=True)
uu_library2 = Room('uu_library2', 'Unseen University Library',
    '''You're in the Unseen University Library. The floor is glass, or possibly
glass. At any rate, you can see people below you walking around, although,
strangely, they seem to be walking upside down. You're in the reading hall,
which extends to the south. There are also stairs leading up and down.''')
uu_library3 = Room('uu_library3', 'Unseen University Library - Walkway',
    '''You're on the upper walkway of the Unseen University Library. The
walkway extends all the way around the walls of the southern end where you're
standing, and into the northern end of the hall beyond. There are stairs
leading down.''')
uu_library4 = Room('uu_library4', 'Unseen University Library - Walkway',
    '''You're on the upper walkway of the Unseen University Library. The
walkway extends all the way around the walls of the northern end where you're
standing, and into the southern end of the hall beyond. There are stairs
leading down.''', inventory=['princess book'])
uu_libraries = [uu_library1.short_name, uu_library2.short_name,
    uu_library3.short_name, uu_library4.short_name]

#Alexandria
alexandria1 = Room('alexandria1', 'Royal Library of Alexandria - Reading Room',
    '''This is a beautiful reading room with high ceilings and columns
everywhere. Bookshelves line the walls. But there's a huge fire in the middle
of the room! It's spread to the far side of the room, covering the doors you
can see in the other three walls. The only safe exit is to go back through the
door east.''', secondary_description=
'''This is a beautiful reading room with high ceilings and columns everywhere.
Bookshelves line the walls, and the room seems kind of smoky. There are doors
to the north, east, and west.''', locked=True, inventory=['translation book'])
alexandria2 = Room('alexandria2', 'Royal Library of Alexandria - Peripatos Walk',
    '''You're in a long, covered walkway between two "buildings." There are
gardens to either side of the walkway, but no doors to get there. You can see
sky beyond the roof above you, which is strange since you know you're still
underground. But it's quite convincing; you can hear birds and everything.
There are doors to the north and south.''', locked=True,
locked_description='''Since there's a giant fire in front of the door, I'm
going to pretend you didn't just try to go in that direction.''',
inventory=['magic book'])
alexandria3 = Room('alexandria3', 'Royal Library of Alexandria - Meeting Room',
    '''This is a small but welcoming meeting room. There's a large sturdy stone
table in the center, surrounded by wooden chairs. There are doors to the
southeast, southwest, and south.''')
alexandria4 = Room('alexandria4', 'Royal Library of Alexandria - Gardens',
    '''You're in a small but full garden. You know it's a fake sky, but the sky
overhead is quite convincing and beautifully blue. You can feel the sunlight
on your face, and there are birds in the carefully maintained shrubs. There are
paths leading to the northeast and south.''')
alexandria5 = Room('alexandria5', 'Royal Library of Alexandria - Gardens',
    '''You're in a small but full garden. You know it's a fake sky, but the sky
overhead is quite convincing and beautifully blue. You can feel the sunlight
on your face, and there are birds in the carefully maintained shrubs. There is
a path leading to the northwest.''')
alexandria6 = Room('alexandria6', 'Royal Library of Alexandria - Lecture Hall',
    '''This is a large lecture hall. There are steps leading down to a lectern
at the front of the room. There are doors to the north and east.''',
locked=True,
locked_description='''Since there's a giant fire in front of the door, I'm
going to pretend you didn't just try to go in that direction.''')
alexandria = [alexandria1.short_name, alexandria2.short_name,
    alexandria3.short_name, alexandria4.short_name, alexandria5.short_name,
    alexandria6.short_name]

#Restricted Section (HP)
restricted = Room('restricted', 'Restricted Section',
    '''You're in the restricted section of an obviously magical library. There
are aisles of bookshelves with a shelf at hip-level to be used as desks, and
study tables next to the floor-length windows. The only exit is to the east.''',
locked=True,
locked_description='''This is Madam Pince's territory and it's CLEARLY
off-limits, so I'm going to pretend you didn't just try to do that. You're
welcome for saving you from that hell, although you obviously don't deserve
it. *coughidiotcough*''', inventory=['diary', 'western book'])


#WTNV Library
wtnv_library1 = Room('wtnv_library1', "Night Vale Public Library - Entrance",
    '''You're in a long, narrow, dimly-lit room with immensely high
bookshelves. You seem to be in the biography section, as on the nearest shelf
you can see three shelves full of copies of the official biography of Helen
Hunt. Tragically, this section of the library seems to lack both librarian
repellant dispensers and trees. I would get out of here as soon as possible if
I were you, as you probably don't want to meet the librarians in this
particular library. There are doors to the north, east, and west.''',
locked=True, inventory=['dark history book'])
wtnv_library2 = Room('wtnv_library2', 'Night Vale Public Library - Northwest Corner',
    '''You're in a long, narrow, dimly-lit room with immensely high
bookshelves. You thought you'd left the biography section, but one of the
nearby shelves has yet more copies of the official biography of Helen Hunt.
Tragically, this section of the library seems to lack both librarian repellant
dispensers and trees. I would get out of here as soon as possible if I were
you, as you probably don't want to meet the librarians in this particular
library. There are doors to the east and south.''')
wtnv_library3 = Room('wtnv_library3', 'Night Vale Public Library - Northeast Corner',
    '''You're in a long, narrow, dimly-lit room with immensely high
bookshelves. There are two very old (vintage? decrepit? Pleistocene?
carbon-dated?) computers in the corner, with hand-lettered "Out of Order" signs
taped to their screens. Tragically, this section of the library seems to lack
both librarian repellant dispensers and trees. I would get out of here as soon
as possible if I were you, as you probably don't want to meet the librarians in
this particular library. There are doors to the west and south.''')
wtnv_library4 = Room('wtnv_library4', 'Night Vale Public Library - Southwest Corner',
    '''You're in a long, narrow, dimly-lit room with immensely high
bookshelves. The shelves here are completely empty. Tragically, this section
of the library seems to lack both librarian repellant dispensers and trees. I
would get out of here as soon as possible if I were you, as you probably don't
want to meet the librarians in this particular library. There are doors to the
north and east.''')
wtnv_library5 = Room('wtnv_library5', 'Night Vale Public Library - Southeast Corner',
    '''You're in a long, narrow, dimly-lit room with immensely high
bookshelves. You think this might be the horror section, as all of the books
you can see seem to be about faceless spectres. Tragically, this section of the
library seems to lack both librarian repellant dispensers and trees. I would
get out of here as soon as possible if I were you, as you probably don't want
to meet the librarians in this particular library. There are doors to the north
and west.''')
wtnv_library6 = Room('wtnv_library6', "Night Vale Public Library - Childrens' Sections",
    '''This room is shaped like a pirate ship, with a mast that almost reaches
the ceiling. Dismembered bodies cover the floor. There are doors to the east
and west.''', inventory=['astronomy book'])
wtnv_library7 = Room('wtnv_library7', "Night Vale Public Library - Crow's Nest",
    '''Phew! You've cleverly avoided the librarians by climbing the pirate
ship's crow's nest. They'll *never* look for you up here, I'm sure. This is
quite a comfy perch, really. You could theoretically see quite far over the
stacks, if the lighting weren't so terrible. Unfortunately, you'll have to go
down at some point, as there is nowhere else to go.''', inventory=['labyrinth book'])
wtnv = [wtnv_library1.short_name, wtnv_library2.short_name,
    wtnv_library3.short_name, wtnv_library4.short_name,
    wtnv_library5.short_name, wtnv_library6.short_name,
    wtnv_library7.short_name]


#Stilken Room
stilken_room1 = Room('stilken_room1', "Oak Room",
    '''This is an immensely peaceful room, without a book in sight. The floor
is tiled, except for the center, which is home to a pleasant (if small) meadow
and a large oak tree, as well as a small silver pool. A narrow gate is open to
the east (too small for a human), and a door to the west.''', locked=True,
inventory=['odyssean book'])
stilken_room2 = Room('stilken_room2', "Glass Floor Room",
    '''There is a glass floor in this room, and a low stone table in the
middle. The only exit is a narrow gate to the west, too small for a human.''',
inventory=['phial'])


#Name of the Rose Labyrinth
#Eastern Tower
labyrinth1 = Labyrinth('labyrinth1', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
heptagonal, and the inscription above one of the archways reads "Apocalypsis
Iesu Christi." There are doors to the northwest, east, and south, and stairs
leading down.''', npc='jorge', inventory=['chalk', 'potions book'])
labyrinth2 = Labyrinth('labyrinth2', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
roughly rectangular. There's an altar below the window. There are doors to the
northwest and west.''')
labyrinth3 = Labyrinth('labyrinth3', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads
"Obscuratus est sol et aer." There are doors to the west and southeast.''')
labyrinth4 = Labyrinth('labyrinth4', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "Facta
est grandi et ignis." There are doors to the east, southeast, and southwest.''')
labyrinth5 = Labyrinth('labyrinth5', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
pentagonal, and the inscription above one of the archways reads "U*." There are
doors to the northeast and west.''') #unfinished inscription (U)
labyrinth6 = Labyrinth('labyrinth6', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
pentagonal, and the inscription above one of the archways reads "D*." There are
doors to the west, southeast, and south.''') #unfinished inscription (D)
labyrinth7 = Labyrinth('labyrinth7', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "Super
thronos viginti quatuor." There are doors to the east and northwest.''')
labyrinth8 = Labyrinth('labyrinth8', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "V*."
There are doors to the north and west.''') #unfinished inscription (V)
labyrinth12 = Labyrinth('labyrinth12', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads
"Apocalypsis Iesu Christi." There are doors to the north and east.''')
labyrinth13 = Labyrinth('labyrinth13', "Labyrinth Room - Eastern Tower",
    '''You're in a room in the eastern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "Equus
albus." There are doors to the north, east, and south.''')

#Between East and South
labyrinth9 = Labyrinth('labyrinth9', "Labyrinth Room",
    '''You're in a room in the labyrinth between the east and south towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Gratia vobis et pax." There are doors to the north, northwest, and
southwest.''')
labyrinth10 = Labyrinth('labyrinth10', "Labyrinth Room",
    '''You're in a room in the labyrinth between the east and south towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Y*." There is a door to the northeast.''') #unfinished inscription (Y)
labyrinth11 = Labyrinth('labyrinth11', "Labyrinth Room",
    '''You're in a room in the labyrinth between the east and south towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Equus albus." There are doors to the southeast and southwest.''')
labyrinth14 = Labyrinth('labyrinth14', "Labyrinth Room",
    '''You're in a room in the labyrinth between the east and south towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Primogenitus mortuorum." There are doors to the northeast and south.''')

#Southern Tower
labyrinth15 = Labyrinth('labyrinth15', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads
"Tertia pars terrae combusta est." There are doors to the east and south.''')
labyrinth16 = Labyrinth('labyrinth16', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
pentagonal, and the inscription above one of the archways reads "U*." There are
doors to the north, west, and southeast.''') #unfinished inscription (U)
labyrinth17 = Labyrinth('labyrinth17', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "L*."
There are doors to the northwest and south.''') #unfinished inscription (L)
labyrinth18 = Labyrinth('labyrinth18', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "Equus
albus." There are doors to the north and southwest.''')
labyrinth19 = Labyrinth('labyrinth19', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads
"Obscuratus est sol et aer." There are doors to the northeast and
northwest.''')
labyrinth20 = Labyrinth('labyrinth20', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads
"Nomen illi mors." There are doors to the north and southeast.''')
labyrinth21 = Labyrinth('labyrinth21', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "Equus
albus." There are doors to the northeast and south.''')
labyrinth22 = Labyrinth('labyrinth22', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
pentagonal, and the inscription above one of the archways reads "Super thronos
viginti quatuor." There are doors to the north, east, west, and southwest, and
a mirror on the southeast wall with the same inscription written over it.''',
inventory=['south african book'])
labyrinth23 = Labyrinth('labyrinth23', "Labyrinth Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "Y*."
There is a door to the south.''') #unfinished inscription (Y)
finis_africae = Labyrinth('finis_africae', "Hidden Room - Southern Tower",
    '''You're in a room in the southern tower of the labyrinth. This one is
heptagonal. There's a door to the northwest.''', locked=True,
inventory=['drama book'])

#Between South and West
labyrinth24 = Labyrinth('labyrinth24', "Labyrinth Room",
    '''You're in a room in the labyrinth between the south and west towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Primogenitus mortuorum." There are doors to the northeast and east.''')
labyrinth25 = Labyrinth('labyrinth25', "Labyrinth Room",
    '''You're in a room in the labyrinth between the south and west towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Requiescant a laboribus suis." There are doors to the northwest and
southwest.''')
labyrinth26 = Labyrinth('labyrinth26', "Labyrinth Room",
    '''You're in a room in the labyrinth between the south and west towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Obscuratus est sol et aer." There are doors to the southeast and
southwest.''')
labyrinth27 = Labyrinth('labyrinth27', "Labyrinth Room",
    '''You're in a room in the labyrinth between the south and west towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Apocalypsis Iesu Christi." There are doors to the north and
northeast.''')

#West Tower
labyrinth28 = Labyrinth('labyrinth28', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is
pentagonal, and the inscription above one of the archways reads "Nomen illi
mors." There are doors to the north, east, west, and southwest.''')
labyrinth29 = Labyrinth('labyrinth29', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is roughly
rectangular, and the inscription above one of the archways reads "Requiescant a
laboribus suis." There are doors to the northeast and west.''')
labyrinth30 = Labyrinth('labyrinth30', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is roughly
rectangular, and the inscription above one of the archways reads "Equus albus."
There are doors to the northeast and east.''')
labyrinth31 = Labyrinth('labyrinth31', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is
heptagonal, and the inscription above one of the archways reads "Apocalypsis
Iesu Christi." There is a door to the southwest.''',
inventory=['fantasy book'])
labyrinth32 = Labyrinth('labyrinth32', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is
pentagonal, and the inscription above one of the archways reads "In diebu
illis." There are doors to the northwest and south.''')
labyrinth33 = Labyrinth('labyrinth33', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is roughly
rectangular, and the inscription above one of the archways reads "H*." There
are doors to the southeast and west.''') #unfinished inscription (H)
labyrinth34 = Labyrinth('labyrinth34', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is roughly
rectangular, and the inscription above one of the archways reads "In diebu
illis." There are doors to the east and southwest.''')
labyrinth35 = Labyrinth('labyrinth35', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is roughly
rectangular, and the inscription above one of the archways reads "B*." There is
a door to the northeast.''') #unfinished inscription (B)
labyrinth36 = Labyrinth('labyrinth36', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is roughly
rectangular, and the inscription above one of the archways reads "M*." There
are doors to the north and west.''') #unfinished inscription (M)
labyrinth37 = Labyrinth('labyrinth37', "Labyrinth Room - Western Tower",
    '''You're in a room in the western tower of labyrinth. This one is roughly
rectangular, and the inscription above one of the archways reads "Apocalypsis
Iesu Christi." There are doors to the north and south.''')

#Between West and North
labyrinth38 = Labyrinth('labyrinth38', "Labyrinth Room",
    '''You're in a room in the labyrinth between the west and north towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "In diebu illis." There are doors to the northeast, northwest, and
south.''')
labyrinth39 = Labyrinth('labyrinth39', "Labyrinth Room",
    '''You're in a room in the labyrinth between the west and north towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "L*." There is a door to the southeast.''') #unfinished inscription (L)
labyrinth40 = Labyrinth('labyrinth40', "Labyrinth Room",
    '''You're in a room in the labyrinth between the west and north towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Apocalypsis Iesu Christi." There are doors to the north, northwest, and
southwest.''')
labyrinth41 = Labyrinth('labyrinth41', "Labyrinth Room",
    '''You're in a room in the labyrinth between the west and north towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "L*." There is a door to the southeast.''') #unfinished inscription (L)

#North Tower
labyrinth42 = Labyrinth('labyrinth42', "Labyrinth Room - Northern Tower",
    '''You're in a room in the northern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads
"Gratia vobis et pax." There are doors to the north and west.''')
labyrinth43 = Labyrinth('labyrinth43', "Labyrinth Room - Northern Tower",
    '''You're in a room in the northern tower of the labyrinth. This one is
pentagonal, and the inscription above one of the archways reads "M*." There are
doors to the northeast, northwest, east, and south.''') #unfinished inscription (M)
labyrinth44 = Labyrinth('labyrinth44', "Labyrinth Room - Northern Tower",
    '''You're in a room in the northern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "In
diebu illis." There are doors to the north and southeast.''')
labyrinth45 = Labyrinth('labyrinth45', "Labyrinth Room - Northern Tower", 
    '''You're in a room in the northern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "L*."
There is a door to the south.''') #unfinished inscription (L)
labyrinth46 = Labyrinth('labyrinth46', "Labyrinth Room - Northern Tower", 
    '''You're in a room in the northern tower of the labyrinth. This one is
heptagonal, and the inscription above one of the archways reads "Apocalypsis
Iesu Christi." There are doors to the north, east, and southwest.''',
inventory=['epic book'])
labyrinth47 = Labyrinth('labyrinth47', "Labyrinth Room - Northern Tower", 
    '''You're in a room in the northern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads
"Gratia vobis et pax." There is a door to the south.''')
labyrinth48 = Labyrinth('labyrinth48', "Labyrinth Room - Northern Tower",
    '''You're in a room in the northern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "In
diebu illis." There are doors to the north and west.''')
labyrinth49 = Labyrinth('labyrinth49', "Labyrinth Room - Northern Tower", 
    '''You're in a room in the northern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "Nomen
illi mors." There is a door to the south.''')
labyrinth50 = Labyrinth('labyrinth50', "Labyrinth Room - Northern Tower", 
    '''You're in a room in the northern tower of the labyrinth. This one is
pentagonal, and the inscription above one of the archways reads "Requiescant a
laboribus suis." There are doors to the east and west.''')
labyrinth51 = Labyrinth('labyrinth51', "Labyrinth Room - Northern Tower", 
    '''You're in a room in the northern tower of the labyrinth. This one is
roughly rectangular, and the inscription above one of the archways reads "Equus
albus." There is a door to the east.''')

#Between North and East
labyrinth52 = Labyrinth('labyrinth52', "Labyrinth Room", 
    '''You're in a room in the labyrinth between the north and east towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Apocalypsis Iesu Christi." There are doors to the west, southeast, and
southwest.''')
labyrinth53 = Labyrinth('labyrinth53', "Labyrinth Room", 
    '''You're in a room in the labyrinth between the north and east towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Cecidit de cielo stella magna." There are doors to the northeast and
west.''')
labyrinth54 = Labyrinth('labyrinth54', "Labyrinth Room", 
    '''You're in a room in the labyrinth between the north and east towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "In diebu illis." There are doors to the northwest and southwest.''')
labyrinth55 = Labyrinth('labyrinth55', "Labyrinth Room", 
    '''You're in a room in the labyrinth between the north and east towers.
This one is roughly rectangular, and the inscription above one of the archways
reads "Apocalypsis Iesu Christi." There are doors to the northeast and
south.''')


#Room Directions
reading_room.add_directions(s=librarian_alcove, w=hall1, e=outside_of_library)
librarian_alcove.add_directions(w=binding_room, e=robing_room,
    s=upper_librarian_hallway)
upper_librarian_hallway.add_directions(s=chiefs_office, d=middle_librarian_hallway)
middle_librarian_hallway.add_directions(d=lower_librarian_hallway,
    e=second_assistant_study)
lower_librarian_hallway.add_directions(se=third_assistant_study)

hall1.add_directions(w=hall2)
hall2.add_directions(w=hall3)
hall3.add_directions(s=hall4, w=beast_library1)
hall4.add_directions(s=hall5)
hall5.add_directions(s=hall6) #pagemaster library
hall6.add_directions(e=hall7)
hall7.add_directions(e=hall8)
hall8.add_directions(e=hall9, s=uu_library1)
hall9.add_directions(n=hall10)
hall10.add_directions(n=hall11, w=alexandria1)
hall11.add_directions(n=hall12)
hall12.add_directions(w=hall13)
hall13.add_directions(w=hall14) #lucien
hall14.add_directions(s=hall15)
hall15.add_directions(s=hall16, w=restricted)
hall16.add_directions(e=hall17)
hall17.add_directions(e=hall18) #dw
hall18.add_directions(n=hall19)
hall19.add_directions(n=hall20, e=wtnv_library1)
hall20.add_directions(w=hall21)
hall21.add_directions(s=hall22, u=labyrinth1)
hall22.add_directions(e=hall23)
hall23.add_directions(n=hall24, e=stilken_room1)

beast_library1.add_directions(s=beast_library2, n=beast_library4)
beast_library2.add_directions(u=beast_library3)
beast_library4.add_directions(u=beast_library5)

uu_library1.add_directions(n=uu_library2, u=uu_library3, d=uu_library1)
uu_library2.add_directions(u=uu_library4, d=uu_library2)
uu_library3.add_directions(n=uu_library4)

alexandria1.add_directions(n=alexandria2, w=alexandria6)
alexandria2.add_directions(n=alexandria3)
alexandria3.add_directions(se=alexandria5, sw=alexandria4)
alexandria4.add_directions(s=alexandria6)

wtnv_library1.add_directions(e=wtnv_library3, w=wtnv_library2)
wtnv_library2.add_directions(s=wtnv_library4)
wtnv_library3.add_directions(s=wtnv_library5)
wtnv_library4.add_directions(e=wtnv_library6)
wtnv_library5.add_directions(w=wtnv_library6)
wtnv_library6.add_directions(u=wtnv_library7)

stilken_room1.add_directions(e=stilken_room2)

labyrinth1.add_directions(e=labyrinth2, nw=labyrinth4, s=labyrinth8)
labyrinth2.add_directions(nw=labyrinth3)
labyrinth3.add_directions(w=labyrinth4)
labyrinth4.add_directions(sw=labyrinth5)
labyrinth5.add_directions(w=labyrinth13)
labyrinth6.add_directions(se=labyrinth7, w=labyrinth12, s=labyrinth9)
labyrinth7.add_directions(e=labyrinth8)
labyrinth9.add_directions(nw=labyrinth11, sw=labyrinth10)
labyrinth11.add_directions(sw=labyrinth14)
labyrinth12.add_directions(n=labyrinth13)
labyrinth13.add_directions(n=labyrinth55)
labyrinth14.add_directions(s=labyrinth15)
labyrinth15.add_directions(s=labyrinth16)
labyrinth16.add_directions(w=labyrinth22, se=labyrinth17)
labyrinth17.add_directions(s=labyrinth18)
labyrinth18.add_directions(sw=labyrinth19)
labyrinth19.add_directions(nw=labyrinth20)
labyrinth20.add_directions(n=labyrinth21)
labyrinth21.add_directions(ne=labyrinth22)
labyrinth22.add_directions(n=labyrinth23, w=labyrinth24, se=finis_africae)
labyrinth24.add_directions(ne=labyrinth25)
labyrinth25.add_directions(nw=labyrinth26)
labyrinth26.add_directions(sw=labyrinth27)
labyrinth27.add_directions(n=labyrinth28)
labyrinth28.add_directions(e=labyrinth36, n=labyrinth32, sw=labyrinth29)
labyrinth29.add_directions(w=labyrinth30)
labyrinth30.add_directions(ne=labyrinth31)
labyrinth32.add_directions(nw=labyrinth33)
labyrinth33.add_directions(w=labyrinth34)
labyrinth34.add_directions(sw=labyrinth35)
labyrinth36.add_directions(n=labyrinth37)
labyrinth37.add_directions(n=labyrinth38)
labyrinth38.add_directions(ne=labyrinth40, nw=labyrinth39)
labyrinth40.add_directions(nw=labyrinth41, n=labyrinth42)
labyrinth42.add_directions(n=labyrinth43)
labyrinth43.add_directions(e=labyrinth50, ne=labyrinth46, nw=labyrinth44)
labyrinth44.add_directions(n=labyrinth45)
labyrinth46.add_directions(n=labyrinth47, e=labyrinth48)
labyrinth48.add_directions(n=labyrinth49)
labyrinth50.add_directions(e=labyrinth52)
labyrinth51.add_directions(e=labyrinth53)
labyrinth52.add_directions(se=labyrinth54, sw=labyrinth53)
labyrinth54.add_directions(sw=labyrinth55)
labyrinth55.add_directions(ne=labyrinth54)
