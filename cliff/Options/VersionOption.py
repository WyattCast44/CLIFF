from cliff import Application
from cliff.helpers import s


class VersionOption:

    signature = "--v"

    def __init__(self, application: Application):

        self.application = application

    def handle(self):

        print(f'\n{s("v").green()}{self.application.config()["version"]}')

        self.application.exit(0)
