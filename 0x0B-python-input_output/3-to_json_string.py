#!/usr/bin/python3
"""
contain the JSON string
"""

import json


def to_json_string(my_obj):
    """returns an object parsed to JSON"""
    return json.dumps(my_obj)
