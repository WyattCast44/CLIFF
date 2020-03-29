from src import Application
import time
from src.UI import FilePicker


def functionBasedOption(app):
    """Show a quick litte help message"""

    path = FilePicker().setTitle('Function File Picker').prompt().getPath()

    print(path)


Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
}).registerOptions({
    '--f|--flag': functionBasedOption
}).registerCommands({
    'run:app|run:wyatt': functionBasedOption
}).run()
