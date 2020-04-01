import colored
from colored import stylize
from src.Exceptions import PrettyException


class OptionSignatureValidationError(PrettyException):
    pass

    def __init__(self, signature, config={}):

        self.signature = signature

        self.setName("Option Signature Validation Error")
        self.setProblem(
            "Option signatures must start with either a single or double hypen.")
        self.setGiven(self.signature)

        self.build().print()

        exit()

        return
