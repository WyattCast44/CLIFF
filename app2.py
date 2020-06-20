from cliff import Application


def main(application: Application, params=None):
    """Docstring description"""
    pass


class Test:

    def __init__(self, application: Application):

        self.application = application

    def get_signature():

        return "print"

    def handle(self, params=None):

        print(f"\nName: {self.application._config.get('name')}")
        print(f"Description: {self.application._config.get('description')}")
        print(f"Version: {self.application._config.get('version')}")


class EnvChanger:

    signature = "--prod"

    def __init__(self, app):

        self.app = app

    def handle(self):

        self.app._config.set('env', 'prod')


app = Application({
    'name': "Test",
    'version': '2.1.2.rc',
}).registerCommands([
    Test,
]).registerCommands({
    'main': main
}).registerOptions([
    EnvChanger
]).run()
