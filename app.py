import time
from src import Application
from src.UI import FilePicker
from src.Support import helpers
from src.Support import Str

import types

# http://docopt.org/
# http://effbot.org/librarybook/formatter.htm
# https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56


def functionBasedOption(app):
    """Show a quick litte help message"""

    path = FilePicker().setTitle(
        'Function File Picker').allowMultiple(False).prompt().getPath()

    print(path)


app = Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
    'version': "0.1.3"
}).registerOptions({
    'flag|--w': functionBasedOption
}).registerCommands({
    'run:app': functionBasedOption
}).run()
