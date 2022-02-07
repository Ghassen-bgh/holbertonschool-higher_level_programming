#!/usr/bin/python3
"""
Module for Base class
"""
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ ctor for Base Class """
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
