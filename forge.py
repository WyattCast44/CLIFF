from cliff import Application
from providers import ForgeProvider
from commands import ListServers
from cliff.Commands import PrintMainMenu

Application({
    'name': "Laravel Forge CLI",
    'version': '0.1.0',
    'providers': [
        ForgeProvider
    ]
}).registerCommands([
    ListServers,
    PrintMainMenu
]).setDefaultCommand(PrintMainMenu).run()
