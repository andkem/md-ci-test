import sys
import unittest
import md
import os

class RunTest(unittest.TestCase):
    def test_run(self):
        md.run_md()
        self.assertTrue(os.path.isfile('cu.traj'))

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(RunTest)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
