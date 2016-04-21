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

    def delete(self, n):
        if n is None:
            return None
        y = None
        if (n.pointers['left'] is None or n.pointers['right'] is None):
            y = n
        else:
            y = self.successor(n)

        x = None
        if y.pointers['left'] is not None:
            x = y.pointers['left']
        else:
            x = y.pointers['right']

        p = None
        if y is not None:
            p = y.pointers['parent']

        if p is None:
            self.root = x
            x.pointers['parent'] = None
        else:
            if p.pointers['left'] is y:
                p.pointers['left'] = x
            else:
                p.pointers['right'] = x

        if (n.pointers['left'] is not None and
           n.pointers['right'] is not None):
            # We should exchange y and n,
            # We could simply exchange values
            # but if someone maintains a reference to the successor
            # we will corrupt it
            print "Replace %s , %s" % (y.key, n.key)
            y = self._replace(y, n)

        return y

    def _replace(self, src, dst):
        src_pointers = src.pointers
        src.pointers = dst.pointers
        dst.pointers = src_pointers

        # Replace references in other nodes
        left = src.pointers['left']
        if left is not None:
            left.pointers['parent'] = src

        right = src.pointers['right']
        if right is not None:
            right.pointers['parent'] = src

        parent = src.pointers['parent']
        if parent is not None:
            if parent.pointers['left'] is dst:
                parent.pointers['left'] = src
            else:
                parent.pointers['right'] = src

        # Special case for the root
        if self.root is dst:
            self.root = src
        return dst
