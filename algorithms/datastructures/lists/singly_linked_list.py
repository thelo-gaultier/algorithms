'''
Created on Apr 12, 2016

@author: Thelo
'''
from algorithms.datastructures import node


class SinglyLinkedList:
    '''
    Class representing a singly linked list
    '''

    def __init__(self):
        self.head = None

    def add(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.pointers['next'] = None
            return

        tmp = self.head
        self.head = new_node
        new_node.pointers['next'] = tmp

    def search(self, key):
        c = self.head
        while (c is not None and c.key != key):
            c = c.pointers['next']
        return c

    def delete(self, elt):
        p = None
        c = self.head
        while (c is not None and elt != c):
            p = c
            c = c.pointers['next']

        """If we could not find it"""
        if c is None:
            return False

        """If its the head"""
        if p is None:
            self.head = c.pointers['next']
        else:
            p.pointers['next'] = c.pointers['next']
        return True

    def reverse_non_recursive(self):
        """Reverse a list using a non recursive method.
           Besides the method takes no extra memory
        """
        l = SinglyLinkedList()
        while self.head is not None:
            first = self.head
            l.add(node.Node(first.key))
            self.delete(first)
        self.head = l.head

    def reverse_recursive(self):
        """Reverse a list using a non recursive method.
           Besides the method takes no extra memory
        """
        new_head = self._reverse_recursive(None, self.head)
        self.head = new_head

    def _reverse_recursive(self, p, c):

        if (c.pointers['next'] is None):
            c.pointers['next'] = p
            return c
        else:
            tail = self._reverse_recursive(c, c.pointers['next'])
            c.pointers['next'] = p
            return tail

    """
    def display(self):
        tmp = self.head
        list_str = []
        while tmp is not None:
            list_str.append(str(tmp.key))
            tmp = tmp.pointers['next']
        list_str.append("None")
        s = ' -> '.join(list_str)
        print s
    """
