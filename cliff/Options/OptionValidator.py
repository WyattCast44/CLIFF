import string
from cliff import Application


class OptionValidator:

    validSignatureCharacters = string.ascii_lowercase + "-"

    def __init__(self, application: Application):

        self.application = application

    def validate(self, option, signature=None):

        self.signature = signature

        self.option = option

        self._determineSignature()

        self._validateSignature()

        return (self.signature, self.option)

    def _determineSignature(self):

        if not self.signature == None:

            return self

        if hasattr(self.option, "signature"):

            self.signature = self.option.signature

            return self

        elif hasattr(self.option, "getSignature"):

            self.signature = self.option.getSignature()

            return self

        elif hasattr(self.option, "get_signature"):

            self.signature = self.option.get_signature()

            return self

        else:

            self._raiseException(
                "The given option does not have a recognizable signature", "https://google.com")

    def _validateSignature(self):

        if not "-" in self.signature[0]:

            self._raiseException(
                "The options signature is not a valid format", "https://google.com")

        for letter in self.signature:

            if not letter in self.validSignatureCharacters:

                self._raiseException(
                    "The options signature is not a valid format", "https://google.com")

        return self

    def _raiseException(self, message, link):

        raise Exception(message, "Option:", self.option,
                        "Signature:", self.signature, "Documentation:", link)
