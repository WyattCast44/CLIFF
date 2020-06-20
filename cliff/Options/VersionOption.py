from cliff import Application


class VersionOption:

    signature = "--v"

    def handle(application: Application):

        print(f'\nv{application._config.get("version")}')

        application.exit(0)
