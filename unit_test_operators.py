import unittest


class MyClass:

    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __eq__(self, other):
        print("equals")
        if isinstance(other, MyClass):
            return self.x == other.x
        elif isinstance(other, (int, float, complex)):
            return self.x == other
        return NotImplemented


class FixturesTest(unittest.TestCase):

    def setUp(self):
        print('In setUp()')
        self.obj1 = MyClass(5)
        self.obj2 = MyClass(5)
        self.obj3 = MyClass(6)

    def tearDown(self):
        print('In tearDown()')
        del self.obj1
        del self.obj2
        del self.obj3

    def test(self):
        print('in test()')
        self.assertEqual(self.obj1, self.obj2)
        self.assertNotEqual(self.obj1, self.obj3)
        self.assertEqual(self.obj1, 5)

if __name__ == '__main__':
    unittest.main()
