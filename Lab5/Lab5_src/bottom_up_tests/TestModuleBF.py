import unittest
from unittest.mock import mock_open
from unittest.mock import patch
from unittest.mock import call

from modules.ModuleB import ModuleB
from modules.ModuleF import ModuleF


class TestModuleBF(unittest.TestCase):
    def setUp(self):
        self.modF = ModuleF()
        self.modB = ModuleB(self.modF)

    @patch("builtins.print")
    @patch("builtins.open")
    def test_file_not_found_error(self, mock_file, mock_print):
        error = IOError()
        error.filename = "file_name.txt"
        mock_file.side_effect = error
        self.modB.loadFile("this_file_does_not_exist.txt")

        # Check the proper print statements have been made
        # This fails because FileNotFoundError branch is unreachable
        mock_print.assert_has_calls([
            call("FileNotFoundError"),
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("----------------------------------------------------------")
        ])

    @patch("builtins.print")
    @patch("builtins.open")
    def test_io_error(self, mock_file, mock_print):
        error = IOError()
        error.filename = "file_name.txt"
        mock_file.side_effect = error
        self.modB.loadFile("file_name.txt")

        # Check the proper print statements have been made
        mock_print.assert_has_calls([
            call("Could not read file:file_name.txt"),
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("----------------------------------------------------------")
        ])
        mock_file.assert_called_once_with("file_name.txt")

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open, read_data="x,d\nq,a\nthis,should,error\np,o\nerr\n")
    def test_load_file(self, mock_file, mock_print):
        data = self.modB.loadFile("file_name.txt")
        self.assertEqual(3, len(data))
        mock_file.assert_called_once_with("file_name.txt")

        # Check the proper print statements have been made
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 x, d"),
            call("2 q, a"),
            call("3 p, o"),
            call("----------------------------------------------------------")
        ])

        mock_file().__exit__.assert_called()

    def test_get_f(self):
        self.modB._f = "yeet"
        self.assertEqual(self.modB.f, "yeet")

    def test_set_f(self):
        self.modB.f = "yeet2"
        self.assertEqual(self.modB._f, "yeet2")


if __name__ == '__main__':
    unittest.main()
