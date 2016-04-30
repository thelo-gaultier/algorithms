'''
Created on Apr 29, 2016

@author: Thelo
'''

import copy
import random
import unittest


class TestSorting(unittest.TestCase):

    def _test_sort_random(self, sort_method):
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
