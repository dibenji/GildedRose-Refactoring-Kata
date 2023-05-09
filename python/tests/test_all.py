import unittest
from test_item import suite as item_suite
from test_gilded_rose import suite as gilded_rose_suite


class MainTestSuite(unittest.TestSuite):
    def run(self, result, debug=False):
        super().run(result, debug)


if __name__ == '__main__':
    suite = MainTestSuite()
    suite.addTest(item_suite())
    suite.addTest(gilded_rose_suite())
    unittest.TextTestRunner(verbosity=2).run(suite)
