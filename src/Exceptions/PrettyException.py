import colored
import traceback
from colored import stylize


class PrettyException:

    def __init__(self, config={}):

        self.config = config

    def setName(self, name: str):

        self.name = stylize(name, colored.fg('red'))

        return self

    def setProblem(self, problem: str):

        self.problem = f"\nProblem:\n   {problem}"

        return self

    def setGiven(self, given):

        self.given = f"\nGiven:\n   {given}"

        return self

    def build(self):

        message = f"\n{stylize('ERROR', colored.bg('red'))} {self.name}\n"
        message = message + self.problem + self.given

        self.message = message

        return self

    def print(self):

        print(self.message)

        return
