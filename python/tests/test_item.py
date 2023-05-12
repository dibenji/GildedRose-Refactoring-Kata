import unittest
from src.item import Item
from src.gilded_rose import GildedRose


def suite():
    item_suite = unittest.TestSuite()
    item_suite.addTest(TestItem('test_name'))
    item_suite.addTest(TestItem('test_sell_within_days'))
    item_suite.addTest(TestItem('test_quality_value'))
    item_suite.addTest(TestItem('test_update_quality_aged_brie'))
    item_suite.addTest(TestItem('test_update_sell_in_aged_brie'))
    item_suite.addTest(TestItem('test_update_quality_twice_if_sell_in_10_days_or_less'))
    item_suite.addTest(TestItem('test_update_quality_three_times_if_sell_in_5_days_or_less'))
    return item_suite


class TestItem(unittest.TestCase):
    def test_name(self):
        item = Item("foo", 0, 0)
        self.assertEqual(item.name, "foo")

    def test_sell_within_days(self):
        item = Item("foo", 0, 0)
        self.assertEqual(item.sell_in, 0)

    def test_quality_value(self):
        item = Item("foo", 0, 0)
        self.assertEqual(item.quality, 0)

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

    def __str__(self):
        return f"Item Class - {self._testMethodName}"
