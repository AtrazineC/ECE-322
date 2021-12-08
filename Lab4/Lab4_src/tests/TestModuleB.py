import unittest
from unittest.mock import Mock
from unittest.mock import mock_open
from unittest.mock import patch

from modules.ModuleB import ModuleB


class TestModuleB(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()
        self.modB = ModuleB(self.modF)

    @patch("builtins.print")
    @patch("builtins.open")
    def test_file_not_found_error(self, mock_file, mock_print):
        error = IOError()
        error.filename = "file_name.txt"
        mock_file.side_effect = error
        self.modB.loadFile("this_file_does_not_exist.txt")
        mock_print.assert_called_once_with("FileNotFoundError")

    @patch("builtins.print")
    @patch("builtins.open")
    def test_io_error(self, mock_file, mock_print):
        error = IOError()
        error.filename = "file_name.txt"
        mock_file.side_effect = error
        data = self.modB.loadFile("file_name.txt")
        mock_file.assert_called_once_with("file_name.txt")
        self.modF.displayData.assert_called_once_with(data)
        mock_print.assert_called_once_with("Could not read file:file_name.txt")

    @patch("builtins.open", new_callable=mock_open, read_data="x, d\nq, a\nthis, should, error\np, o\nerr\n")
    def test_load_file(self, mock_file):
        data = self.modB.loadFile("file_name.txt")
        self.assertEqual(3, len(data))
        mock_file.assert_called_once_with("file_name.txt")
        self.modF.displayData.assert_called_once_with(data)
        mock_file().__exit__.assert_called()

    def test_get_f(self):
        self.modB._f = "yeet"
        self.assertEqual(self.modB.f, "yeet")

    def test_set_f(self):
        self.modB.f = "yeet2"
        self.assertEqual(self.modB._f, "yeet2")


if __name__ == "__main__":
    unittest.main()
