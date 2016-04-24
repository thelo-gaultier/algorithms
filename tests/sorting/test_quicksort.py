'''
Created on Apr 23, 2016

@author: Thelo
'''
import copy
import random
import unittest
from algorithms.sorting import sort


class TestQuickSort(unittest.TestCase):

    def test_quicksort_basic(self):
        """Test basic and corner cases."""
        sorter_hoare = sort.Sorter.create("hoare")
        sorter_lomuto = sort.Sorter.create("lomuto")

        self._test_quicksort_basic(sorter_hoare)
        self._test_quicksort_basic(sorter_lomuto)

    def _test_quicksort_basic(self, sort_method):
        empty_array = []
        sort_method.sort(empty_array)
        self.assertEqual(empty_array,
                         [],
                         "Two empty arrays should not differ.")

        sorted_array = [1, 2, 3, 4, 5]
        expected_sorted_array = copy.deepcopy(sorted_array)
        sort_method.sort(sorted_array)
        self.assertEqual(sorted_array,
                         expected_sorted_array,
                         "a sorted array should not change.")

        sorted_array.reverse()
        reverse_sorted_array = copy.deepcopy(sorted_array)
        sort_method.sort(reverse_sorted_array)
        self.assertEqual(reverse_sorted_array,
                         expected_sorted_array,
                         "The array should be sorted.")

        double_pivot = [5, 4, 9, 3, 5]
        expected_double_pivot = copy.deepcopy(double_pivot)
        sort_method.sort(sorted_array)
        self.assertEqual(double_pivot,
                         expected_double_pivot,
                         "A sorted array should be sorted.")

    def test_quicksort_random(self):
        """Generate random arrays, then sort them."""
        sorter_hoare = sort.Sorter.create("hoare")
        sorter_lomuto = sort.Sorter.create("lomuto")

        self._test_quicksort_random(sorter_hoare)
        self._test_quicksort_random(sorter_lomuto)

    def _test_quicksort_random(self, sort_method):
        for i in xrange(1, 50):
            # init an array
            random_array = []
            # generate i random number
            for i in xrange(1, 50):
                r = random.randint(1, 1000)
                random_array.append(r)

            random_array_copy = copy.deepcopy(random_array)
            random_array_copy.sort()
            sort_method.sort(random_array)
            msg = ("%s and %s should be equal"
                   % (random_array, random_array_copy))
            self.assertEquals(random_array,
                              random_array_copy,
                              msg)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
