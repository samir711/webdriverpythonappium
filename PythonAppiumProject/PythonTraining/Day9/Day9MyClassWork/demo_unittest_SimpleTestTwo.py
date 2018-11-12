import unittest


class SimpleTest2(unittest.TestCase):

    def setUp(self):
        # self.a = 10
        # self.b = 20
        name = self.shortDescription()

        if name == "add":
            self.a = 10
            self.b = 20
            print(name,  self.a, self.b)
        if name == "sub":
            self.a = 50
            self.b = 60
            print(name, self.a, self.b)

    def tearDown(self):
        print('end of test', self.shortDescription())
        print('\n')

    def testAdd(self):
        """add"""
        result = self.a + self.b
        self.assertEqual(result, 30)

    def testSub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)


if __name__ == '__main__':
    unittest.main()


