#!/usr/bin/python3
"""import module JSON"""
import json


def load_from_json_file(filename):
    """Function that creates an Object"""
    with open(filename, 'r', encoding="utf-8") as file:
        """use the json.load() function"""
        return json.load(file)
