import unittest

from modules.ModuleE import ModuleE


class TestModuleE(unittest.TestCase):
    def setUp(self):
        self.modE = ModuleE()

    def test_run_exit(self):
        with self.assertRaises(SystemExit) as e:
            self.modE.exitProgram()
            self.assertEqual(e.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
