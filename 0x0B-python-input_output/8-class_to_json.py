#!/usr/bin/python3
"""This will define a python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary represntation of a simple data structure."""
    return obj.__dict__