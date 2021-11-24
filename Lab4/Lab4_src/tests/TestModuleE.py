import unittest

from modules.ModuleE import ModuleE


class TestModuleE(unittest.TestCase):
    def setUp(self):
        self.modE = ModuleE()

    def test_exit(self):
        with self.assertRaises(SystemExit) as cm:
            self.modE.exitProgram()
            self.assertEqual(cm.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
