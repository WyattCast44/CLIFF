class CommandNotRegistered(Exception):
    """The requested command was found but is not registered. Please register the command
    or run via the `_runUnregisteredCommand` method.
    """
    pass
