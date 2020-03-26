from box import Box


class State:

    def __init__(self, raiseExceptions=True):

        self.context = Box({})

        self.raiseExceptions = raiseExceptions

        return

    def set(self, key, value, overide=False):

        # If key not set, no problem
        if not self.has(key):

            self.context.key = value

            return True

        # Key is set, check if overide is true
        if overide:

            self.context.key = value

            return True

        if self.raiseExceptions:
            raise Exception(
                f'Cannot set `{key}` in state, `{key}` is already to: {self.get(key)}.')
            return
        else:
            return False

    def get(self, key=None, default=None):

        return

    def update(self, key, value):

        return

    def unset(self, key, catchExceptions=True):

        return

    def upsert(self, key, value):

        return

    def has(self, key):

        return

    def all(self):

        return
