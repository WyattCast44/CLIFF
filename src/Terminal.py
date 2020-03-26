import os


class Terminal:

    def __init__(self):

        self.width = os.get_terminal_size().columns
        self.height = os.get_terminal_size().lines

        return
