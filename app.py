import sys
from src import Application
import traceback


def functionBasedOption(app):
    """Show a quick litte help message"""

    print(app)


def funTwo(app):

    print(app)


Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
    'version': "0.1.3",
    'strict_registration': True
}).registerOptions({
    '-v, --versions': functionBasedOption,
    '-v|--version': funTwo
}).registerCommands({
    'run:app': functionBasedOption
}).run()
