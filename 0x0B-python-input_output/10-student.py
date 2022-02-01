#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        s = vars(self)
        if attrs is None:
            return s
        new_s = {}
        for a in s:
            if a in attrs:
                new_s[a] = s[a]
        return new_s
