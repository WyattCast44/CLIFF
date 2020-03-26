def tap(value, callback):
    """The tap function accepts two arguments: an arbitrary value and a callback. The value will be passed to the callback and then be returned by the tap function. The return value of the callback is irrelevant"""

    callback(value)

    return value
