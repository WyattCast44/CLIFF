import colored
from colored import stylize


class OptionSignatureValidationError(Exception):
    pass

    def __init__(self, signature):

        self.signature = signature

        return

    def print(self):

        print(stylize("\nERROR", colored.bg('red')),
              stylize(self.__class__.__name__, colored.fg('red')), '\n')
        print(f"Given:\n - {self.signature}")
        print(
            f"Expected:\n - Option signatures must start with either a single or double hypen")

        return
