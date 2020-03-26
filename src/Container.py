import inspect


class Container:

    bindings = {}

    singletons = {}

    def __init__(self):

        return

    def resolve(self, key):

        binding = self.bindings[key]

        print(binding)

        # Check if is class
        if inspect.isclass(binding):
            return binding()

        # Check if is instance
        if isinstance(binding, binding):
            return binding

        # Check if is function
        if callable(binding):
            return binding()

        # Unknown, just return binding
        return binding

    def bind(self, key, value):

        self.bindings[key] = value

        return

    def singleton(self, key, value):

        return

    def instance(self, instance):

        return

container = Container()
