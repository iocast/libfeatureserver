import exception

class Base(object):
    
    def __init__(self, *args, **kwargs): pass


class WFS(Base):
    
    @property
    def service(self):
        return 'WFS'
    
    @property
    def supported_version(self):
        return ['1.1.0', '2.0.0']
    @property
    def version(self):
        return self._version
    @version.setter
    def version(self, value):
        if value not in self.supported_version:
            raise exception.VersionNotSupported(version = value, locator = self.__class__.__name__)
        self._version = value
    
    def __init__(self, *args, **kwargs):
        super(WFS, self).__init__(*args, **kwargs)

    