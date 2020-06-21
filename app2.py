from cliff import Application
from cliff.Options import SilentOption
from cliff.Commands import PrintMainMenu, HelpCommand

app = Application({
    'name': "Testing Application",
    'env': 'dev',
})

app.registerProviders([
    HelpCommand,
])

app.registerCommands([
    PrintMainMenu,
])

app.registerOptions([
    SilentOption
])

app.registerCommands([
    HelpCommand,
], 'dev')

app.setDefaultCommand(PrintMainMenu)

app.run()
