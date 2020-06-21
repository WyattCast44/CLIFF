import os
import textwrap
from cliff import Application
from cliff.Commands import PrintMainMenu, HelpCommand

Application({
    'name': "Testing Application",
}).registerCommands([
    HelpCommand,
    PrintMainMenu
]).setDefaultCommand(PrintMainMenu).run()
