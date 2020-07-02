
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
