'''
Created on Apr 13, 2016

@author: Thelo
'''
import unittest
from algorithms.datastructures.lists.singly_linked_list import SinglyLinkedList
from algorithms.datastructures.node import Node


class TestSinglyLinkedList(unittest.TestCase):

    def test_add_delete_element(self):
        l = SinglyLinkedList()
        for i in xrange(1, 100):
            l.add(Node(i))

        for i in xrange(1, 100):
            n = l.search(i)
            self.assertIsNotNone(n, "Node should not be None.")

        for i in xrange(1, 100):
            n = l.search(i)
            self.assertTrue(l.delete(n), "Could not delete an existing node.")

        """Delete a deleted node."""
        n = Node(101)
        l.add(n)
        self.assertTrue(l.delete(n), "Could not delete an existing node.")
        self.assertFalse(l.delete(n), "Could delete a deleted node.")

    def test_search_element(self):
        l = SinglyLinkedList()

        """Add and search a node."""
        n1 = Node(5)
        l.add(n1)
        n1s = l.search(5)
        self.assertTrue(n1 is n1s, "Node added and node searched differ.")

        """Search an non-existing node."""
        n2s = l.search(2)  
        self.assertIsNone(n2s, "Node found while it should not be found.")

        """Search a deleted node."""
        l.delete(n1)
        n1s = l.search(5)
        self.assertIsNone(n1s, "Node found while it should not be found.")

    def test_reverse_recursive(self):
        l = SinglyLinkedList()
        self._generic_test_reverse_list(l, l.reverse_recursive)

    def test_reverse_non_recursive(self):
        l = SinglyLinkedList()
        self._generic_test_reverse_list(l, l.reverse_non_recursive)

    def _generic_test_reverse_list(self, l, reverse_function):
        msg_empty_list = "Node should be None since we have reached the end of the list."
        for i in reversed(xrange(1, 100)):
            l.add(Node(i))
  
        c = l.head
        for i in xrange(1, 100):
            self.assertEquals(c.key, i, "Keys are not in order.")
            c = c.pointers['next']
        self.assertIsNone(c, msg_empty_list)

        reverse_function()

        c = l.head
        for i in reversed(xrange(1, 100)):
            self.assertEquals(c.key, i, "Keys are not in order %i." % i)
            c = c.pointers['next']
        self.assertIsNone(c, msg_empty_list)

        reverse_function()

        c = l.head
        for i in xrange(1, 100):
            self.assertEquals(c.key, i, "Keys are not in order.")
            c = c.pointers['next']
        self.assertIsNone(c, msg_empty_list)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testAddElement']
    unittest.main()
