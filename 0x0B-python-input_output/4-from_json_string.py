#!/usr/bin/python3
"""This module defines the JSON representation of an object"""
import json


def from_json_string(my_str):
    """Returns the python object representation of a JSON string"""
    return json.loads(my_str)
