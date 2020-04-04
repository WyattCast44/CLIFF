import colored
from colored import stylize


class StrExtended(str):

    def __init__(self, str: str):

        self.str = str

        return

    def rtn(self):

        return self.__class__(self.str)

    ###
    # Colors
    ###

    def color(self, color: str, layer="fg"):

        if layer == "fg":
            self.str = stylize(self.str, colored.fg(color))
        else:
            self.str = stylize(self.str, colored.bg(color))

        return self.rtn()

    def green(self, layer="fg"):

        return self.color('green', layer)

    def red(self, layer="fg"):

        self.color('red', layer)

        return self.rtn()

    def yellow(self, layer="fg"):

        self.color('yellow', layer)

        return self.rtn()

    def blue(self, layer="fg"):

        self.color('blue', layer)

        return self.rtn()

    ###
    # Styles
    ###

    def style(self, style: str):

        # Reversed doesn't make sense to me, lets just
        # overide it to inverse
        if style == "inverse":
            style = "reverse"

        self.str = stylize(self.str, colored.attr(style))

        return self.rtn()

    def inverse(self):

        self.style('inverse')

        return self.rtn()
