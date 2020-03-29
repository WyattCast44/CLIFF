class CommandFinder:

    def __init__(self, application):

        self.app = application

        self.registeredCommands = self.app.commands

        self.processRegisteredCommands()

        return

    def processRegisteredCommands(self):

        processedCommands = {}

        # We need to process the registered command signatures and
        # split them if they have a "|"" in them
        for signature, handler in self.registeredCommands.items():

            if "|" in signature:

                parts = signature.split("|")

                for part in parts:

                    processedCommands[part] = handler

            else:

                processedCommands[signature] = handler

        self.processedCommands = processedCommands

        return self

    def search(self, signature=None):

        # If a signature is not passed in, lets take the
        # first argument passed to the script as a potential
        # commands

        if signature == None:

            signature = self.app.args[0]

        # First we will check in the registered commands
        # and see if we can find it
        if signature in self.processedCommands:

            # The signature matches a register command
            # we will return the handler for the signature
            return self.processedCommands[signature]

        else:

            return None
