#!/usr/bin/python3
"""
json str parser function
"""

import json


def from_json_string(my_str):
    """returns a parsed JSON string"""
    return json.loads(my_str)
