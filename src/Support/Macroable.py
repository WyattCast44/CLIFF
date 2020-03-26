class Macroable(type):

    macros = {}

    def __getattr__(self, name):

        # To do, ensure that errors
        # are still raised for missing key
        # errors. We also need to check
        # and see if the method name is in
        # the registered macros and fail
        # if not there

        def method(*args):

            if len(args) > 0:
                return Macroable.macros[name](*args)
            else:
                return Macroable.macros[name]()

        return method

    def macro(self, name, handler):

        Macroable.macros[name] = handler

        return
