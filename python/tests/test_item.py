import unittest
from src.item import Item


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

    def test_creation_not_possible_with_negative_quality(self):
        item = Item("foo", 0, -1)
        self.assertGreaterEqual(item.quality, 0)

    def test_creation_not_possible_with_quality_greater_50(self):
        item = Item("foo", 0, 51)
        self.assertLessEqual(item.quality, 50)

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestItem('test_name'))
        suite.addTest(TestItem('test_sell_within_days'))
        suite.addTest(TestItem('test_quality_value'))
        suite.addTest(TestItem('test_creation_not_possible_with_negative_quality'))
        suite.addTest(TestItem('test_creation_not_possible_with_quality_greater_50'))
        return suite

    def __str__(self):
        return f"Item Class - {self._testMethodName}"
