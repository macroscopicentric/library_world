import unittest
from nose.tools import eq_

import library_world.rooms as rooms
import library_world.commands as commands
import library_world.people as people
from library_world.player import player

class TestCommands(unittest.TestCase):
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
    def test_banana_peel(self):
        rooms.hall15.add_invent('banana')
        player.location = rooms.hall15
        output = commands.command((['n']), player)
        hall14_dict = rooms.hall14.describe()
        hall14_dict['event'] = '''You hear a massive CRASH from the direction of the Restricted
Section. The next minute, a gurney rushes by you with Madame Pince lying on it,
her arm thrown dramatically over her eyes.'''
        eq_(output, hall14_dict)

class TestInitialStates(unittest.TestCase):
    def test_home(self):
        output = commands.command((['teleport']), player)
        reading_room_dict = rooms.reading_room.describe()
        eq_(output, reading_room_dict)

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

