import inspect
from src.Support import Str
from src.Exceptions import OptionSignatureValidationError
from src import Application
import functools


class OptionValidator:

    @staticmethod
    def validate(application: Application, signature: str, handler):

        # We need to check if we need to split the signature into
        # parts, either by pipe (|) or by comma (,)
        if "|" in signature:

            signatures = signature.split('|')

        elif "," in signature:

            signatures = signature.split(',')

        else:

            signatures = [signature]

        # We need to strip whitespace off all parts
        signatures = [part.strip() for part in signatures]

        # We need to validate each part and make sure it
        # meets naming requirements
        for part in signatures:

            OptionValidator.__validateSignature(part)

        # We need to check if any part of signature has
        # already been registered and if we are in strict mode
        # TODO This is not working because options has the actual
        # string orginally passed, not the formatted, split version
        if application.config["strict_registration"]:

            for part in signatures:

                if part in application.options:

                    print("\nTODO raise duplicate signature error")

                    return False

        # If we made it here, we know all parts of the signature
        # are valid :)
        return True

    @staticmethod
    def __validateSignature(signature: str):

        # Options signatures must start
        # with either a single or double hypen

        if Str.startsWith(signature, '-'):

            return True

        if Str.startsWith(signature, '--'):

            return True

        # If we get here we know the signature
        # is invalid, raise exception
        OptionSignatureValidationError(
            signature)

        exit()

        return False
