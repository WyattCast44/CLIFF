def tap(value, callback):
    """The tap function accepts two arguments: an arbitrary value and a callback. The value will be passed to the callback and then be returned by the tap function. The return value of the callback is irrelevant"""

    callback(value)

    return value


def dd(*values):

    import sys
    import pprint

    for value in values:

        pprint.pprint(value)

    sys.exit()


def now():
    """Return the current time in seconds since the Epoch. Fractions of a second may be present if the system clock provides them."""

    import time

    return time.time()


def s(str: str):
    """Return an extended string class with additional convience methods"""

    from src.Support import StrExtended

    return StrExtended(str)
