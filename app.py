import time
from src import Application
from src.UI import FilePicker
from src.Support import helpers

import types

# http://docopt.org/
# http://effbot.org/librarybook/formatter.htm


def functionBasedOption(app):
    """Show a quick litte help message"""

    path = FilePicker().setTitle(
        'Function File Picker').allowMultiple(False).prompt().getPath()

    print(path)


Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
    'version': "0.1.3"
}).registerOptions({
    '--f|--flag': functionBasedOption
}).registerCommands({
    'run:app|run:wyatt': functionBasedOption
}).run()
