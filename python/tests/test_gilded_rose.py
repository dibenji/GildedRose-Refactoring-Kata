import unittest
from src.gilded_rose import GildedRose
from src.item import Item


class TestGildedRose(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_decrease_quality_below_0_not_possible(self):
        item = Item("foo", 0, 0)
        item.quality -= 1
        self.assertGreaterEqual(item.quality, 0)

    def test_increase_quality_over_50_not_possible(self):
        item = Item("foo", 0, 50)
        item.quality += 1
        self.assertLessEqual(item.quality, 50)

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestGildedRose('test_foo'))
        suite.addTest(TestGildedRose('test_decrease_quality_below_0_not_possible'))
        suite.addTest(TestGildedRose('test_increase_quality_over_50_not_possible'))
        return suite

    def __str__(self):
        return f"Gilded Rose Class - {self._testMethodName}"
