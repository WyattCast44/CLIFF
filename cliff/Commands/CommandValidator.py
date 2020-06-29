import string
from cliff import Application


class CommandValidator:

    validSignatureCharacters = string.ascii_lowercase + ":"

    def __init__(self, application: Application):

        self.application = application

    def validate(self, command, signature=None) -> dict:

        self.signature = signature

        self.command = command

        self._determineSignature()

        self._validateSignature()

        return (self.signature, self.command)

    def _determineSignature(self):

        if not self.signature == None:

            return self

        if hasattr(self.command, "signature"):

            self.signature = self.command.signature

            return self

        elif hasattr(self.command, "getSignature"):

            self.signature = self.command.getSignature()

            return self

        elif hasattr(self.command, "get_signature"):

            self.signature = self.command.get_signature()

            return self

        else:

            raise Exception(
                "The given command does not have a recognizable signature", "Command:", self.command)

    def _validateSignature(self):

        for letter in self.signature:

            if not letter in self.validSignatureCharacters:

                raise Exception("The commands signature is not a valid format",
                                "Command: ", self.command, "Signature: ", self.signature, "Details: https://google.com")

        return self
