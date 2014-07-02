import unittest
from nose.tools import eq_

import json

import library_world.library as library
from library_world.game import Game, home, simplify, reconstitute
from library_world.commands import command

game = Game()
player = game.player_state
directory = game.directory
spells = game.spells
npc_list = game.npc_list

class TestCommands(unittest.TestCase):
    def tearDown(self):
        player.update(dict(
            inventory=[],
            location=home,
            level=1,
            shelved_books=[]
            ))
        directory['third_assistant_study'].inventory = ['mouse', 'key',
            'yellow waistcoat', 'dagger']
        directory['reading_room'].inventory = []

    def test_look(self):
        player['location'] = 'binding_room'
        output = command(['look'], game)
        binding_room_dict = {'header': 'Binding Room',
        'text': ['''This is the room where the librarians repair damaged books. There are
books covering every flat surface, and a giant press in the back corner. The
only exit is to the east.'''], 'npc': 'Clippy is here.',
    'inventory': 'There is a wire here.'}
        eq_(output, binding_room_dict)

    def test_talk_normal_NPC(self):
        player['location'] = 'upper_librarian_hallway'
        output = command(['talk', 'imshi'], game)
        self.assertIn(output, npc_list['imshi'].dialogue)

    def test_give_banana(self):
        player['location'] = 'uu_library1'
        player['inventory'] = ['banana', 'chalk']
        output = command(['give', 'banana', 'orangutan'], game)
        eq_(output, 'The orangutan looks at you in disgust.')

    def test_talk_vancelle(self):
        player['location'] = 'chiefs_office'
        output = command(['talk', 'vancelle'], game)
        vancelle_dialogue = {'header': '"You need to shelve these books to get to level 2:"',
            'text': ['french book']}
        eq_(output, vancelle_dialogue)

    def test_vancelle_level_up(self):
        game.take('key')
        player['shelved_books'] = ['french book']
        player['location'] = 'chiefs_office'
        output = command(['talk', 'vancelle'], game)
        vancelle_dialogue = {'header':
            '"Congratulations, you\'ve shelved your first book. Now go do the rest. You need to shelve these books to get to level 3:"',
            'text': npc_list['vancelle'].levels['2'],
            'event': '''Level up! You're now level 2.'''}
        eq_(output, vancelle_dialogue)

    def test_take_all(self):
        player['location'] = 'third_assistant_study'
        output = command(['take', 'all'], game)
        eq_(output, {'text': ['You take the mouse.', 'You take the key.',
            'You take the yellow waistcoat.', 'You take the dagger.']})

    def test_drop_all(self):
        player['inventory'] = ['diary', 'key', 'scissors']
        output = command(['drop', 'all'], game)
        eq_(output, {'text': ['You drop the diary.', 'You drop the key.',
            'You drop the scissors.']})
        eq_(directory['reading_room'].inventory, ['diary', 'key', 'scissors'])
        eq_(directory['upper_librarian_hallway'].inventory, [])

class TestMetaGameFunctions(unittest.TestCase):
    def setUp(self):
        player.update(dict(
            inventory=['diary', 'floral book', 'yellow waistcoat', 'key'],
            location='labyrinth1',
            level=2,
            shelved_books=['french book']
            ))

    def tearDown(self):
        player.update(dict(inventory=[], location='reading_room', level=1,
            shelved_books=[]))

    def testSave(self):
        library.save(game, 'test_save')
        eq_(json.load(open('test_save.txt')), simplify(game))

    def testLoad(self):
        load_output, game = library.load('test_save')
        self.assertEquals(simplify(game), simplify(reconstitute(json.load(open('test_save.txt')))))

    def testRestart(self):
        restart_output, game = library.restart()
        new_game = Game()
        new_game_desc = new_game.directory[game.player_state['location']].describe()
        new_game_desc['event'] = 'Restarting...'
        eq_(simplify(game), simplify(new_game))
        eq_(restart_output, new_game_desc)


class TestEvents(unittest.TestCase):
    def tearDown(self):
        player['location'] = home
        player['inventory'] = []
        directory['hall15'].inventory = []

    def test_uu_down_under(self):
        player['location'] = 'uu_library2'
        output = command(['d'], game)
        uu_dict = directory['uu_library2'].describe()
        uu_dict['event'] = '''You feel a swooping sensation in your tummy, like gravity just shifted and up is down
and down is up. But now it's gone, so you don't trouble yourself over it.'''
        eq_(output, uu_dict)

    def test_banana_peel_true(self):
        directory['hall15'].add_invent('banana')
        player['location'] = 'hall15'
        output = command(['n'], game)
        hall14_dict = directory['hall14'].describe()
        hall14_dict['event'] = '''You hear a massive CRASH from the direction of the Restricted
Section. The next minute, a gurney rushes by you with Madame Pince lying on it,
her arm thrown dramatically over her eyes.'''
        eq_(output, hall14_dict)
        eq_(directory['restricted'].locked, False)
        eq_(directory['hall15'].describe()['text'],
            directory['hall15'].secondary_description)

    def test_banana_peel_false(self):
        player['location'] = 'hall15'
        output = command(['n'], game)
        eq_(output, directory['hall14'].describe())

    def test_break_seal(self):
        player['inventory'] = ['fairy tale book', 'french book', 'diary',
            'yellow waistcoat', 'key', 'scissors', 'translation book']
        player['location'] = 'hall15'
        output = command(['break', 'rope'], game)
        reading_room_dict = directory['reading_room'].describe()
        reading_room_dict['event'] = '''As you poise to cut through the rope, Madam Pince
appears seemingly out of nowhere, screeching at the top of her lungs. "WHAT DO
YOU THINK YOU'RE DOING?! Disrespecting library property! Out out out!" She
promptly confiscates all your books, and to add insult to injury, she escorts
you all the way back to the main reading room.'''
        eq_(output, reading_room_dict)
        eq_(player['inventory'], ['yellow waistcoat', 'key', 'scissors',
            'translation book'])

class TestInitialStates(unittest.TestCase):
    def test_home(self):
        output = command(['teleport'], game)
        eq_(output, directory['reading_room'].describe())

    def test_inventory(self):
        output = command(['i'], game)
        eq_(output, "You're not holding anything!")

    def test_level_shelved_books(self):
        output = command(['level'], game)
        first_level_dict = {'header':
            'You are level 1. You have shelved these books:', 'text': []}
        eq_(output, first_level_dict)

    def test_known_spells(self):
        output = command(['spells'], game)
        eq_(output, "You don't know any spells.")

