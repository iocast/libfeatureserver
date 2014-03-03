from unittest import TestSuite

import wfs, spatialite

def test_suite():
    suite = TestSuite()
    suite.addTest(wfs.test_suite())
    suite.addTest(spatialite.test_suite())
    return suite

if __name__ == "__main__":
    test_suite()
