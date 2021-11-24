import unittest
from unittest.mock import Mock
from unittest.mock import mock_open
from unittest.mock import patch

from modules.ModuleB import ModuleB


class TestModuleB(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()
        self.modB = ModuleB(self.modF)

    @patch('builtins.open', new_callable=mock_open,
           read_data="one, 1\n"
                     "two, 2\n"
                     "too, many, 2\n"
                     "three, 3\n"
                     "four\n"
                     "five, 5\n"
           )
    def test_load_file(self, mock_file):
        data = self.modB.loadFile('fileName.txt')
        self.assertEqual(4, len(data))
        mock_file.assert_called_once_with('fileName.txt')
        self.modF.displayData.assert_called_once_with(data)
        mock_file().__exit__.assert_called()

    def test_fgetter(self):
        self.modB._f = "Hello"
        self.assertEqual(self.modB.f, "Hello")

    def test_fsetter(self):
        self.modB.f = "Hello"
        self.assertEqual(self.modB._f, "Hello")

    @patch('builtins.print')
    @patch('builtins.open')
    def test_io_error(self, mock_file, mock_print):
        error = IOError()
        error.filename = 'fileName.txt'
        mock_file.side_effect = error
        data = self.modB.loadFile('fileName.txt')
        mock_file.assert_called_once_with('fileName.txt')
        self.modF.displayData.assert_called_once_with(data)
        mock_print.assert_called_once_with("Could not read file:fileName.txt")

    @patch('builtins.print')
    @patch('builtins.open')
    def test_file_not_found_error(self, mock_file, mock_print):
        error = IOError()
        error.filename = 'fileName.txt'
        mock_file.side_effect = error
        data = self.modB.loadFile('file.txt')
        mock_print.assert_called_once_with("FileNotFoundError")


if __name__ == '__main__':
    unittest.main()
