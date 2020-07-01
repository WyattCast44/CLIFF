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

    # This is the base configuration for
    # the application
    _config = Repository({
        'name': 'Console Application',
        'description': 'A simple CLI application',
        'version': '1.0.0',
        'env': 'dev',
        'width': 70,
        'silent': False,
        'providers': [],
    })

    # If a default command has been set
    # this will be set to the signature
    # of the command
    _defaultCommand = None

    # This holds all registered options
    _options = Repository({})

    # This holds all registered commands
    _commands = Repository({})

    # This holds are providers that have
    # had the "register" method called
    # on them, it will be a list of service
    # provider instances, waiting for thier
    # boot methods to be called
    _registeredProviders = []

    # This is a list of all the parameters
    # passed to the script, if none were
    # passed, it will be an empty list
    _params = None

    def __init__(self, config: dict = {}):

        # The first thing we do is merge the
        # user config and the base config
        self._config.merge(config)

        # Next we grab the name of the script
        # and store it in the config repo
        self._config.set('script', sys.argv[0])

        # Next we set the params property to
        # any parameters passed to the script
        self._params = sys.argv[1:]

        # Next we loop thru any providers and
        # call the register method, these instances
        # will be stored in the registeredProviders
        # property
        self._registerProviders()

    def getEnv(self) -> str:

        return self.config().get('env')

    def envIs(self, toCheck: str) -> bool:

        return self.getEnv() == toCheck

    def registerOptions(self, options, env=None) -> Application:
        """Allows you to register multiple options with the application.

        Args:
            options (list, dict): The option(s) to register
            env (str): Register the option(s) if the application env is equal to the value passed. If no value is passed, the option(s) will be registered in all envs

        Returns:
            self: Returns the application instance.

        Examples:

        Register a class based option

        Application().registerOptions([
            MyOptionClass
        ])

        Register a class based option, but only if the application enviroment == dev 

        Application().registerOptions([
            MyOptionClass
        ], 'dev')

        Register a function based option

        Application().registerOptions({
            '--signature': myFunction
        })
        """

        # First we will check if the user passed an env
        # option. If so, we will check if the current env
        # is equal to what they passed, if not, we will
        # just return early
        if env != None:

            if not self.envIs(env):

                return self

        # Now we need to determine what type of data structure
        # they passed in
        if type(options) == list:

            # If it is a list, we can assume they passed in a
            # list of class based options. We will iterate through
            # and validate, if they pass validation, we will
            # register the option into the options repo
            for option in options:

                signature, option = OptionValidator(self).validate(option)

                self._options.set(signature, option)

            return self

        elif type(options) == dict:

            # If it is a dict, we can assume they passed in a
            # dict where the keys are the signatures, and the
            # values are the handlers. We will iterate thru
            # the options, validate the signature and handlder
            # and if it passes we will register the option into
            # the options repo
            for signature, option in options.items():

                signature, option = OptionValidator(
                    self).validate(option, signature)

                self._options.set(signature, option)

        else:

            # If they passed some other data structure, we
            # have no current way to parse the option, raise an
            # exception and exit
            raise Exception(
                "Unrecognized format for registering options", "Options:", options, "Documentation: https://google.com")

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

        signature, command = CommandValidator(self).validate(command)

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
