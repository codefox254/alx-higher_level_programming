#!/usr/bin/python3
"""Define a locked class."""

class LockedClass:
    """
    We need to prevent the user from instatiating new LockedClass att for
    anything except att called 'first_name'.
    """

    __slots__ = ["first_name"]
