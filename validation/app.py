
import sys

paramList = {
    'name': ['required'],
    '--aim': ['optional'],
}

inputs = sys.argv[1:]

for inn in inputs:

    if "-" in inn or "--" in inn:

        if inn in paramList:
            print(f"map to {inn}")
        else:
            print('print error')

    else:
        pass

print("\n", paramList)

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
