import unittest
from unittest.mock import Mock
from unittest.mock import call
from unittest.mock import mock_open
from unittest.mock import patch

from modules.ModuleA import ModuleA
from modules.ModuleB import ModuleB
from modules.ModuleC import ModuleC
from modules.ModuleD import ModuleD
from modules.ModuleE import ModuleE
from modules.ModuleF import ModuleF
from modules.ModuleG import ModuleG


class TestModuleA(unittest.TestCase):
    def setUp(self):
        self.modF = ModuleF()
        self.modG = ModuleG()
        self.modB = ModuleB(self.modF)
        self.modC = ModuleC(self.modF)
        self.modD = ModuleD(self.modF, self.modG)
        self.modE = ModuleE()
        self.modA = ModuleA(self.modB, self.modC, self.modD, self.modE)
        self.modA._data = ["Bill", "John"]

    def test_get_data(self):
        self.modA._data = "b"
        self.assertEqual(self.modA.data, "b")

    def test_set_data(self):
        self.modA.data = "test_data_setter"
        self.assertEqual(self.modA._f, "test_data_setter")

    @patch("builtins.print")
    def test_display_help(self, print_mock):
        self.assertEqual(self.modA.displayHelp(), True)
        print_mock.assert_called_once_with(
            "Available Commands: \n"
            "load <filepath>\n"
            "add <name> <number>\n"
            "update <index> <name> <number>\n"
            "delete <index>\n"
            "sort\n"
            "exit")

    @patch("builtins.print")
    def test_empty_command(self, mock_print):
        self.modA.run()
        mock_print.assert_called_with("No command passed!")

    @patch("builtins.print")
    def test_invalid_command(self, mock_print):
        self.modA.run("yeeeeet this is an invalid command")
        mock_print.assert_called_with("Unknown command, type 'help' for command list.")

    @patch("builtins.print")
    def test_help(self, mock_print):
        self.modA.run("help")
        mock_print.assert_called_with("Available Commands: \n"
                                      + "load <filepath>\n"
                                      + "add <name> <number>\n"
                                      + "update <index> <name> <number>\n"
                                      + "delete <index>\n"
                                      + "sort\n"
                                      + "exit")

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open, read_data="alpha,a\nbeta,b\ngamma,g\nyeet,y\n")
    def test_load(self, mock_file, mock_print):
        self.modA.run("load", "file_name.txt")
        mock_file.assert_called_once_with("file_name.txt")
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 alpha, a"),
            call("2 beta, b"),
            call("3 gamma, g"),
            call("4 yeet, y"),
            call("----------------------------------------------------------")
        ])

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open, read_data="alpha,a\nbeta,b\ngamma,g\nyeet,y\n")
    def test_update(self, mock_file, mock_print):
        self.modA.run("load", "file_name.txt")
        mock_file.assert_called_once_with("file_name.txt")
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 alpha, a"),
            call("2 beta, b"),
            call("3 gamma, g"),
            call("4 yeet, y"),
            call("----------------------------------------------------------")
        ])
        self.modA.run("update", 1, "John", "john-test")
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 John, john-test"),
            call("2 beta, b"),
            call("3 gamma, g"),
            call("4 yeet, y"),
            call("----------------------------------------------------------")
        ])

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open, read_data="alpha,a\nbeta,b\ngamma,g\nyeet,y\n")
    def test_add(self, mock_file, mock_print):
        self.modA.run("load", "file_name.txt")
        mock_file.assert_called_once_with("file_name.txt")
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 alpha, a"),
            call("2 beta, b"),
            call("3 gamma, g"),
            call("4 yeet, y"),
            call("----------------------------------------------------------")
        ])
        self.modA.run("add", "John", "john-test")
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 alpha, a"),
            call("2 beta, b"),
            call("3 gamma, g"),
            call("4 yeet, y"),
            call("5 John, john-test"),
            call("----------------------------------------------------------")
        ])

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open, read_data="alpha,a\nbeta,b\ngamma,g\nyeet,y\n")
    def test_delete(self, mock_file, mock_print):
        self.modA.run("load", "file_name.txt")
        mock_file.assert_called_once_with("file_name.txt")
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 alpha, a"),
            call("2 beta, b"),
            call("3 gamma, g"),
            call("4 yeet, y"),
            call("----------------------------------------------------------")
        ])
        self.modA.run("delete", 1)
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 beta, b"),
            call("2 gamma, g"),
            call("3 yeet, y"),
            call("----------------------------------------------------------")
        ])

    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open, read_data="gamma,g\nbeta,b\nalpha,a\nyeet,y\n")
    def test_sort(self, mock_file, mock_print):
        self.modA.run("load", "file_name.txt")
        mock_file.assert_called_once_with("file_name.txt")
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 gamma, g"),
            call("2 beta, b"),
            call("3 alpha, a"),
            call("4 yeet, y"),
            call("----------------------------------------------------------")
        ])
        self.modA.run("sort")
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 alpha, a"),
            call("2 beta, b"),
            call("3 gamma, g"),
            call("4 yeet, y"),
            call("----------------------------------------------------------")
        ])

    def test_exit(self):
        with self.assertRaises(SystemExit) as cm:
            self.modA.run("exit")
            self.assertEqual(cm.exception.code, 1)

    @patch("builtins.print")
    def test_commands_index_error(self, mock_print):
        self.modA.displayHelp = Mock()
        self.modA.parseLoad = Mock()
        self.modA.parseAdd = Mock()
        self.modA.runSort = Mock()
        self.modA.parseUpdate = Mock()
        self.modA.parseDelete = Mock()
        self.modA.runExit = Mock()

        self.modA.run("load")
        mock_print.assert_called_with("Malformed command!")
        self.modA.run("add")
        mock_print.assert_called_with("Malformed command!")
        self.modA.run("delete")
        mock_print.assert_called_with("Malformed command!")
        self.modA.run("update")
        mock_print.assert_called_with("Malformed command!")

    @patch("builtins.print")
    def test_commands_no_file(self, mock_print):
        self.modA.displayHelp = Mock()
        self.modA.parseLoad = Mock()
        self.modA.parseAdd = Mock()
        self.modA.runSort = Mock()
        self.modA.parseUpdate = Mock()
        self.modA.parseDelete = Mock()
        self.modA.runExit = Mock()

        self.modA._data = None

        self.modA.run("add", "John", "1")
        mock_print.assert_called_with("No file loaded!")
        self.modA.run("delete", 1)
        mock_print.assert_called_with("No file loaded!")
        self.modA.run("sort")
        mock_print.assert_called_with("No file loaded!")
        self.modA.run("update", 1, "John", "1")
        mock_print.assert_called_with("No file loaded!")


if __name__ == "__main__":
    unittest.main()
