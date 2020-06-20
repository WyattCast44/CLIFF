from cliff import Application


class Test:

    def get_signature():

        return "v"

    def handle(app):

        print(f"\nName: {app._config.get('name')}")
        print(f"Description: {app._config.get('description')}")
        print(f"Version: {app._config.get('version')}")


class EnvChanger:

    signature = "--prod"

    def handle(app):

        app._config.set('env', 'prod')


app = Application({
    'name': "Test",
    'version': '2.1.2.rc'
}).registerCommands([
    Test
]).registerOptions([
    EnvChanger
]).run()
