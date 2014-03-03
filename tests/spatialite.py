import unittest

from .base import BaseTest

from libfeatureserver import datasource, exception, configuration

class SpatiaLiteTestCase(BaseTest):
    
    def setUp(self):
        self.config = configuration.SpatiaLite(file = "./tests/data/test-0.1.sqlite")
        self.datasource = datasource.SpatiaLite(self.config)
    
    def tearDown(self):
        self.datasource.close()
        self.datasource = None
    
    def test_connection(self):
        with self.assertRaises(exception.DatabaseConnectionFailed):
            self.datasource.config.file = "./tests/data/dummy.sqlite"
            self.datasource.connect()
        
        self.datasource.config.file = "./tests/data/test-0.1.sqlite"
        try:
            self.datasource.connect()
            self.datasource.close()
        except:
            self.fail("couldn't not find {file}".format(file = self.datasource.file))

def test_suite():
    return unittest.TestLoader().loadTestsFromTestCase(SpatiaLiteTestCase)

