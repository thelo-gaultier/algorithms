'''
Created on Apr 17, 2016

@author: Thelo
'''


class BinaryTree:
    '''
    classdocs
    '''

    def __init__(self):
        self.root = None

    def insert(self, n):
        self._init_node(n)
        p = None
        c = self.root

        while c is not None:
            p = c
            if n.key <= c.key:
                c = c.pointers['left']
            else:
                c = c.pointers['right']

        if p is None:
            self.root = n
            return

        if n.key <= p.key:
            p.pointers['left'] = n
        else:
            p.pointers['right'] = n
        n.pointers['parent'] = p

    def search(self, key):
        c = self.root
        while c is not None and c.key != key:
            if key <= c.key:
                c = c.pointers['left']
            else:
                c = c.pointers['right']
        return c

    def _init_node(self, n):
        n.pointers['parent'] = None
        n.pointers['left'] = None
        n.pointers['right'] = None

    def with_root(self):
        return self.root

    def minimum(self, n):

        if n is None:
            return None

        while n.pointers['left'] is not None:
            n = n.pointers['left']
        return n

    def maximum(self, n):

        if n is None:
            return None

        while n.pointers['right'] is not None:
            n = n.pointers['right']
        return n

    def successor(self, n):

        if n is None:
            return None

        right = n.pointers['right']
        if right is not None:
            return self.minimum(right)

        z = n
        p = n.pointers['parent']
        while p is not None and p.pointers['right'] is z:
            z = p
            p = p.pointers['parent']
        return p

    def predecessor(self, n):

        if n is None:
            return None

        left = n.pointers['left']
        if left is not None:
            return self.maximum(left)

        z = n
        p = n.pointers['parent']
        while p is not None and p.pointers['left'] is z:
            z = p
            p = p.pointers['parent']
        return p
