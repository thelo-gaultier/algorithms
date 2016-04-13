import unittest
from algorithms.datastructures import heap

class TestHeap(unittest.TestCase):

   def test_parent(self):
      h = heap.Heap([])
      self.assertEqual(h.parent(3), 1)

   def test_left(self):
      h = heap.Heap([])
      self.assertEqual(h.left(3), 6)
      
   def test_right(self):
      h = heap.Heap([])
      self.assertEqual(h.right(3), 7)

   def test_is_in(self):
      h = heap.Heap([])
      self.assertFalse(h.is_in(1), "1 is not in the empty heap")
      h2 = heap.Heap([4,5,6,7])
      self.assertFalse(h2.is_in(4), "4 is not in the empty heap")
      self.assertTrue(h2.is_in(3), "3 is in the empty heap")
      
   def test_heapify(self):
      h = heap.Heap([16,14,10,8,7,9,3,2,4,1])
      
if __name__ == '__main__':
    unittest.main()