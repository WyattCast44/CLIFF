from cliff import Application


class ListCommand:

    signature = "list"

    def handle(application: Application):

        print("\nListing options and commands...",
              f"Env is: {application._config.get('env')}")
