class Basic(object):
    
    @property
    def config(self):
        return self._config
    
    @property
    def connection(self):
        return self._connection
    
    def __init__(self, config, *args, **kwargs):
        self._config = config


from datasources import spatialite

SpatiaLite = spatialite.SpatiaLite

