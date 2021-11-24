import unittest
from unittest.mock import mock_open, call
from unittest.mock import patch

from data.Entry import Entry
from modules.ModuleG import ModuleG


class TestModuleE(unittest.TestCase):
    def setUp(self):
        self.modG = ModuleG()

    @patch('builtins.open', new_callable=mock_open)
    def test_update_data(self, mock_file):
        data = [
            Entry('A', '1'),
            Entry('B', '2'),
            Entry('C', '3'),
            Entry('D', '4'),
        ]
        calls = [
            call('A,1\n'),
            call('B,2\n'),
            call('C,3\n'),
            call('D,4\n'),
        ]

        self.modG.updateData('fileName.txt', data)
        mock_file.assert_called_once_with('fileName.txt', 'w')
        file = mock_file()
        self.assertEqual(file.write.call_count, 4)
        file.write.assert_has_calls(calls)
        file.__exit__.assert_called()

    @patch('builtins.open', side_effect=FileNotFoundError())
    @patch('builtins.print')
    def test_update_data_file_not_found(self, mock_print, mock_file):
        data = [
            Entry('A', '1'),
            Entry('B', '2'),
            Entry('C', '3'),
            Entry('D', '4'),
        ]
        self.modG.updateData('fileName.txt', data)
        mock_file.assert_called_once_with('fileName.txt', 'w')
        mock_print.assert_called_with("Error updating DB File.")


if __name__ == '__main__':
    unittest.main()
