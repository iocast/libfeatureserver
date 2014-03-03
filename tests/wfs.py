import unittest

from .base import BaseTest

from libfeatureserver import request
from libfeatureserver import exception

class WFSTestCase(BaseTest):
    
    def setUp(self):
        self.request = request.WFS()
    
    def test_version(self):
        with self.assertRaises(exception.VersionNotSupported):
            self.request.version = 'not supported'
        try:
            self.request.version = '2.0.0'
        except:
            self.fail("version not supported")
    
    
def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(WFSTestCase)

