from src import Application


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
    '-v, --versions': functionBasedOption,
    '-v|--version': funTwo
}).registerCommands({
    'run:app': functionBasedOption,
    'serve': functionBasedOption
}).run()
