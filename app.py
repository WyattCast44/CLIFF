from src import Application


def functionBasedOption(app):
    """Show a quick litte help message"""

    print(app)


app = Application({
    'name': 'Example App',
    'description': 'This is an example CLI app.',
    'version': "0.1.3"
}).registerOptions({
    '-flag|--w': functionBasedOption
}).registerCommands({
    'run:app': functionBasedOption
}).run()
