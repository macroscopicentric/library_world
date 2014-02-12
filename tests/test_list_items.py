import unittest

from list_items import list_items, article
from nose.tools import eq_

class TestListItems(unittest.TestCase):
    def test_list_one_item(self):
        items = ['flask']
        eq_(list_items(items), '\nThere is a flask here.')

    def test_list_two_items(self):
        items = ['flask', 'bucket']
        eq_(list_items(items), '\nThere are a flask and a bucket here.')

    def test_list_many_items(self):
        items = ['flask'] + (['bee'] * 8) + ['bucket']
        many_bees = 'a bee, ' * 8
        eq_(list_items(items), '\nThere are a flask, ' + many_bees + 'and a bucket here.')

    def test_list_no_items(self):
        eq_(list_items([]), '')

    def test_list_a_vowel_noun(self):
        items = ['apple', 'orange']
        eq_(list_items(items), '\nThere are an apple and an orange here.')


class TestArticle(unittest.TestCase):
    def test_normal_nouns_should_get_an_a(self):
        eq_(article('frog'), 'a frog')

    def test_nouns_that_start_with_vowels_should_get_an_an(self):
        eq_(article('apple'), 'an apple')
