import os
import textwrap
from cliff import Application
from cliff.Commands import PrintCommands, PrintOptions, PrintUsage

Application({
    'name': "Testing Application",
}).registerCommands([
    PrintUsage,
    PrintOptions,
    PrintCommands,
]).setDefaultCommand(PrintOptions).run()
