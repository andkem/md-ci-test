import sys, unittest
from md import calc_energy

class MockAtoms:
    def get_potential_energy(self):
        return 5;

    def get_kinetic_energy(self):
        return 10;

    def __len__(self):
        return 2;

class MdTests(unittest.TestCase):
    def test_calc_energy(self):
        epot, ekin = calc_energy(MockAtoms())
        self.assertEqual(epot, 2.5)
        self.assertEqual(ekin, 5)

if __name__ == "__main__":
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
