import unittest


def equals(x, y):
    return x == y


class Tester(unittest.TestCase):
    def test(self):
        self.assertFalse(equals(2, 2))
        self.assertTrue(equals(3, 3))
        self.assertGreater(4, 2)


if __name__ == '__main__':
    unittest.main()
