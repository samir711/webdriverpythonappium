import unittest


class MySuiteTest(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 20

    def testAdd(self):
        """Add"""
        result = self.a + self.b
        self.assertTrue(result == 30)

    def testSub(self):
        """Sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)


def test_suite():
        suite = unittest.TestSuite()
        suite.addTest(MySuiteTest("testAdd"))
        suite.addTest(MySuiteTest("testSub"))
        return suite


if __name__ == '__main__':
    my_test_suite = test_suite()
    runner = unittest.TextTestRunner()
    runner.run(my_test_suite)

