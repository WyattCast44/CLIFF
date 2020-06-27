class RequestProvider(object):

    def __init__(self, application) -> None:

        self.application = application

    def register(self):

        self.application.config().set('key', 1)

    def boot(self):

        self.application.registerCommands({
            'request': main
        })


def main(application, params=None):

    print("\n", application.config().items())
