
import sys

paramList = {
    'name': ['required'],
    '--aim': ['optional'],
}

inputs = sys.argv[1:]

print("\n", inputs)

quit()


class Validate:

    def __init__(self, values: list, rules: dict):

        self.rules = rules

        self.rawValues = values

        self._validate()

    def _validate(self):

        for key, rules in self.rules.items():

            pass


class IsStr:

    signature = "str"

    def passes(self, attribute, value):

        try:
            return str(value)
        except Exception:
            pass

    def message(self, attribute, value):

        return f"The {attribute} must be castable to a string"


class MaxStr:

    signature = "max:str"

    def passes(self, attribute, value):

    def message(self, attribute, value):

        return f"The {attribute} must be "


params = Validate([
    'Arg1',
    '--Arg2'
    '--Arg3=1'
], {
    'key': ['str', 'required', 'max:40']
})


# this->validate(request, [
#     'name' => ['rules']
# ]);
