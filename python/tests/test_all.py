import unittest
from test_item import TestItem
from test_gilded_rose import TestGildedRose


class MainTestSuite(unittest.TestSuite):
    def run(self, result, debug=False):
        super().run(result, debug)


if __name__ == '__main__':
    suite = MainTestSuite()
    suite.addTest(TestItem().suite())
    suite.addTest(TestGildedRose().suite())
    unittest.TextTestRunner(verbosity=2).run(suite)
