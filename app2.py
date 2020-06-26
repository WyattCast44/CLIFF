from cliff import Application
from cliff.helpers import config
from cliff.Options import SilentOption
from providers import CatProvider, RequestProvider
from cliff.Commands import PrintMainMenu, HelpCommand

import os

app = Application({
    'name': "Testing Application",
    'description': "This is a demo application for CLIFF",
    "providers": [
        CatProvider,
        RequestProvider
    ]
}).registerOptions([
    SilentOption
]).registerCommands([
    PrintMainMenu,
]).registerCommands([
    HelpCommand,
], 'dev')

app.setDefaultCommand(PrintMainMenu)

app.run()
