from cliff import Application


class ListCommand:

    signature = "list"

    def __init__(self, application: Application):

        self.application = application

    def handle(self, params=None):

        if len(params) == 0:
            print("\nList all options and commands")
            self.application.exit(0)

        if params[0] == "options":
            print("\nList all options")
            self.application.exit(0)

        if params[0] == "commands":
            print("\nList all commands")
            self.application.exit(0)

        # check for command namespaces

        raise Exception("Uknown parameter passed to 'list', please try again")
