import textwrap
from cliff.helpers import s


class PrintOptions:

    signature = "print:options"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        if len(self.application._options) == 0:

            return

        print(s("\nAvailable Options:").yellow())

        for option in sorted(self.application._options.items()):

            print(
                f" {textwrap.fill(option, self.application._config.get('width'))}")
