from cliff import Application


class IdealCommand:
    """This is the command desc"""

    # or

    description = "This is the command desc"

    signature = "ideal:command"

    # or

    signature = [
        "ideal"
        "ideal:command"
    ]

    params = [
        "name": ['str', 'required']
        "--flag": ['bool', 'optional']
        "--number": ['int', 'optional', 'max:5']
    ]

    def __init__(self, app: Application):

        self.app = app

    def handle(self):

        pass


def validate(value, rules):
