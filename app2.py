from cliff import Application
from providers import RequestProvider
from cliff.Options import SilentOption, VersionOption
from cliff.Commands import PrintMainMenu, HelpCommand

app = Application({
    'name': "Testing Application",
    'providers': [
        RequestProvider
    ]
}).registerOptions([
    VersionOption,
    SilentOption,
]).registerCommands([
    HelpCommand,
    PrintMainMenu,
]).setDefaultCommand(PrintMainMenu)

app.run()
