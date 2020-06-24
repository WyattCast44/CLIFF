from cliff import Application
from cliff.Options import SilentOption
from cliff.Commands import PrintMainMenu, HelpCommand
from providers import CatProvider

app = Application({
    'name': "Testing Application",
    'description': "This is a demo application for CLIFF"
})

app.registerProviders([
    CatProvider
])

app.registerOptions([
    SilentOption
])

app.registerCommands([
    PrintMainMenu,
]).registerCommands([
    HelpCommand,
], 'dev')

app.setDefaultCommand(PrintMainMenu)

app.run()
