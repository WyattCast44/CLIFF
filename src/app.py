from Application import Application


def myFunc(app):
    """ This function is a closure based option"""
    print('wyatts app', app)


class MyClass:

    signature = "key:first"

    description = "My command class"

    def __init__(self, application: Application):

        return

    def handle(self):

        print('class based command...')


Application({
    'name': 'NetScan Port Tool',
    'description': 'Let us see how a really long program description looks in the help menu.',
}).registerOptions({
    'long:key': myFunc
}).registerCommands([
    MyClass
]).run()
