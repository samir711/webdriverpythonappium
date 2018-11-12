import unittest

class simpleTest2(unittest.TestCase):
  
   def setUp(self):
      self.a = 0
      self.b = 0
      name = self.shortDescription()
      
      if name == "add":
         self.a = 10
         self.b = 20
         print(name, self.a, self.b)
      if name == "sub":
         self.a = 50
         self.b = 60
         print(name, self.a, self.b)
         
   def tearDown(self):
      print('\nend of test',self.shortDescription())

   def testadd(self):
      """add"""  #docstring, will be used as short description
      result = self.a+self.b
      self.assertTrue(result == 30)
   
   def testsub(self):
      """sub"""  #docstring, will be used as short description
      result = self.a-self.b
      self.assertTrue(result == -10)
      
if __name__ == '__main__':
   unittest.main()