from .YoloCommand import YoloCommand


class CatProvider:

    def __init__(self, application):

        self.application = application

    def register(self):

        pass

    def boot(self):

        self.application.registerCommands([
            YoloCommand
        ])
