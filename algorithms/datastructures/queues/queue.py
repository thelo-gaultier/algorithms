'''
Created on Apr 14, 2016
@author: Thelo
'''


class Queue(object):

    def __init__(self, size):
        self.queue = []
        self.size = size
        """Init with useless values."""
        for i in xrange(1, size+1):
            self.queue.append(i)
        self.head = 0
        self.tail = 0
        self.current_size = 0

    def _next(self, index):
        return (index + 1) % self.size

    def is_full(self):
        return self.current_size == self.size

    def is_empty(self):
        return self.current_size == 0

    def enqueue(self, item):
        if self.is_full():
            return False

        self.queue[self.head] = item
        self.head = self._next(self.head)
        self.current_size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.queue[self.tail]
        self.tail = self._next(self.tail)
        self.current_size -= 1
        return item
