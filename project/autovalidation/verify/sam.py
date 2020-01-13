class Oho:
    def __init__(self, h, value, on, mode):
        self.__h = h
        self.value = value
        self.__on = on
        self.__mode = mode

    @property
    def h(self):
        return self.h

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self,value):
        self.value = value

    @property
    def on(self):
        return self.on

    @property
    def mode(self):
        return self.mode


class Url:
    def __init__(self, m):
        self.m = m

    @property
    def m(self):
        return self.m

    @m.setter
    def m(self, m):
        self.m = m
