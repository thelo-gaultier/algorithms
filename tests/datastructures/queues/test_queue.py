'''
Created on Apr 16, 2016

@author: Thelo
'''
import unittest
from algorithms.datastructures.queues.queue import Queue


class TestQueue(unittest.TestCase):

    def test_is_empty(self):
        q = Queue(3)
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_is_full(self):
        q = Queue(2)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue(1)
        self.assertFalse(q.is_full())
        q.enqueue(2)
        self.assertTrue(q.is_full())
        q.dequeue()
        self.assertFalse(q.is_full())

    def test_enqueue_dequeue(self):
        q = Queue(5)
        self.assertTrue(q.is_empty())

        for i in xrange(1, 6):
            self.assertTrue(q.enqueue(i), "We should be able to enqueue.")
        print q.current_size
        self.assertFalse(q.enqueue(6), "We should not be able to enqueue.")
        self.assertTrue(q.is_full(), "Queue should be full.")
        item = q.dequeue()
        self.assertEquals(item, 1, "Dequeued element is not the first in.")
        self.assertTrue(q.enqueue(6), "We should be able to enqueue.")

        for i in xrange(2, 7):
            self.assertEquals(i, q.dequeue(), "Does not verify FIFO order.")
        self.assertIsNone(q.dequeue(), "Empty queue should return None.")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
