import unittest
from src.gilded_rose import GildedRose
from src.item import Item


def suite():
    gilded_rose_suite = unittest.TestSuite()
    gilded_rose_suite.addTest(TestGildedRose('test_foo'))
    gilded_rose_suite.addTest(TestGildedRose('test_decrease_quality_below_0_not_possible'))
    gilded_rose_suite.addTest(TestGildedRose('test_increase_quality_over_50_not_possible'))
    gilded_rose_suite.addTest(TestGildedRose('test_quality_decreases_twice_as_fast_after_sell_date_passed'))
    gilded_rose_suite.addTest(TestGildedRose('test_update_quality_aged_brie'))
    gilded_rose_suite.addTest(TestGildedRose('test_update_sell_in_aged_brie'))
    gilded_rose_suite.addTest(TestGildedRose('test_update_quality_twice_if_sell_in_10_days_or_less'))
    gilded_rose_suite.addTest(TestGildedRose('test_update_quality_three_times_if_sell_in_5_days_or_less'))
    gilded_rose_suite.addTest(TestGildedRose('test_quality_drops_to_zero_after_concert'))
    gilded_rose_suite.addTest(TestGildedRose('test_update_conjured_item_twice_as_fast'))
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

    def test_update_quality_aged_brie(self):
        item = Item("Aged Brie", 0, 0)
        GildedRose.update_item(item)
        GildedRose.update_item(item)
        GildedRose.update_item(item)
        self.assertEqual(item.quality, 3)

    def test_update_sell_in_aged_brie(self):
        item = Item("Aged Brie", 0, 0)
        GildedRose.update_item(item)
        GildedRose.update_item(item)
        GildedRose.update_item(item)
        self.assertEqual(item.sell_in, -3)

    def test_update_quality_twice_if_sell_in_10_days_or_less(self):
        item = Item("backstage pass test", 10, 0)
        GildedRose.update_item(item)
        self.assertEqual(item.quality, 2)

    def test_update_quality_three_times_if_sell_in_5_days_or_less(self):
        item = Item("backstage pass test", 5, 0)
        GildedRose.update_item(item)
        self.assertEqual(item.quality, 3)

    def test_quality_drops_to_zero_after_concert(self):
        item = Item("backstage pass test", -1, 5)
        GildedRose.update_item(item)
        self.assertEqual(item.quality, 0)

    def test_update_conjured_item_twice_as_fast(self):
        item = Item("Conjured test", 5, 6)
        GildedRose.update_conjured_item(item)
        GildedRose.update_conjured_item(item)
        GildedRose.update_conjured_item(item)
        self.assertEqual(item.quality, 0)

    def __str__(self):
        return f"Gilded Rose Class - {self._testMethodName}"
