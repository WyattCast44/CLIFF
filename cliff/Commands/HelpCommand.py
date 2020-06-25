import inspect
import textwrap


class HelpCommand:
    """The help command displays help for a given command"""

    signature = "help"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):
        """The help command displays help for a given command"""

        if len(params) == 0:
            self._subject = "help"
        else:
            self._subject = params[0]

        self._handler = self._getCommandHandler(self._subject)

        self._printDescription()
        self._printUsage()
        self._printDetails()

        self.application.exit(0)

    def _getCommandHandler(self, signature):

        return self.application._commands.get(signature)

    def _getDescription(self):

        command = self._handler

        if inspect.isclass(command):

            if hasattr(command, "description"):

                description = command.description

            elif hasattr(command, "getDescription"):

                description = command.getDescription()

            elif hasattr(command, "get_description"):

                description = command.get_description()

            elif not command.__doc__ == None:

                description = command.__doc__

            else:

                description = "None"

        else:

            description = "TBD - Function"

        return description

    def _printDescription(self):

        print("\nDescription:")
        print(textwrap.fill(
            f" {self._getDescription()}", self.application._config.get('width'), subsequent_indent=" "))

    def _printUsage(self):

        print("\nUsage:")
        print(textwrap.fill(
            f"> {self.application._config.get('script')} {self._subject} [argument(s)]", self.application._config.get('width'), subsequent_indent=" "))

    def _printDetails(self):

        if not inspect.isclass(self._handler):

            return

        if not hasattr(self._handler, "handle"):

            return

        if self._handler.handle.__doc__ == None:

            return

        print("\nDetails:")
        print(textwrap.fill(" " + self._handler.handle.__doc__,
                            self.application._config.get('width'), subsequent_indent=" "))
