'''
Created on Apr 12, 2016

@author: Thelo
'''


class Node:

    def __init__(self, key):
        self.key = key
        self.pointers = {}

    def equals(self, another_node):
        return (
            another_node is not None and
            self.key == another_node.key)
