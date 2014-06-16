import unittest
from nose.tools import eq_

import library_world.rooms as rooms
import library_world.commands as commands
import library_world.people as people
from library_world.player import player, home

class TestCommands(unittest.TestCase):
    def tearDown(self):
        player.inventory = []
        player.location = home
        player.level = 1
        player.shelved_books = set()
        rooms.third_assistant_study.inventory = ['mouse', 'key',
            'yellow waistcoat', 'dagger']

    def test_look(self):
        player.location = rooms.binding_room
        output = commands.command((['look']), player)
        binding_room_dict = {'header': 'Binding Room',
        'text': ['''This is the room where the librarians repair damaged books. There are
books covering every flat surface, and a giant press in the back corner. The
only exit is to the east.'''], 'npc': 'Clippy is here.',
    'inventory': 'There is a wire here.'}
        eq_(output, binding_room_dict)

    def test_talk_normal_NPC(self):
        player.location = rooms.middle_librarian_hallway
        output = commands.command((['talk', 'imshi']), player)
        self.assertIn(output, people.imshi.dialogue)

    def test_talk_vancelle(self):
        player.location = rooms.chiefs_office
        output = commands.command((['talk', 'vancelle']), player)
        vancelle_dialogue = {'header': '"You need to shelve these books to get to level 2:"',
            'text': ['french book']}
        eq_(output, vancelle_dialogue)

    def test_vancelle_level_up(self):
        player.take('key')
        player.shelved_books = set(('french book',))
        player.location = rooms.chiefs_office
        output = commands.command((['talk', 'vancelle']), player)
        vancelle_dialogue = {'header':
            '"Congratulations, you\'ve shelved your first book. Now go do the rest. You need to shelve these books to get to level 3:"',
            'text': ['floral book', 'fairy tale book', 'princess book'],
            'event': '''Level up! You're now level 2.'''}
        eq_(output, vancelle_dialogue)

    def test_take_all(self):
        player.location = rooms.third_assistant_study
        output = commands.command((['take', 'all']), player)
        eq_(output, {'text': ['You take the mouse.', 'You take the key.',
            'You take the yellow waistcoat.', 'You take the dagger.']})

class TestEvents(unittest.TestCase):
    def tearDown(self):
        player.location = home
        player.inventory = []

    def test_uu_down_under(self):
        player.location = rooms.uu_library1
        output = commands.command((['d']), player)
        uu_dict = rooms.uu_library1.describe()
        uu_dict['event'] = '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
and down is up. But now it's gone, so you don't trouble yourself over it.'''
        eq_(output, uu_dict)

    def test_banana_peel_true(self):
        rooms.hall15.add_invent('banana')
        player.location = rooms.hall15
        output = commands.command((['n']), player)
        hall14_dict = rooms.hall14.describe()
        hall14_dict['event'] = '''You hear a massive CRASH from the direction of the Restricted
Section. The next minute, a gurney rushes by you with Madame Pince lying on it,
her arm thrown dramatically over her eyes.'''
        eq_(output, hall14_dict)
        eq_(rooms.restricted.locked, False)
        eq_(rooms.hall15.describe()['text'], rooms.hall15.secondary_description)

    def test_banana_peel_false(self):
        player.location = rooms.hall15
        output = commands.command((['n']), player)
        eq_(output, rooms.hall14.describe())

    def test_break_seal(self):
        player.inventory = ['fairy tale book', 'french book', 'diary',
            'yellow waistcoat', 'key', 'scissors']
        player.location = rooms.hall15
        output = commands.command((['break', 'rope']), player)
        reading_room_dict = rooms.reading_room.describe()
        reading_room_dict['event'] = '''As you poise the scissors to cut through the rope, Madam Pince
appears seemingly out of nowhere, screeching at the top of her lungs. "WHAT DO
YOU THINK YOU'RE DOING?! Disrespecting library property! Out out out!" She
promptly confiscates all your books, and to add insult to injury, she escorts
you all the way back to the main reading room.'''
        eq_(output, reading_room_dict)
        eq_(player.inventory, ['scissors', 'key', 'yellow waistcoat'])

class TestInitialStates(unittest.TestCase):
    def test_home(self):
        output = commands.command((['teleport']), player)
        eq_(output, rooms.reading_room.describe())

    def test_inventory(self):
        output = commands.command((['i']), player)
        eq_(output, "You're not holding anything!")

    def test_level_shelved_books(self):
        output = commands.command((['level']), player)
        first_level_dict = {'header':
            'You are level 1. You have shelved these books:', 'text': []}
        eq_(output, first_level_dict)

    def test_known_spells(self):
        output = commands.command((['spells']), player)
        eq_(output, "You don't know any spells.")

