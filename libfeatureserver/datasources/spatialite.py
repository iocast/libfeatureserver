import os
from libfeatureserver.datasource import Basic
from libfeatureserver import exception

from pyspatialite import dbapi2 as spatialite


class SpatiaLite(Basic):
    
    def __init__(self, config, *args, **kwargs):
        super(SpatiaLite, self).__init__(config, *args, **kwargs)
    
    def connect(self):
        if not os.path.isfile(self.config.file):
            raise exception.DatabaseConnectionFailed(connection = self.config.file, locator = self.__class__.__name__)
        
        self._connection = spatialite.connect(self.config.file)
    
    def close(self):
        if self.connection:
            self.connection.close()
    
    def commit(self):
        if self.connection:
            self.connection.commit()

