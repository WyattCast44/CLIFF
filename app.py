from src import Application
import time


def functionBasedOption(app):
    """Show a quick litte help message"""

    print("\nTODO\n")


Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
}).registerOptions({
    '--f|--flag': functionBasedOption
}).run()

time.sleep(10)
