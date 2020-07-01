import inspect


class Singleton:

    _instance = None

    def __new__(cls):
        """
        Manages the creation of a singleton class
        """

        if cls._instance == None:

            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance

    def getInstance(self):

        return self._instance


class ContainerNew(Singleton):

    # The containers bindings
    bindings = {}  # { {'shared': bool, 'concrete': None|concrete} }

    # The containers shared instances
    instances = {}

    # The containers registered aliases
    aliases = {}

    # The containers resolved abstracts
    resolved = {}

    def bound(self, key) -> bool:
        """
        Determine if the given key has been bound.
        """

        if key in self.bindings:

            return True

        if key in self.instances:

            return True

        if key in self.aliases:

            return True

        return False

    def has(self, key) -> bool:
        """
        Determine if the given key has been bound.
        """

        return self.bound(key)

    def hasResolved(self, abstract) -> bool:
        """
        Determine if the given abstract has been resolved
        """

        if abstract in self.aliases:

            abstract = self.getAlias(abstract)

        if abstract in self.resolved:

            return True

        if abstract in self.instances:

            return True

        return False

    def getAlias(self, abstract):
        """
        Get an aliases base abstract
        """

        if not abstract in self.aliases:

            return abstract

        return self.getAlias(self.aliases[abstract])

    def getBindings(self) -> dict:
        """
        Return the list of registered bindings
        """

        return self.bindings

    def getInstances(self) -> dict:
        """
        Return the list of registered instances
        """

        return self.instances

    def isShared(self, abstract) -> bool:
        """
        Determine if a given type is shared
        """

        if abstract in self.instances:

            return True

        if abstract in self.bindings:

            if self.bindings[abstract]['shared']:

                return True

        return False

    def bind(self, abstract, concrete=None, shared=False):
        """
        Register a binding with the container
        """

        # If no concrete type was given, we will simply set the concrete type to the abstract type.
        if concrete == None:

            concrete = abstract

        # After that, the concrete type to be registered as shared without being
        # forced to state their classes in both of the parameters.

        # If the factory is not a Closure, it means it is just a class name which is bound
        # into this container to the abstract type and we will just wrap it up inside its
        # own Closure to give us more convenience when extending.

        if not self.isfunc(concrete):

            concrete = self.getfunc(abstract, concrete)

        self.bindings[abstract] = {
            'shared': shared,
            'concrete:': concrete
        }

    def bindIf(self, abstract, concrete=None, shared=False):
        """
        Bind an abstract into the container only if it hasn't been bound before
        """

        if not self.bound(abstract):

            self.bind(abstract, concrete, shared)

    def singleton(self, abstract, concrete=None):
        """
        Register a shared binding in the container
        """

        self.bind(abstract, concrete, shared=True)

    def singletonIf(self, abstract, concrete=None):
        """
        Register a shared binding if it hasn't already been bound.
        """

        if not self.bound(abstract):

            self.singleton(abstract, concrete)

    def instance(self, abstract, instance, autoInit=False):
        """
        Register an existing instance in the container, this instance will be shared
        """

        if self.isfunc(instance):

            raise Exception("Cannot bind a function using the instance method")

        elif instance is None:

            raise Exception("Cannot bind a function using the instance method")

        elif callable(instance):

            # If the instance is still callable, then it
            # is just a class name and not an instance
            # raise an error.
            raise Exception(
                "Cannot bind a non-instance using the instance method, please init your class before binding")

        exists = self.bound(abstract)

        # Remove any aliaseses
        self.aliases.pop(abstract, None)

        self.instances[abstract] = instance

    def removeAbstractAlias(searched):
        """
        Remove any alias to a abstract class?
        """

        if not searched in self.aliases:

            return

        return

    def isfunc(self, abstract) -> bool:
        """
        Determine if a given abstract is a function
        """

        if inspect.isfunction(abstract):

            return True

        if inspect.isbuiltin(abstract):

            return True

        return False

    def getfunc(self, abstract, concrete):
        """
        Used to wrap a abstact type in a function
        """

        def tmp(container, parameters=[]):

            if abstract == concrete:

                return self.build(concrete)

            return self.resolve(concrete, parameters)

        return tmp


# app = ContainerNew()


class Two:

    pass


def myf():

    pass


# app.singleton(Two)

# print(app.getInstances())
