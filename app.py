from src import Application
from commands import ShowHelpMenu


def functionBasedOption(app):
    """Show a quick litte help message"""

    print(app)


def funTwo(app):
    """Doc string desc"""

    print(app)


Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.'
}).registerOptions({
    '-v, --versions': functionBasedOption
}).registerCommands([
    ShowHelpMenu
]).run()
