import pprint
import inspect
from cliff import Application
from providers import RequestProvider, DatabaseProvider
from cliff.Options import SilentOption, VersionOption
from cliff.Commands import PrintMainMenu, HelpCommand, MakeCommand, DumpConfig
from cliff.helpers import dd

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
    MakeCommand,
    DumpConfig
], 'dev').setDefaultCommand(PrintMainMenu)


class Ty:

    def handle(self, param2: dict, param1={}):

        pass


params = Ty.handle.__code__.co_varnames[1:]
params2 = inspect.signature(Ty.handle).parameters['param2'].annotation
dd(params, len(params), params2 == dict)


app.run()
