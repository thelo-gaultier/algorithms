'''
Created on Apr 17, 2016

@author: Thelo
'''


class Traversal:

    def __init__(self, params):
        """""Do something."""

    @staticmethod
    def pre_order_recursive(c, fct, params):

        if c is None:
            return

        fct(c, params)
        Traversal.pre_order_recursive(c.pointers['left'], fct, params)
        Traversal.pre_order_recursive(c.pointers['right'], fct, params)

    @staticmethod
    def in_order_recursive(c, fct, params):

        if c is None:
            return

        Traversal.in_order_recursive(c.pointers['left'], fct, params)
        fct(c, params)
        Traversal.in_order_recursive(c.pointers['right'], fct, params)

    @staticmethod
    def post_order_recursive(c, fct, params):

        if c is None:
            return

        Traversal.post_order_recursive(c.pointers['left'], fct, params)
        Traversal.post_order_recursive(c.pointers['right'], fct, params)
        fct(c, params)
