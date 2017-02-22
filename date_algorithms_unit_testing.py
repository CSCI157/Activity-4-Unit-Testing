import unittest
from date_algorithms import *


class TestDates(unittest.TestCase):
    """
    3,3,2017 = 2457816
    """
    def test_date(self):
        print("test_date")
        self.assertEqual((date(2457817)), (4,3,2017))
        self.assertEqual((date(2457817+365)), (4,3,2018))
        self.assertEqual((date(2457817 + 2*365)), (4, 3, 2019))
        self.assertEqual((date(2457817 + 3*365)), (3, 3, 2020))
        self.assertEqual((date(2457817 - 101*365 - 25)), (4, 3, 1916))
        self.assertEqual((date(2457817 - 101*365 - 25 + 35)), (8, 4, 1916))

    def test_days(self):
        print("test_days")
        self.assertEqual(num_days(4,3,2017), num_days(3,3,2017)+1)

if __name__ == '__main__':
    unittest.main()
