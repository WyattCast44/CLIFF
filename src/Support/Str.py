from .Macroable import Macroable


class Str(metaclass=Macroable):

    @staticmethod
    def startsWith(subject, search):
        return (search == subject[0:len(search)])

    @staticmethod
    def after(subject, search):
        """The after method returns everything after the given value in a string. The entire string will be returned if the value does not exist within the string"""

        if search in subject:
            return subject.replace(search, "", 1)
        else:
            return subject

    @staticmethod
    def afterLast(subject, search):
        """The afterLast method returns everything after the last occurrence of the given value in a string. The entire string will be returned if the value does not exist within the string"""

        if search in subject:
            return subject[subject.rfind(search) + len(search):]
        else:
            return subject

    @staticmethod
    def camel(subject, stripUnderscores=True):
        """The camel method converts the given string to CamelCase"""

        return ''.join(letter for letter in subject.replace('_', ' ').title() if not letter.isspace())

    @staticmethod
    def contains(subject, search, caseSensative=False):

        # TODO, fix case sensativity

        if type(search) == list:
            found = False

            for term in search:

                if term in subject:

                    found = True

                    break

            return found

        else:
            return (search in subject)
