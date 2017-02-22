import unittest


class Roman:
    roman_numerals = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    def __init__(self, x):
        self.x = x % 10

    def __str__(self):
        return Roman.roman_numerals[self.x-1]


class Polygon:
    def __init__(self, n, x):
        self.num_sides = n
        self.length_sides = x

    def interior_angle(self):
        return 360/self.num_sides

    def perimeter(self):
        return self.num_sides*self.length_sides


class Testaroo(unittest.TestCase):
    def setUp(self):
        global objrom
        global objpol
        test_case = self.shortDescription()
        print("setUp", test_case)
        if test_case == "test Roman":
            objrom = Roman(5)
        elif test_case == "test Polygon":
            objpol = Polygon(5, 7)


    def tearDown(self):
        global objrom
        global objpol
        test_case = self.shortDescription()
        print("tear down", test_case)
        if test_case == "test Roman":
            del objrom
        elif test_case == "test Polygon":
            del objpol

    def testRoman(self):
        global objrom
        """test Roman"""
        print("testing roman")
        self.assertEqual(str(objrom),"V")

    def testPolygon(self):
        global objpol
        """test Polygon"""
        print("testing polygon")
        self.assertEqual(objpol.interior_angle(), 72)

if __name__ == '__main__':
    unittest.main()
