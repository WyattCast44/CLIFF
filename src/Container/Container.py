import os
import inspect
from src import Application


class Container:

    bindings = {}

    singletons = {}

    def __init__(self, application: Application):

        self.application = application

        self.bind('cwd', os.getcwd())
        self.bind('root', os.path.realpath(__file__))

        return

    def resolve(self, key):

        # TODO make this an actual
        # useful container, and inspect
        # the constructor to inject
        # dependencies

        return self.bindings[key]

    def bind(self, key, value):

        self.bindings[key] = value

        return

    def singleton(self, key, value):

        return

    def instance(self, instance):

        return

    def __del__(self):

        return
