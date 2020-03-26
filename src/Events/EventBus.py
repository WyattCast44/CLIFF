class EventBus:

    listeners = {}

    def __init__(self):

        return

    def fire(self, event, context=None):

        if not event in self.listeners:
            return

        for listener in self.listeners[event]:

            listener(context)

        return self

    def listen(self, event, handler):

        if not event in self.listeners:
            self.listeners[event] = []

        if not handler in self.listeners[event]:
            self.listeners[event].append(handler)

        return self
