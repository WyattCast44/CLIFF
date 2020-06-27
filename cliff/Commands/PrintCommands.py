import types
import inspect
import textwrap
from cliff.helpers import s


class PrintCommands:

    signature = "print:commands"

    def __init__(self, application):

        self.application = application

        self.commands = self.application._commands.items()

    def handle(self, params=None):

        maxLength = 0

        for signature in self.commands:

            signature = s(signature).green()

            if len(signature) > maxLength:

                maxLength = len(signature)

        print(s("\nAvailable Commands:").yellow())

        for signature in sorted(self.commands):

            handler = self.commands.get(signature)

            if hasattr(handler, "description"):

                if type(handler.description) == types.FunctionType:
                    description = handler.description()
                else:
                    description = handler.description

            elif hasattr(handler, "getDescription"):

                description = handler.getDescription()

            elif hasattr(handler, "get_description"):

                description = handler.get_description()

            elif handler.__doc__ != None:

                description = inspect.cleandoc(handler.__doc__)

            else:

                description = ""

            print(
                f"> {s(signature).green():<{maxLength + 3}}{description}")
