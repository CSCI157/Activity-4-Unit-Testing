import unittest


class MyClass:

    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def plus_two(self):
        return self.x+2


class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.fixture = MyClass(5)

    def tearDown(self):
        print('In tearDown()')
        del self.fixture

    def test(self):
        print('in test()')
        self.assertEqual(self.fixture.plus_two(), 7)
        self.assertEqual(str(self.fixture), str(5))

if __name__ == '__main__':
    unittest.main()
