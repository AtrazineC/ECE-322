import unittest
from unittest.mock import call
from unittest.mock import patch

from modules.ModuleF import ModuleF


class TestModuleF(unittest.TestCase):
    def setUp(self):
        self.modF = ModuleF()

    @patch("builtins.print")
    def test_display_data(self, mock_print):
        data = ["alpha", "beta", "gamma", "yeet"]
        self.modF.displayData(data)

        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 alpha"),
            call("2 beta"),
            call("3 gamma"),
            call("4 yeet"),
            call("----------------------------------------------------------")
        ])


if __name__ == "__main__":
    unittest.main()
