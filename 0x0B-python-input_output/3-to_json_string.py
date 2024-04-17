#!/usr/bin/python3
"""This module defines the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object"""
    data = json.dumps(my_obj)
    return data
