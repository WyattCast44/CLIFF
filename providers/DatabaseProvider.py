import sqlite3
from cliff import Application


class DatabaseProvider:

    def __init__(self, application):

        self.application = application

    def register(self):

        db = sqlite3.connect('app.db')

        self.application.macro('db', db.cursor)

    def boot(self):

        pass
