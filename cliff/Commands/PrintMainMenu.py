from .PrintUsage import PrintUsage
from .PrintOptions import PrintOptions
from .PrintCommands import PrintCommands


class PrintMainMenu:

    signature = "print:menu"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        PrintUsage(self.application).handle()
        PrintOptions(self.application).handle()
        PrintCommands(self.application).handle()

        self.application.exit(0)
