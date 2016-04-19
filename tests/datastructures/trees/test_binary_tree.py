'''
Created on Apr 18, 2016

@author: Thelo
'''
import unittest
from algorithms.datastructures.trees import binary_tree
from algorithms.datastructures import node
from algorithms.datastructures.trees import traversals


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.t = binary_tree.BinaryTree()
        self.values = [15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9]
        for v in self.values:
            self.t.insert(node.Node(v))

    def test_minimum(self):
        # Find the minimun from the root.
        min = self.t.minimum(self.t.root)
        self.assertEquals(min.key, 2)

        # Find the minimum from the minimum.
        min2 = self.t.minimum(min)
        self.assertEquals(min.key, min2.key)

        # Find the minimum on right subtree.
        right_child = self.t.root.pointers['right']
        min = self.t.minimum(right_child)
        self.assertEquals(min.key, 17)

        # Find the minimum on left subtree.
        left_child = self.t.root.pointers['left']
        min = self.t.minimum(left_child)
        self.assertEquals(min.key, 2)

        # Give a None node.
        min = self.t.minimum(None)
        self.assertIsNone(min, "Minimum of empty tree should be None.")

    def test_maximum(self):
        # Find the maximun from the root.
        max = self.t.maximum(self.t.root)
        self.assertEquals(max.key, 20)

        # Find the maximum from the maximum.
        max2 = self.t.maximum(max)
        self.assertEquals(max.key, max2.key)

        # Find the maximum on right subtree.
        right_child = self.t.root.pointers['right']
        max = self.t.maximum(right_child)
        self.assertEquals(max.key, 20)

        # Find the maximum on left subtree.
        left_child = self.t.root.pointers['left']
        max = self.t.maximum(left_child)
        self.assertEquals(max.key, 13)

        # Give a None node.
        max = self.t.maximum(None)
        self.assertIsNone(max, "Maximum of empty tree should be None.")

    def test_successor(self):
        self.values.sort()
        c = self.t.minimum(self.t.root)

        # Make sure than iterating on the successor give all
        # the node ordered by key
        for v in self.values:
            self.assertTrue(v, c.key)
            c = self.t.successor(c)

        # Next successor should be None
        self.assertIsNone(self.t.successor(c))

        # None successor should be None
        self.assertIsNone(self.t.successor(None))

    def test_predecessor(self):
        self.values.sort()
        self.values.reverse()
        c = self.t.maximum(self.t.root)

        # Make sure than iterating on the successor give all
        # the node ordered by key
        for v in self.values:
            self.assertTrue(v, c.key)
            c = self.t.predecessor(c)

        # Next successor should be None
        self.assertIsNone(self.t.predecessor(c))

        # None successor should be None
        self.assertIsNone(self.t.predecessor(None))

    def _add_list(self, n, params):
        params.append(n.key)

    def test_inorder_traversal_recursive(self):
        fct = traversals.Traversal.in_order_recursive
        expected_list = [2, 3, 4, 6, 7, 9, 13, 15, 17, 18, 20]
        self._test_traversal(expected_list, fct)

    def test_preorder_traversal_recursive(self):
        fct = traversals.Traversal.pre_order_recursive
        expected_list = [15, 6, 3, 2, 4, 7, 13, 9, 18, 17, 20]
        self._test_traversal(expected_list, fct)

    def test_postorder_traversal_recursive(self):
        fct = traversals.Traversal.post_order_recursive
        expected_list = [2, 4, 3, 9, 13, 7, 6, 17, 20, 18, 15]
        self._test_traversal(expected_list, fct)

    def _test_traversal(self, expected, fct):
        head = self.t.root
        list_traversal = []
        fct(head, self._add_list, list_traversal)
        self.assertEquals(list_traversal, expected)

    def test_search(self):
        # Make sure each values can be found and is correct
        for v in self.values:
            n = self.t.search(v)
            self.assertEquals(v, n.key)

        # Make sure the search function return None
        # if the value cannot be found
        v = self.t.search(-1)
        self.assertIsNone(v, "Value : %s should not be in the tree" % v)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_insert']
    unittest.main()
