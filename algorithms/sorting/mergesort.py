'''
Created on Apr 28, 2016

@author: Thelo
'''


class MergeSort(object):
    '''
    classdocs
    '''
   
    def __init__(self):
        """Not much to init here."""

    def sort(self, array_to_sort):
        self.sort(array_to_sort, 0, len(array_to_sort-1))
    
    def _sort(self, array_to_sort, start, end):
        
        size = end - start
        if size <= 2:
            self._sort_small_array(array_to_sort, start, size)
            return self._extract_sub_array(array_to_sort, start, size)
         
        middle_point = size / 2
        left_part = self._sort(start, middle_point)
        right_part = self._sort(middle_point + 1, end)
        return self._merge(left_part, right_part)
        
    def merge(self, array_a, array_b):
        merged_array = []
        size_a = len(array_a) 
        size_b = len(array_b) 
        index_a = 0
        index_b = 0
        merged_index = 0
        
        while index_a < size_a and index_b < size_b:
           
            if array_a[index_a] > array_b[index_b]:
                merged_array.append(array_b[index_b]) 
                index_b += 1
            else:
                merged_array.append(array_a[index_a])
                index_a += 1

        for missing_index in xrange(index_a, size_a):
             merged_array.append(array_a[missing_index])
             merged_index += 1

        for missing_index in xrange(index_b, size_b):
             merged_array.append(array_b[missing_index])

        return merged_array       

    def _sort_small_array(self, array_to_sort, start, size):
        if size == 2:
           if array_to_sort[start] > array_to_sort[start + 1]:
              tmp = array_to_sort[start]
              array_to_sort[start] = array_to_sort[start + 1]
              array_to_sort[start + 1] = tmp
    
    def _extract_sub_array(self, array_to_sort, start, size):
        sub_array = []
        for i in xrange(start, start + size + 1):
            sub_array.append(array_to_sort[i])
        return sub_array