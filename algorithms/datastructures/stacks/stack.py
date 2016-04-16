'''
Created on Apr 14, 2016
Implementation of a Stack with an array/list
book: Introduction to algorithm - 10.1 Stacks and queues
@author: Thelo
'''


class Stack:
   
    def __init__(self):
        self.stack = []
        self.size = 0

    """Probably not the best language to practice Stack."""
    def push(self, item):
        self.stack.append(item)

    def pop(self):     
        size = len(self.stack)
        return self.stack.pop(size-1)

    def is_empty(self):
        return len(self.stack) == 0
