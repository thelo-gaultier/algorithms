'''
Created on Apr 24, 2016

@author: Thelo
'''

from algorithms.sorting import quicksort


class Sorter(object):
    """"Super class for the sorting algorithms."""

    def __init__(self, params):
        """"No global initialisation needed."""

    def sort(self, array_to_sort):
        """Sort an array given in parameter."""

    @staticmethod
    def create(method):
        if "quicksort_hoare":
            return quicksort.QuickSort("hoare")
        elif "quicksort_lomuto":
            return quicksort.QuickSort("lomuto")
        else:
            return None
