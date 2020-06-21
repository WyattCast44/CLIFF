import textwrap


class PrintOptions:

    signature = "print:options"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        print(f"\nAvailable Options:")

        for option in self.application._options.items():

            print(f" {textwrap.fill(option, self.application._config.get('width'))}")
