import unittest
from src.gilded_rose import GildedRose
from src.item import Item


class TestGildedRose(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestGildedRose('test_foo'))
        return suite

    def __str__(self):
        return f"Gilded Rose Class - {self._testMethodName}"