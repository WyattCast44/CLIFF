from .PrintUsage import PrintUsage
from .PrintOptions import PrintOptions
from .PrintCommands import PrintCommands
from .PrintMenuHeader import PrintMenuHeader

import os


class PrintMainMenu:
    """Print the application main menu"""

    signature = "print:menu"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        PrintMenuHeader(self.application).handle()
        PrintUsage(self.application).handle()
        PrintOptions(self.application).handle()
        PrintCommands(self.application).handle()

        self.application.exit(0)
