from cliff import Application
from .PrintOptions import PrintOptions
from .PrintCommands import PrintCommands


class ListCommand:

    signature = "list"

    def __init__(self, application: Application):

        self.application = application

    def handle(self, params=None):

        if len(params) == 0:

            PrintOptions(self.application).handle()

            PrintCommands(self.application).handle()

        else:

            if params[0] == "options":

                PrintOptions(self.application).handle()

            if params[0] == "commands":

                PrintCommands(self.application).handle()

        self.application.exit(0)

        raise Exception("Uknown parameter passed to 'list', please try again")
