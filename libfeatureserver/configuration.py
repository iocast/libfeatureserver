

class Basic(object):

    def __init__(self, *args, **kwargs):
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])


class SpatiaLite(Basic):
    
    @property
    def file(self):
        return self._file
    @file.setter
    def file(self, value):
        self._file = value

    