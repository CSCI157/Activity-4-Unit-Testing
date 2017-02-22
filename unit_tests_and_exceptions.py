import unittest


def divides(x, y):
    print(x, y)
    return x/y


class Divides(unittest.TestCase):
    def test(self):
        self.assertEqual(divides(4, 2), 2)
        self.assertRaises(ZeroDivisionError, divides, 2, 0)
        self.assertEqual(divides(100, 3), 100/3)

if __name__ == '__main__':
    unittest.main()
