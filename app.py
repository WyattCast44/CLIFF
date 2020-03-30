import time
from src import Application
from src.UI import FilePicker

import types

# http://docopt.org/


def functionBasedOption(app):
    """Show a quick litte help message"""

    path = FilePicker().setTitle(
        'Function File Picker').allowMultiple(False).prompt().getPath()

    print(path)


Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
}).registerOptions({
    '--f|--flag': functionBasedOption
}).registerCommands({
    'run:app|run:wyatt': functionBasedOption
}).run()
