import textwrap
from cliff.helpers import s


class PrintUsage:

    signature = "print:usage"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        print(s("\nUsage:").yellow())

        message = f"> {self.application._config.get('script')}"

        if len(self.application._options.all()) > 0:

            message = message + " [option(s)]"

        if len(self.application._commands.all()) > 0:

            message = message + " command [argument(s)]"

        message = textwrap.fill(message, self.application._config.get('width'))

        print(message)
