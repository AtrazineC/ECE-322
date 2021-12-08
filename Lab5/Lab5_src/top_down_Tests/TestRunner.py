import unittest

import TestModuleA
import TestModuleABCDE
import TestModuleABCDEFG

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Layer 1
suite.addTests(loader.loadTestsFromModule(TestModuleA))

# Layer 2
suite.addTests(loader.loadTestsFromModule(TestModuleABCDE))

# Layer 3
suite.addTests(loader.loadTestsFromModule(TestModuleABCDEFG))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
