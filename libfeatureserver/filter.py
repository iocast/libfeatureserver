class WFS(object):
    
    @property
    def raw(self):
        return self._raw
    
    @property
    def fsom(self):
        """ FeatureServer Object Model """
        return self._fsom
    
    def __init__(self, *args, **kwargs): pass

    def parse(raw):
        self._raw = raw

    