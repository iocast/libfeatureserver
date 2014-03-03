

class BaseException(Exception):
    @property
    def locator(self):
        return self._locator
    
    def __init__(self, message, locator=None, **kwargs):
        super(BaseException, self).__init__(message)
        self._locator = locator


class VersionNotSupported(BaseException):
    _message = "Version {version} not supported"
    
    def __init__(self, version, locator=None, **kwargs):
        super(VersionNotSupported, self).__init__(self._message.format(version = version), locator)


class DatabaseConnectionFailed(BaseException):
    _message = "Unable to connect to {connection}"
    
    def __init__(self, connection, locator=None, **kwargs):
        super(DatabaseConnectionFailed, self).__init__(self._message.format(connection = connection), locator)

