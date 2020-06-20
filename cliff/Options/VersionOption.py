from cliff import Application


class VersionOption:

    signature = "--v"

    def __init__(self, application: Application):

        self.application = application

    def handle(self):

        print(f'\nv{self.application._config.get("version")}')

        self.application.exit(0)
