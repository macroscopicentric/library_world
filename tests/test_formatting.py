import unittest

from library_world.formatting import list_items, article, print_npc
from nose.tools import eq_

class TestListItems(unittest.TestCase):
    def test_list_one_item(self):
        items = ['flask']
        eq_(list_items(items), 'There is a flask here.')

    def test_list_two_items(self):
        items = ['flask', 'bucket']
        eq_(list_items(items), 'There are a flask and a bucket here.')

    def test_list_many_items(self):
        items = ['flask'] + (['bee'] * 8) + ['bucket']
        many_bees = 'a bee, ' * 8
        eq_(list_items(items), 'There are a flask, ' + many_bees + 'and a bucket here.')

    def test_list_a_vowel_noun(self):
        items = ['apple', 'orange']
        eq_(list_items(items), 'There are an apple and an orange here.')


class TestArticle(unittest.TestCase):
    def test_normal_nouns_should_get_an_a(self):
        eq_(article('frog'), 'a frog')

    def test_nouns_that_start_with_vowels_should_get_an_an(self):
        eq_(article('apple'), 'an apple')

class TestNPCs(unittest.TestCase):
    def test_normal_npc(self):
        function = 'room'
        npc = 'vancelle'
        eq_(print_npc(npc, function), 'Vancelle')

    def test_orangutan_room(self):
        function = 'room'
        npc = 'orangutan'
        eq_(print_npc(npc, function), 'An orangutan')

    def test_orangutan_give(self):
        function = 'give'
        npc = 'orangutan'
        eq_(print_npc(npc, function), 'The orangutan')
