#!/usr/bin/python3
"""This module defines an object from a JSON file"""
import json


def load_from_json_file(filename):
    """This function that creates an Object from a “JSON file"""
    with open(filename, 'r') as file:
        data = file.read()
        dict_data = json.loads(data)
    return dict_data
