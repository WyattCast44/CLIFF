import sys
import inspect
from EventBus import EventBus


class Application:

    defaults = {
        'name': 'Console Application',
        'version': '1.0.0',
        'description': 'Helping you build command line applications',
        'env': 'dev',
        'width': 55
    }

    options = {}

    commands = {}

    defaultCommand = None

    def __init__(self, config: dict = {}, eventbus: EventBus = None):

        # Merge the defaults and user config
        self.config = {**self.defaults, **config}

        # Register the event bus
        if not eventbus == None:
            self.eventbus = eventbus
        else:
            self.eventbus = EventBus()

        self.eventbus.fire('app:starting')

        # Grab the name of the script
        self.script = sys.argv[0]

        # Grab any args passed to the app
        self.args = sys.argv[1:]

        return

    def env(self):

        # Return the current
        # application env

        return self.config['env']

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

                self.eventbus.fire('options:register', [option])

                self.options[option.signature] = option

        elif type(options) == dict:

            # If we get a dict, then we can assume
            # it is a list of signatures and handlers

            for signature, handler in options.items():

                # Options can be overwritten
                # I think this is good, because
                # I'd like users to be able to
                # override any default options

                self.eventbus.fire('options:register', [signature, handler])

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

                self.eventbus.fire('commands:register', [signature, handler])

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

        self.eventbus.fire('app:run')

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

            from HelpMenu import HelpMenu

            HelpMenu(self, self.config["width"]).render()

    def __del__(self):

        self.eventbus.fire('app:end')

        return
