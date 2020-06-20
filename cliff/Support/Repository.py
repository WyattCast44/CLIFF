class Repository:

    def __init__(self, items={}) -> None:
        self.store = items

    def items(self) -> dict:
        ''''Get the dict of items'''
        return self.store

    def has(self, key) -> bool:
        '''Determine if the given configuration value exists'''
        return key in self.store

    def get(self, key, defaultValue=None):
        '''Get the specified configuration value'''
        return self.store.get(key, defaultValue)

    def set(self, key, value) -> None:
        '''Set the specified configuration value'''
        self.store[key] = value

    def merge(self, items: dict) -> None:
        '''Merge the given items into the store'''
        self.store.update(items)

# class Collection:

#     def __init__(self, items={}):
#         self.store = items

#     def all(self):
#         return self.store

#     def get(self, key):

#         keystack = []

#         for part in key.split("."):

#             keystack.append(part)

#         transient = (None, self.store)

#         for key in keystack:

#             transient = (key, transient[1][key])

#         return transient[1]

#     def set(self, key, value):

#         def singleSet(key, value):

#             self.store[key] = value

#         def nestedSet(key, value):

#             struct = {}

#             keystack = key.split(".")

#             keystack.reverse()

#             struct[keystack[0]] = value

#             for key in keystack[1:-1]:

#                 new = {key: struct}

#                 struct = new

#             self.store[keystack[-1]] = struct

#         if not "." in key:

#             return singleSet(key, value)

#         else:

#             return nestedSet(key, value)


# c = Collection({
#     'name': 'wyatt',
# })

# # c.set('names.age.int', 1)
# c.set('names.test', {
#     'key': 'value'
# })

# print(c.all())
# quit()

# print(c.get('names.age.int'))
