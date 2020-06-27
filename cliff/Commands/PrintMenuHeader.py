import textwrap


class PrintMenuHeader:

    signature = "print:menu-header"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        print(
            f"\n{self.application.config()['name']} - {self.application.config()['version']}")
        print(f"{self.application.config()['description']}")
