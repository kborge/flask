class Status(object):
    __attribs = ['active', 'deleted', 'edited']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            for attrib in self.__attribs:
                if attrib is not value:
                    setattr(self, key, value)

    def __active(self):
        for value in self.__attribs:
            yield [value] if value == 'active' else None

    @property
    def default(self):
        return next(self.__active())

    def __inactive(self):
        for value in self.__attribs:
            yield [value] if value == 'deleted' else None

    @property
    def inactive(self):
        return next(self.__inactive())

    @property
    def all(self):
        return self.__attribs
