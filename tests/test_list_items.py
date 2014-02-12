import unittest

from list_items import list_items
from nose.tools import eq_

class TestListItems(unittest.TestCase):
    def test_list_one_item(self):
        items = ['flask']
        eq_(list_items(items), 'a flask')

    def test_list_two_items(self):
        items = ['flask', 'bucket']
        eq_(list_items(items), 'a flask and a bucket')

    def test_list_many_items(self):
        items = ['flask'] + (['bee'] * 8) + ['bucket']
        many_bees = 'a bee, ' * 8
        eq_(list_items(items), 'a flask, ' + many_bees + 'and a bucket')

    def test_list_no_items(self):
        eq_(list_items([]), '')
