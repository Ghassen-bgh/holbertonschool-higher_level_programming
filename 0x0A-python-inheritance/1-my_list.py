#!/usr/bin/python3
"""
Module representation of a list class
"""


class MyList(list):
    """ My list class """
    def __init__(self):
        """ Init method """
        super().__init__()

    def print_sorted(self):
        """
        prints the list in sorted way, ascending order
        """
        x = self[:]
        x.sort()
        print(x)
