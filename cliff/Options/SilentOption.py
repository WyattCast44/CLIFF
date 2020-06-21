from cliff import Application


class SilentOption:

    signature = "--silent"

    def __init__(self, application: Application):

        self.application = application

    def handle(self):

        self.application._config.merge({
            'silent': True
        })
