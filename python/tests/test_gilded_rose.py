import unittest
from src.gilded_rose import GildedRose
from src.item import Item


def suite():
    gilded_rose_suite = unittest.TestSuite()
    gilded_rose_suite.addTest(TestGildedRose('test_foo'))
    gilded_rose_suite.addTest(TestGildedRose('test_decrease_quality_below_0_not_possible'))
    gilded_rose_suite.addTest(TestGildedRose('test_increase_quality_over_50_not_possible'))
    gilded_rose_suite.addTest(TestGildedRose('test_quality_decreases_twice_as_fast_after_sell_date_passed'))
    return gilded_rose_suite


class TestGildedRose(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_decrease_quality(self):
        item = Item("foo", 0, 25)
        GildedRose.decrease_quality(item)
        GildedRose.decrease_quality(item)
        GildedRose.decrease_quality(item)
        self.assertEqual(item.quality, 22)

    def test_increase_quality(self):
        item = Item("foo", 0, 25)
        GildedRose.increase_quality(item)
        GildedRose.increase_quality(item)
        GildedRose.increase_quality(item)
        self.assertEqual(item.quality, 28)

    def test_decrease_quality_below_0_not_possible(self):
        item = Item("foo", 0, 0)
        GildedRose.decrease_quality(item)
        self.assertGreaterEqual(item.quality, 0)

    def test_increase_quality_over_50_not_possible(self):
        item = Item("foo", 0, 50)
        GildedRose.increase_quality(item)
        self.assertLessEqual(item.quality, 50)

    def test_quality_decreases_twice_as_fast_after_sell_date_passed(self):
        item = Item("foo", -1, 25)
        GildedRose.decrease_quality(item)
        GildedRose.decrease_quality(item)
        GildedRose.decrease_quality(item)
        self.assertEqual(item.quality, 19)

    def __str__(self):
        return f"Gilded Rose Class - {self._testMethodName}"
