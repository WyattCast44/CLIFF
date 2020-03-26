import inspect
import textwrap


class HelpMenu:

    def __init__(self, application, width=55):

        self.width = width

        self.app = application

        return

    def build(self):

        script = self.app.script
        name = self.app.config["name"]
        vers = f'v{self.app.config["version"]}'
        desc = "\n".join(textwrap.wrap(
            self.app.config["description"], self.width))
        padding = " " * (self.width - (len(name) + len(vers)))

        output = f"\n{name}{padding}{vers}\n"
        output = output + f"{'-' * self.width}\n"
        output = output + f"{desc}\n"
        output = output + self.buildUsageLine()
        output = output + self.buildOptionsList()
        output = output + self.buildCommandsList()

        return output

    def buildUsageLine(self):

        return f"\nUsage: {self.app.script} [option/command]\n"

    def buildOptionsList(self):

        output = ""

        # If no options are registered
        # we will skip building this section out
        if len(self.app.options) == 0:

            return output

        # Alright we have registered options
        # lets build out the signature/desc

        # First lets get the length of the longest
        # option signatures
        maxLength = len(max(self.app.options.keys(), key=len))

        output = "\nOptions:"

        # Now lets loop through all signatures
        # and handlers to generate the options
        # list
        for signature, handler in self.app.options.items():

            signature = "  " + signature + \
                (" " * (maxLength - len(signature) + 2))

            if inspect.isclass(handler):

                output = output + f"\n{signature}{handler.description}"

            elif callable(handler):

                desc = ""

                if not handler.__doc__ == None:
                    desc = handler.__doc__

                output = output + f"\n{signature}{desc}"

        return output + "\n"

    def buildCommandsList(self):

        output = ""

        # If no options are registered
        # we will skip building this section out
        if len(self.app.commands) == 0:

            return output

        # Alright we have registered options
        # lets build out the signature/desc

        # First lets get the length of the longest
        # command signatures
        maxLength = len(max(self.app.commands.keys(), key=len))

        output = "\nCommands:"

        for signature, handler in self.app.commands.items():

            signature = "  " + signature + \
                (" " * (maxLength - len(signature) + 3))

            if inspect.isclass(handler):

                if hasattr(handler, "description"):
                    output = output + \
                        f"\n{signature}{handler.description}"
                elif not handler.__doc__ == None:
                    output = output + \
                        f"\n{signature}{handler.__doc__}"
                else:
                    output = output + f"\n{signature}"

            elif callable(handler):

                desc = ""

                if not handler.__doc__ == None:
                    desc = handler.__doc__

                output = output + f"\n{signature}{desc}"

        return output + "\n"

    def render(self):

        print(self.build())

        return
