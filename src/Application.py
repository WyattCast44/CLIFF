import sys
import inspect
from src.Menus import HelpMenu
from src.Events import EventBus
from src.Container import Container
from src.Commands import CommandFinder
from src.Commands import CommandValidator
from src.Options import OptionFinder


class Application:

    defaults = {
        'name': 'Console Application',
        'version': '1.0.0',
        'description': 'Helping you build command line applications',
        'env': 'dev',
        'width': 55,
    }

    options = {}

    commands = {}

    defaultCommand = None

    def __init__(self, config: dict = {}):

        # Merge the defaults and user config
        self.config = {**self.defaults, **config}

        # Bind the container
        self.container = Container(self)

        # Register base bindings
        self.container.bind("Application", self)
        self.container.bind("EventBus", EventBus())
        self.container.bind("HelpMenu", HelpMenu)

        self.container.resolve("EventBus").fire('app:starting')

        # Grab the name of the script
        self.script = sys.argv[0]

        # Grab any args passed to the app
        self.args = sys.argv[1:]

        return

    def env(self):

        # Return the current
        # application env

        return self.config['env']

    def container(self):

        return self.container

    def registerOptions(self, options):

        if type(options) == list:

            # If we get a list, then we can assume
            # it is a list of class based options
            # in the future, I'd like to expand and
            # allow functions to be registered.
            # The problem is we need a some type
            # signature to assign

            for option in options:

                # Options can be overwritten
                # I think this is good, because
                # I'd like users to be able to
                # override any default options

                self.container.resolve("EventBus").fire(
                    'options:register', [option])

                self.options[option.signature] = option

        elif type(options) == dict:

            # If we get a dict, then we can assume
            # it is a list of signatures and handlers

            for signature, handler in options.items():

                # Options can be overwritten
                # I think this is good, because
                # I'd like users to be able to
                # override any default options

                self.container.resolve("EventBus").fire(
                    'options:register', [signature, handler])

                self.options[signature] = handler

        return self

    def registerCommands(self, commands):

        if type(commands) == list:

            # If we get a list, then we can assume
            # it is a list of class based commands
            # in the future, I'd like to expand and
            # allow functions to be registered.
            # The problem is we need a some type
            # signature to assign

            for command in commands:

                # Options can be overwritten
                # I think this is good, because
                # I'd like users to be able to
                # override any default options

                self.eventbus.fire('commands:register', [command])

                self.commands[command.signature] = command

        elif type(commands) == dict:

            # If we get a dict, then we can assume
            # it is a list of signatures and handlers

            for signature, handler in commands.items():

                # Options can be overwritten
                # I think this is good, because
                # I'd like users to be able to
                # override any default options

                self.container.resolve("EventBus").fire(
                    'commands:register', [signature, handler])

                self.commands[signature] = handler

        return self

    def setDefaultCommand(self, command):

        # A dev can set a default command
        # that will run if the user runs
        # the app w/o passing any args.
        # One tradeoff with default commands
        # is that they will not be able to
        # accept any arguments, the question
        # of whether or not to register it
        # with other app commands remains?

        self.defaultCommand = command

        return self

    def _runCommand(self, command):

        # Get the handler out of the commands
        handler = self.commands[command]

        # Determine how to handle the command
        if inspect.isclass(handler):

            # Command is a class based
            # command, pass the application
            # and call handle while passing
            # the args
            handler(self).handle()

        elif callable(handler):

            # Command is callable
            # pass the application and
            # any args
            handler(self)

        return self

    def _runDefaultCommand(self):

        # We need to determine if the default command
        # is a class based command or a function
        # handler.

        if inspect.isclass(self.defaultCommand):
            self.defaultCommand(self).handle()
        else:
            self.defaultCommand(self)

        return self

    def run(self):

        self.container.resolve("EventBus").fire('app:running')

        # First thing to do is
        # check if we have a default
        # command to run, and no args
        # were passed

        if not self.defaultCommand == None and len(self.args) == 0:

            self._runDefaultCommand()

            return

        # Alright, not running a default command
        # Let's check if we have any args passed
        # If none, lets just print the help menu

        if len(self.args) == 0:

            # HelpMenu(self, self.config["width"]).render()

            menu = self.container.resolve("HelpMenu")(
                self, self.config["width"]).render()

        else:

            # Houston we have arguments, lets first
            # see if we can find an option that finds
            # matches the first arg
            option = OptionFinder(self).search()

            if not option == None:

                # We found a matching option, lets run that option
                print(f"\nTODO - Run option {option}\n")

                return

            command = CommandFinder(self).search()

            if not command == None:

                # We found a matching command, lets run that command
                print(f"\nTODO - Run command {command}\n")

                return

            print("\nTODO - Raise a exception, no matching option or command found")

    def __del__(self):

        self.container.resolve("EventBus").fire('app:end')

        return
