#!/usr/bin/python3
""" Load from JSON file """

import json


def load_from_json_file(filename):
    """ Load from JSON file """

    with open(filename, "r", encoding="utf-8") as f:
        json_obj = f.read()
        if not len(json_obj):
            return None
        return json.loads(json_obj)
