import sys
import string
import inspect
from cliff.Support import Repository
from cliff.Commands import ListCommand
from cliff.Options import VersionOption


class Application:

    _config = Repository({
        'name': 'Console Application',
        'description': 'Helping you build CLI apps',
        'version': '1.0.0',
        'env': 'dev',
    })

    _defaultCommand = None

    _commands = Repository({})

    _options = Repository({})

    _params = None

    def __init__(self, config: dict = {}):

        self._config.merge(config)

        self._registerInternalCommands()

        self._registerInternalOptions()

        self._config.set('script', sys.argv[0])

        self._params = sys.argv[1:]

    def _registerInternalCommands(self):

        self.registerCommands([
            ListCommand
        ])

    def registerCommands(self, commands):

        if type(commands) == list:

            for command in commands:

                if hasattr(command, "signature"):

                    signature = command.signature

                elif hasattr(command, "getSignature"):

                    signature = command.getSignature()

                elif hasattr(command, "get_signature"):

                    signature = command.get_signature()

                else:

                    raise Exception(
                        "The given command does not have a recognizable signature", "Command:", command)

                if not signature[0] in string.ascii_lowercase:
                    raise Exception("The commands signature is not a valid format",
                                    "Command: ", command, "Signature: ", signature, "Details: https://google.com")

                self._commands.set(signature, command)

        elif type(commands) == dict:

            for signature, handler in commands.items():

                if not signature[0] in string.ascii_lowercase:
                    raise Exception("The commands signature is not a valid format",
                                    "Command: ", handler, "Signature: ", signature, "Details: https://google.com")

                self._commands.set(signature, handler)

        else:
            raise Exception(
                "Unrecognized format for registering command", "Details: https://google.com")

        return self

    def _registerInternalOptions(self):

        self.registerOptions([
            VersionOption
        ])

        return

    def registerOptions(self, options):

        if type(options) == list:

            for option in options:

                if hasattr(option, "signature"):

                    signature = option.signature

                elif hasattr(option, "getSignature"):

                    signature = option.getSignature()

                elif hasattr(option, "get_signature"):

                    signature = option.get_signature()

                else:

                    raise Exception(
                        "The given option does not have a recognizable signature", "Option:", option)

                # TODO Validate signature

                self._options.set(signature, option)

                return self

        elif type(options) == dict:

            for signature, handler in options.items():

                if not signature[0] == "-":
                    raise Exception("The options signature is not a valid format",
                                    "Option: ", handler, "Signature: ", signature, "Details: https://google.com")

                self._options.set(signature, handler)

        else:
            raise Exception(
                "Unrecognized format for registering option", "Details: https://google.com")

        return self

    def setDefaultCommand(self, command):

        self._defaultCommand = command

        return self

    def hasDefaultCommand(self) -> bool:
        """Check if the application has a default command set"""

        return self._defaultCommand != None

    def run(self):

        optionsStack = []

        commandsStack = []

        for param in self._params:

            if param[0] == "-" or param[0:1] == "--":

                if self._options.has(param):

                    optionsStack.append(param)

            elif self._commands.has(param):

                commandsStack.append(param)

            else:

                pass

        # We now have the options and commands stack we need to filter the params
        uknown = []

        for param in self._params:

            if param in optionsStack or param in commandsStack:

                pass

            else:

                uknown.append(param)

        # Actually Run the stacks
        # code	co_argcount	number of arguments (not including * or ** args)

        for option in optionsStack:

            handler = self._options.get(option)

            if hasattr(handler, "handle"):
                handler.handle(self)
            else:
                handler(self)

        for command in commandsStack:

            handler = self._commands.get(command)

            if hasattr(handler, "handle"):
                handler.handle(self)
            else:
                handler(self)

        print("\nOptions Stack:", optionsStack)
        print("Commands Stack:", commandsStack)
        print("App:", self._config.items())
        print("Options:", self._options.items())
        print("Commands:", self._commands.items())
        print("Uknown Stack:", uknown)

    def exit(self, code=0):

        quit(code)
