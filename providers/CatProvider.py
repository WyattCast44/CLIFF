from .YoloCommand import YoloCommand


class CatProvider:

    def __init__(self, application):

        self.application = application

    def boot(self):

        self.application.config().set('env', 'prod')

        self.application.registerCommands([
            YoloCommand
        ])
