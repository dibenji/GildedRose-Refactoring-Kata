import unittest
from src.item import Item


def suite():
    item_suite = unittest.TestSuite()
    item_suite.addTest(TestItem('test_name'))
    item_suite.addTest(TestItem('test_sell_within_days'))
    item_suite.addTest(TestItem('test_quality_value'))
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
        ite,

    def __str__(self):
        return f"Item Class - {self._testMethodName}"
