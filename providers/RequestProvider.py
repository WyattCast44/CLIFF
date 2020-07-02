import requests


class RequestProvider(object):

    def __init__(self, application) -> None:

        self.application = application

    def register(self):

        self.application.macro('get', requests.get)

    def boot(self):

        pass
