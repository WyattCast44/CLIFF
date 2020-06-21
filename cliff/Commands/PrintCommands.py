class PrintCommands:

    signature = "print:commands"

    def __init__(self, application):

        self.application = application

    def handle(self, params=None):

        print(f"\nAvailable Commands:")

        for command in self.application._commands.items():

            print(f"> {command}")
