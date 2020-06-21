from __future__ import annotations
import os
import sys
import string
import inspect
from cliff.Support import Repository


class Application:

    _config = Repository({
        'name': 'Console Application',
        'description': 'Helping you build CLI apps',
        'version': '1.0.0',
        'env': 'dev',
        'width': 70,
        'silent': False,
    })

    _defaultCommand = None

    _commands = Repository({})

    _options = Repository({})

    _params = None

    def __init__(self, config: dict = {}):

        self._config.merge(config)

        self._registerInternalOptions()

        self._registerInternalCommands()

        self._config.set('script', sys.argv[0])

        self._params = sys.argv[1:]

    def _registerInternalOptions(self) -> None:

        pass

    def registerOptions(self, options) -> Application:

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

    def _registerInternalCommands(self) -> None:

        pass

    def registerCommands(self, commands) -> Application:

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

    def setDefaultCommand(self, command: callable) -> Application:

        if hasattr(command, "signature"):

            signature = command.signature

        elif hasattr(command, "getSignature"):

            signature = command.getSignature()

        elif hasattr(command, "get_signature"):

            signature = command.get_signature()

        else:

            raise Exception(
                "The given command does not have a recognizable signature", "Command:", command)

        self._defaultCommand = signature

        if not self._commands.has(signature):

            self.registerCommands([
                command
            ])

        return self

    def hasDefaultCommand(self) -> bool:

        return self._defaultCommand != None

    def runCommand(self, command, params=None):

        handler = self._commands.get(command)

        if inspect.isclass(handler):

            if len(inspect.signature(handler).parameters) > 0:
                handler(self).handle(params)
            else:
                handler().handle(self, params)

        elif inspect.isfunction(handler):

            handler(self, params)

        return self

    def run(self) -> None:

        optionsStack = []

        commandsStack = []

        commandFound = False

        commandParams = []

        if len(self._params) == 0 and self.hasDefaultCommand:

            self.runCommand(self._defaultCommand)

            self.exit(0)

        for param in self._params:

            if not commandFound:

                if param[0] == "-" or param[0:1] == "--":

                    if self._options.has(param):

                        optionsStack.append(param)

                elif self._commands.has(param):

                    commandsStack.append(param)

                    commandFound = True

                else:

                    pass

            else:

                commandParams.append(param)

        for option in optionsStack:

            handler = self._options.get(option)

            if hasattr(handler, "handle"):
                handler(self).handle()
            else:
                handler(self)

        if self._config.get('silent'):
            sys.stdout = open(os.devnull, 'w')

        for command in commandsStack:

            self.runCommand(command, commandParams)

        self.exit(0)

    def exit(self, code=0) -> None:

        sys.exit(code)

    def __del__(self):

        sys.stdout = sys.__stdout__
