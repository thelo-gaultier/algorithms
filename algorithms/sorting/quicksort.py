'''
Created on Apr 23, 2016

@author: Thelo
'''


class QuickSort:

    def __init__(self, partition):
        """Empty doc string."""
        if partition == "hoare":
            self.partition = self._hoare_partition
        elif partition == "lomuto":
            self.partition = self._lomuto_partition
        else:
            # Default partition is the original one
            self.partition = self._hoare_partition

    def sort(self, array_to_sort):
        self._quicksort(array_to_sort,
                        0,
                        len(array_to_sort)-1)

    def _quicksort(self, array_to_sort, p, q):
        if p < q:
            i = self.partition(array_to_sort, p, q)
            self._quicksort(array_to_sort, p, i)
            self._quicksort(array_to_sort, i+1, q)

    def _lomuto_partition(self, array_to_sort, p, q):
        """Use the Lomuto partition."""
        pivot = array_to_sort[q]
        i = p-1
        for j in xrange(p, q):
            if array_to_sort[j] <= pivot:
                i += 1
                self._exchange(array_to_sort, j, i)

        # Avoid infinite loop if the pivot is the minimum
        self._exchange(array_to_sort, q, i+1)
        return i

    def _hoare_partition(self, array_to_sort, p, q):
        """Do something nice."""
        pivot = array_to_sort[p]
        i = p-1
        j = q+1

        while True:
            j -= 1
            while array_to_sort[j] > pivot and j >= i:
                j -= 1

            i += 1
            while array_to_sort[i] < pivot and j >= i:
                i += 1

            if i < j:
                self._exchange(array_to_sort, i, j)
            else:
                return j

    def _exchange(self, array, a, b):
        tmp = array[a]
        array[a] = array[b]
        array[b] = tmp
