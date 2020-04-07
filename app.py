from src import Application
from commands import ShowHelpMenu
from src.Support.helpers import s


def showVersion(app):
    """Show a quick litte help message"""

    print(s(app.config['version']).green())


app = Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.'
}).registerOptions({
    '-V, --version': showVersion
}).registerCommands([
    ShowHelpMenu
]).run()
