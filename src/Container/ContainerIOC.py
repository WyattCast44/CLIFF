import inspect

"""
@link https://gist.github.com/davejamesmiller/bd857d9b0ac895df7604dd2e63b23afe
"""


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


# app.bind(Two())

# print(app.getBindings())

# quit()


class ContainerIOC(Singleton):

    # An array of the types that have been resolved
    resolved = {}

    # The containers bindings
    bindings = {}

    # The containers method bindings
    methodBindings = []

    # The containers shared instances
    instances = {}

    # The registered type aliases
    aliases = {}

    # The registered aliases keyed by the abstract name
    abstractAliases = {}

    # All the registered tags
    tags = {}

    # The stack of concreations currently being built
    buildStack = []

    # The parameter override stack
    withStack = []

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

    def hasMethodBinding(self, method) -> bool:

        return method in self.methodBindings

    def resolved(self, abstract) -> bool:
        """
        Determine if the given abstract type has been resolved
        """

        if abstract in self.aliases:

            abstract = self.getAlias(abstract)

        if abstract in self.resolved:

            return True

        if abstract in self.instances:

            return True

    def getAlias(self, abstract):

        if not abstract in self.aliases:

            return abstract

        return self.getAlias(self.aliases[abstract])

    def getBindings(self):

        return self.bindings

    def isShared(self, abstract):
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

        # If no concrete type was given, we will simply set the concrete type to the abstract type. After that, the concrete type to be registered as shared without being forced to state their classes in both of the parameters.

        if concrete == None:

            concrete = abstract

        # If the factory is not a Closure, it means it is just a class name which is  bound into this container to the abstract type and we will just wrap it up inside its own Closure to give us more convenience when extending.
        if not self.isfunc(concrete):

            concrete = self.getfunc(abstract, concrete)

        self.bindings[abstract] = {
            'shared': shared,
            'concrete:': concrete
        }

    def bindMethod(self, method, callback):
        """
        Bind a callback to resolve with container::call
        """

        self.methodBindings[self.parseBindMethod(method)] = callback

    def callMethodBinding(self, method, instance):
        """
        Get the method binding for the given method.
        """

        return self.methodBindings[method](self)

    def bindIf(self, abstract, concrete=None, shared=False):

        if not self.bound(abstract):

            self.bind(abstract, concrete, shared)

    def singleton(self, abstract, concrete=None):
        """
        Register a shared binding in the container.
        """

        self.bind(abstract, concrete, shared=True)

    def singletonIf(self, abstract, concrete=None):
        """
        Register s shared binding if it hasn't already been registered.
        """

        if not self.bound(abstract):

            self.singleton(abstract, concrete)

    def parseBindMethod(method):
        """
        Get the method to be bound in the class@method format.
        """

        if type(method) == list:

            return f"{method[0]}@{method[1]}"

        return method

    def instance(self, abstract, instance):

        self.removeAbstractAlias(abstract)

        exists = self.bound(abstract)

        self.aliases.pop(abstract, None)

        # We'll check to determine if this type has been bound before, and if it has we will fire the rebound callbacks registered with the container and it can be updated with consuming classes that have gotten resolved here.
        # TODO
        self.instances[abstract] = instance

        return instance

    def removeAbstractAlias(searched):
        """
        TODO
        Remove an alias from the contextual binding alias cache
        """

        if not searched in self.aliases:

            return

        return

    def tag(self, abstracts: list, tags: list):
        """
        Assign a set of tags to a given binding
        """

        for tag in tags:

            if not tag in self.tags:
                self.tags[tag] = []

            for abstract in abstracts:

                self.tags[tag].append(abstract)

    def tagged(self, tag):

        if not tag in self.tags:
            return []

        items = []

        for abstract in self.tags[tag]:

            value = self.make(abstract)

            items.append(value)

        return items

    def make(self, abstract, parameters=[]):

        return self.resolve(abstract, parameters)

    def resolve(self, abstract, parameters=[], raiseEvents=True):

        abstract = self.getAlias(abstract)

        concrete = None  # TODO

        # If an instance of the type is currently being managed as a singleton we'll just return an existing instance instead of instantiating new instances so the developer can keep using the same objects instance every time.
        if abstract in self.instances:

            return self.instances[abstract]

        self.withStack = parameters

        if concrete == None:

            concrete = self.getConcrete(abstract)

        # We're ready to instantiate an instance of the concrete type registered for the binding. This will instantiate the types, as well as resolve any of its "nested" dependencies recursively until all have gotten resolved.
        if self.isBuildable(concrete, abstract):
            obj = self.build(concrete)
        else:
            obj = self.make(concrete)

    def build(self, concrete):

        # If the concrete type is actually a Closure, we will just execute it and hand back the results of the functions, which allows functions to be used as resolvers for more fine-tuned resolution of these objects.
        if self.isfunc(concrete):
            return concrete(self)

        return

    def getConcrete(self, abstract):

        # If we don't have a registered resolver or concrete for the type, we'll just  assume each type is a concrete name and will attempt to resolve it as is since the container should be able to resolve concretes automatically.

        if abstract in self.bindings:
            return self.bindings[abstract].get('concrete')

        return abstract

    def isBuildable(self, concrete, abstract):

        if concrete is abstract:

            return True

        if self.isfunc(concrete):

            return True

        return False

    def isfunc(self, abstract):

        if inspect.isfunction(abstract):

            return True

        if inspect.isbuiltin(abstract):

            return True

        return False

    def getfunc(self, abstract, concrete):

        def tmp(container, parameters=[]):

            if abstract == concrete:

                return self.build(concrete)

            return self.resolve(concrete, parameters)

        return tmp

    def dropStaleInstance(self, abstract):
        """
        Drop all the stale instances and aliases.
        """

        self.instances.pop(abstract, None)
        self.aliases.pop(abstract, None)

        return

    def forgetInstance(self, abstract):
        """
        Remove a resolved instance from the instance cache.
        """

        self.instances.pop(abstract, None)

    def forgetInstances(self):
        """
        Clear all of the instances from the container.
        """

        self.instances = {}

    def flush(self):
        """
        Flush the container of all bindings and resolved instances.
        """

        self.aliases = {}
        self.resolved = {}
        self.bindings = {}
        self.instances = {}
        self.abstractAliases = {}


# app = ContainerIOC()
