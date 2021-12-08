import unittest
from unittest.mock import mock_open, call
from unittest.mock import patch

from data.Entry import Entry
from modules.ModuleG import ModuleG


class TestModuleG(unittest.TestCase):
    def setUp(self):
        self.modG = ModuleG()

    @patch("builtins.open", new_callable=mock_open)
    def test_data_update(self, mock_file):
        data = [Entry("ece", "322"), Entry("ece", "321")]
        calls = [call("ece,322\n"), call("ece,321\n")]

        self.modG.updateData("test_file.txt", data)
        mock_file.assert_called_once_with("test_file.txt", "w")
        file = mock_file()

        self.assertEqual(file.write.call_count, 2)
        file.write.assert_has_calls(calls)
        file.__exit__.assert_called()

    @patch("builtins.open", side_effect=FileNotFoundError())
    @patch("builtins.print")
    def test_data_update_file_error(self, mock_print, mock_file):
        data = [Entry("ece", "322"), Entry("ece", "321")]
        self.modG.updateData("test_file.txt", data)
        mock_file.assert_called_once_with("test_file.txt", "w")
        mock_print.assert_called_with("Error updating DB File.")


if __name__ == '__main__':
    unittest.main()
