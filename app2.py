from cliff import Application
from cliff.Options import SilentOption
from cliff.Commands import PrintMainMenu, HelpCommand

Application({
    'name': "Testing Application",
}).registerCommands([
    HelpCommand,
    PrintMainMenu,
]).registerOptions([
    SilentOption
]).setDefaultCommand(PrintMainMenu).run()


'''
CLAP - Command Line Applications in Python
'''
