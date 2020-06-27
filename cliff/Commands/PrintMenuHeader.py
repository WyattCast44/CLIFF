import textwrap
from cliff.helpers import s


class PrintMenuHeader:

    signature = "print:menu-header"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        name = self.application.config()['name']
        version = self.application.config()['version']
        desc = self.application.config()['description']

        print(f"\n{s(name).green()} - v{version}")

        print(f"\n{s(desc).color('dark_gray')}")
