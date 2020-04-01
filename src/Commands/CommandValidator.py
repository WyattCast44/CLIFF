import string
import inspect
from src.Support import Str


class CommandValidator:

    @staticmethod
    def validate(signature: str, handler):

        if not CommandValidator.validateSignature(signature):

            print("\nTODO raise command signature validation error")

            return False

        if not CommandValidator.validateHandlerAcceptsApplication(handler):

            print("\nTODO raise option parameter validation error")

            return False

        return True

    @staticmethod
    def validateSignature(signature: str):

        if "|" in signature:

            signatures = signature.split('|')

            for part in signatures:

                part = part.strip()

                valid = CommandValidator.validateSingleSignature(part)

                if not valid:

                    return False

            return True

        elif "," in signature:

            signatures = signature.split(',')

            for part in signatures:

                part = part.strip()

                valid = CommandValidator.validateSingleSignature(part)

                if not valid:

                    return False

            return True

        else:

            # Only one signature, validate it

            return CommandValidator.validateSingleSignature(signature)

    def validateSingleSignature(signature: str):

        # Command signatures must start
        # with a lowercase alpha letter

        if not signature[0] in string.ascii_lowercase:

            return False

        return True

    def validateHandlerAcceptsApplication(handler):

        # TODO: Determine how to do this

        return True
