from src import Application
import time
from src.UI import FilePicker

# http://docopt.org/


def functionBasedOption(app):
    """Show a quick litte help message"""

    path = FilePicker().setTitle(
        'Function File Picker').allowMultiple(True).prompt().getPath()

    print(path)


Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
}).registerOptions({
    '--f|--flag': functionBasedOption
}).registerCommands({
    'run:app|run:wyatt': functionBasedOption
}).run()
