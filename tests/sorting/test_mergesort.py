'''
Created on Apr 29, 2016

@author: Thelo
'''

import copy
import unittest

from algorithms.sorting import sort
from tests.sorting import test_sort
from algorithms.sorting import mergesort


class TestMergeSort(test_sort.TestSorting):

    def test_merge(self):
        sorter = mergesort.MergeSort()
        array_a = [1, 3, 5]
        array_b = [2, 4, 6, 7]
        array_returned = sorter.merge(array_a, array_b)

        for elt in array_b:
            array_a.append(elt)
        array_a.sort()

        self.assertEquals(array_returned, array_a)

    def test_reversed_sorted(self):
        array_to_sort = [5, 4, 3, 2, 1]
        expected_array = copy.deepcopy(array_to_sort)
        expected_array.sort()

        sorter = sort.Sorter.create('mergesort')
        sorter.sort(array_to_sort)
        self.assertEquals(expected_array, array_to_sort)

    def test_mergesort_random(self):
        """Generate random arrays, then sort them."""
        sorter = sort.Sorter.create("mergesort")
        self._test_sort_random(sorter)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
