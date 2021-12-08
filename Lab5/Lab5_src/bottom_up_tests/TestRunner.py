import unittest

import TestModuleF
import TestModuleG
import TestModuleDFG
import TestModuleBF
import TestModuleCF
import TestModuleE
import TestModuleABCDEFG

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Layer 3
suite.addTests(loader.loadTestsFromModule(TestModuleF))
suite.addTests(loader.loadTestsFromModule(TestModuleG))

# Layer 2
suite.addTests(loader.loadTestsFromModule(TestModuleDFG))
suite.addTests(loader.loadTestsFromModule(TestModuleBF))
suite.addTests(loader.loadTestsFromModule(TestModuleCF))
suite.addTests(loader.loadTestsFromModule(TestModuleE))

# Layer 1
suite.addTests(loader.loadTestsFromModule(TestModuleABCDEFG))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
