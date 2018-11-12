import unittest

class suiteTest(unittest.TestCase):
  
   def setUp(self):
      self.a = 10
      self.b = 20
      
   def testadd(self):
      """Add"""
      result = self.a+self.b
      self.assertTrue(result == 30)
      
   def testsub(self):
      """sub"""
      result = self.a-self.b
      self.assertTrue(result == 10)
      
def tsuite():
   suite = unittest.TestSuite()
   suite.addTest (suiteTest("testadd"))
   suite.addTest (suiteTest("testsub"))
   return suite
   
if __name__ == '__main__':
   runner = unittest.TextTestRunner() #create a runner object to execute test suite
   test_suite = tsuite()
   runner.run (test_suite)
   