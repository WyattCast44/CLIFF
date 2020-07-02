class ListServers:

    signature = "servers:list"

    description = "List all servers in your account"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        self.application.forge()
