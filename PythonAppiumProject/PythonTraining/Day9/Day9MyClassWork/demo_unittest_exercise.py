# Create a methods - findGreater(), findSmaller(). Design unit test around it.

import unittest


class NumberTest(unittest.TestCase):

    def setUp(self):
        print("Starting test ")
        self.a = 0
        self.b = 0
        f_name = self.shortDescription()
        if f_name == "find_greater":
            self.a = 60
            self.b = 40
            print(f_name, self.a, self.b)

        if f_name == "find_smaller":
            self.a = 30
            self.b = 80
            print(f_name, self.a, self.b)

    def tearDown(self):
        print("\n Test complete ", self.shortDescription())

    def testFindGreaterNumber(self):
        """find_greater"""
        self.assertTrue((self.a > self.b))
        print("a is greater than b")

    def testFindSmallerNumber(self):
        """find_smaller"""
        self.assertTrue((self.a < self.b))
        print("b is greater than a")


if __name__ == '__main__':
    unittest.main()
