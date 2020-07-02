from cliff import Application
from providers import DigitalOcean
from cliff.Commands import HelpCommand
from cliff.Commands import PrintMainMenu


def listDroplets(application, params=None):
    """List all droplets in your account"""

    droplets = application.do.get_all_droplets()

    print()

    for droplet in droplets:

        print(droplet.name)


app = Application({
    'name': "Digitial Ocean CLI",
    'version': '0.0.1',
    'providers': [
        DigitalOcean
    ]
}).registerCommands([
    HelpCommand,
    PrintMainMenu
]).registerCommands({
    'droplets:list': listDroplets,
    'droplets:create' listDroplets,
    'droplets:shutdown' listDroplets,
}).setDefaultCommand(PrintMainMenu)

app.run()
