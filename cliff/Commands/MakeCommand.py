from cliff import Application


class MakeCommand:
    """Generate a new command class"""

    signature = "make:command"

    def __init__(self, application: Application):

        self.application = application

    def handle(self, params=None):
        """Generates a new command class file in your root 'commands' directory. Also updated __init__.py file in your root `commands` directory"""

        print("\nTODO")

        self.application.exit(0)
