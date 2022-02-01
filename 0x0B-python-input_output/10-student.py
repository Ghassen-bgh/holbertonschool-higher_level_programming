#!/usr/bin/python3
""" Student Class """


class Student:
    """ A Student Class """

    def __init__(self, first_name, last_name, age):
        """ Initialize the Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean) for JSON
        """
        s = vars(self)
        if attrs is None:
            return s
        new_s = {}
        for a in s:
            if a in attrs:
                new_s[a] = s[a]
        return new_s
