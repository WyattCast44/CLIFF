from cliff import Application
from cliff.Options import SilentOption
from cliff.Commands import PrintMainMenu, HelpCommand

app = Application({
    'name': "Testing Application",
    'description': "This is a demo application",
}).registerOptions([
    SilentOption
]).registerCommands([
    HelpCommand,
    PrintMainMenu,
]).setDefaultCommand(PrintMainMenu)

app.run()
