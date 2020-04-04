from src import Application
from commands import ShowHelpMenu


def showVersion(app):
    """Show a quick litte help message"""

    print(app.config['version'])


def funTwo(app):
    """Doc string desc"""

    print(app)


Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.'
}).registerOptions({
    '-V, --version': showVersion
}).registerCommands([
    ShowHelpMenu
]).run()
