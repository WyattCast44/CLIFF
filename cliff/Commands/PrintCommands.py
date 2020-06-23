import inspect
import types


class PrintCommands:

    signature = "print:commands"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        print(f"\nAvailable Commands:")

        commands = self.application._commands.items()

        for signature in sorted(commands):

            handler = commands.get(signature)

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

            print(f"> {signature}   {description}")
