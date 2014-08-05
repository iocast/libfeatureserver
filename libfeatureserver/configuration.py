

class Basic(object):
    
    @property
    def feature_id(self):
        return self._feature_id
    @feature_id.setter
    def feature_id(self, value):
        self._feature_id = value
    
    @property
    def layer(self):
        return self._layer
    @property.setter
    def layer(self, value):
        self._layer = layer
    
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

    