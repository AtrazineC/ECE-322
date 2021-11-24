import unittest
from unittest.mock import Mock
from unittest.mock import call
from unittest.mock import patch

from modules.ModuleF import ModuleF


class TestModuleF(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()
        self.modF = ModuleF()

    @patch('builtins.print')
    def test_display_data(self, mock_print):
        data = [
            'one',
            'two',
            'three'
        ]
        self.modF.displayData(data)
        calls = [
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 one"),
            call("2 two"),
            call("3 three"),
            call("----------------------------------------------------------")
        ]
        mock_print.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
