import inspect
from src.Support import Str
from src.Exceptions import OptionSignatureValidationError


class OptionValidator:

    @staticmethod
    def validate(signature: str, handler):

        if not OptionValidator.validateSignature(signature):

            OptionSignatureValidationError(
                signature).print()

            return False

        if not OptionValidator.validateHandlerAcceptsApplication(handler):

            print("\nTODO raise option parameter validation error")

            return False

        return True

    @staticmethod
    def validateSignature(signature: str):

        if "|" in signature:

            # We need to split the signature
            # and validate each one

            signatures = signature.split('|')

            for part in signatures:

                part = part.strip()

                valid = OptionValidator.validateSingleSignature(part)

                if not valid:

                    return False

            return True

        elif "," in signature:

            signatures = signature.split(',')

            for part in signatures:

                part = part.strip()

                valid = OptionValidator.validateSingleSignature(part)

                if not valid:

                    return False

            return True

        else:

            # Only one signature, validate it

            return OptionValidator.validateSingleSignature(signature)

    def validateSingleSignature(signature: str):

        # Options signatures must start
        # with either a single or double hypen

        if Str.startsWith(signature, '-'):

            return True

        if Str.startsWith(signature, '--'):

            return True

        return False

    def validateHandlerAcceptsApplication(handler):

        # TODO: Determine how to do this

        return True
