class OptionFinder:

    def __init__(self, application):

        self.app = application

        self.registeredOptions = self.app.options

        self.processRegisteredOptions()

        return

    def processRegisteredOptions(self):

        processedOptions = {}

        # We need to process the registered option signatures and
        # split them if they have a "|"" in them
        for signature, handler in self.registeredOptions.items():

            if "|" in signature:

                parts = signature.split("|")

                for part in parts:

                    processedOptions[part] = handler

            else:

                processedOptions[signature] = handler

        self.processedOptions = processedOptions

        return self

    def search(self, signature=None):

        # If a signature is not passed in, lets take the
        # first argument passed to the script as a potential
        # options

        if signature == None:

            signature = self.app.args[0]

        # First we will check in the registered options
        # and see if we can find it
        if signature in self.processedOptions:

            # The signature matches a register option
            # we will return the handler for the signature
            return self.processedOptions[signature]

        else:

            return None
