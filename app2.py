from pprint import pprint
from cliff import Application
from providers import RequestProvider, DatabaseProvider
from cliff.Options import SilentOption, VersionOption
from cliff.Commands import PrintMainMenu, HelpCommand, MakeCommand

app = Application({
    'name': "Testing Application",
    'version': "1.0.2",
    'providers': [
        RequestProvider,
        DatabaseProvider
    ]
}).registerOptions([
    SilentOption,
    VersionOption,
]).registerCommands([
    HelpCommand,
    PrintMainMenu,
]).registerCommands([
    MakeCommand
], 'prod').setDefaultCommand(PrintMainMenu)

app.run()
