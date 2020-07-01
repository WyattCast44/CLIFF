from pprint import pprint


class DumpConfig:

    signature = "dump:config"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        print()
        pprint(self.application.config().all())
