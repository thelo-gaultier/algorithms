'''
Created on Apr 14, 2016

@author: Thelo
'''
import unittest
from algorithms.datastructures.stacks.stack import Stack


class TestStack(unittest.TestCase):


   def test_pop_push(self):
      s = Stack()
      for i in xrange(1,100):
         s.push(i)
         
      for i in reversed(xrange(1,100)):
         item = s.pop()
         self.assertEqual(item, i, "Item %s should be equal to i: %s" % (item, i))
   
   def test_is_empty(self):
      s = Stack()
      self.assertTrue(s.is_empty(), "The stack should be empty.")
      s.push(101)
      self.assertFalse(s.is_empty(), "The stack should not be empty.")

if __name__ == "__main__":
   #import sys;sys.argv = ['', 'Test.testName']
   unittest.main()