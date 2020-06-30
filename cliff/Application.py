from __future__ import annotations
import os
import sys
import string
import inspect
from cliff.Support import Repository
from cliff.Commands import MakeCommand
from cliff.Commands import CommandValidator
from cliff.Options import OptionValidator


class Application:

    _config = Repository({
        'name': 'Console Application',
        'description': 'A simple CLI application',
        'version': '1.0.0',
        'env': 'dev',
        'width': 70,
        'silent': False,
        'providers': [],
    })

    _defaultCommand = None

    _commands = Repository({})

    _options = Repository({})

    _registeredProviders = []

    _params = None

    def __init__(self, config: dict = {}):

        self._config.merge(config)

        self._config.set('script', sys.argv[0])

        self._params = sys.argv[1:]

        self._registerInternalCommands()

        self._registerProviders()

    def registerOptions(self, options, env=None) -> Application:

        if env != None:

            if self._config.get('env') != env:

                return self

        if type(options) == list:

            for option in options:

                signature, option = OptionValidator(self).validate(option)

                self._options.set(signature, option)

            return self

        elif type(options) == dict:

            for signature, option in options.items():

                signature, option = OptionValidator(
                    self).validate(option, signature)

                self._options.set(signature, option)

        else:

            raise Exception(
                "Unrecognized format for registering option", "Details: https://google.com")

        return self

    def _registerInternalCommands(self) -> None:

        self.registerCommands([
            MakeCommand
        ], 'dev')

    def registerCommands(self, commands, env=None) -> Application:

        if env != None:

            if self._config.get('env') != env:

                return self

        if type(commands) == list:

            for command in commands:

                signature, command = CommandValidator(self).validate(command)

                self._commands.set(signature, command)

        elif type(commands) == dict:

            for signature, handler in commands.items():

                signature, command = CommandValidator(
                    self).validate(handler, signature)

                self._commands.set(signature, command)

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

        self._bootProviders()

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

    def config(self):

        return self._config

    def _bootProviders(self):

        for provider in self._registeredProviders:

            provider.boot()

    def _registerProviders(self):

        for provider in self.config().get('providers'):

            tmp = provider(self)

            tmp.register()

            self._registeredProviders.append(tmp)

    def exit(self, code=0) -> None:

        sys.exit(code)

    def __del__(self):

        sys.stdout = sys.__stdout__
