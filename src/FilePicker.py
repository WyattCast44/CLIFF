import os
import tkinter as tk
from tkinter import filedialog


class FilePicker:

    # @link https://pythonspot.com/tk-file-dialogs/

    defaults = {
        'title': 'Select Files',
        'filetypes': [],
        'initialDir': os.getcwd()
    }

    def __init__(self, config: dict = {}):

        # Init the tkinter instance
        self.win = tk.Tk()

        # Hide the tkinter root window
        self.win.withdraw()

        # Set the initial state of cancelled
        self.cancelled = None

        # Merge in any user config
        self.defaults.update(config)

        return

    def setTitle(self, title: str):
        """Set the title of the filepicker dialog"""

        self.defaults["title"] = title

        return self

    def setFiletypes(self, types: list):
        """Set the allowable file types of the filepicker"""

        self.defaults["filetypes"] = types

        return self

    def prompt(self):
        """Show the file picker and prompt user to select file(s)"""

        path = filedialog.askopenfilename(
            initialdir=self.defaults["initialDir"], title=self.defaults["title"])

        # If the path is an empty string
        # the user cancelled, update cancelled
        # state
        if path == "":
            self.cancelled = True
        else:
            self.cancelled = False

        return path

    def wasCancelled(self):
        """Determine whether or not the user cancelled selecting a file"""

        return self.cancelled

    def __del__(self):

        # Clean up tkinter instance
        self.win.destroy()


p = FilePicker()

p.prompt()

print(p.wasCancelled())
