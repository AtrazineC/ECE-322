import unittest
from unittest.mock import Mock
from unittest.mock import patch

from modules.ModuleA import ModuleA


class TestModuleA(unittest.TestCase):
    def setUp(self):
        self.modB = Mock()
        self.modC = Mock()
        self.modD = Mock()
        self.modE = Mock()

        self.modA = ModuleA(self.modB, self.modC, self.modD, self.modE)
        self.modA._data = ["Jane", "Doe"]

    @patch('builtins.print')
    def test_help(self, print_mock):
        self.assertEqual(self.modA.displayHelp(), True)
        print_mock.assert_called_once_with(
            "Available Commands: \n"
            "load <filepath>\n"
            "add <name> <number>\n"
            "update <index> <name> <number>\n"
            "delete <index>\n"
            "sort\n"
            "exit"
        )

    def test_parse_delete_without_value(self):
        self.modD.deleteData.return_value = None
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseDelete(1), False)
        self.modD.deleteData.assert_called_once()

    def test_parse_delete_with_value(self):
        self.modD.deleteData.return_value = ["Jane"]
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseDelete(1), True)
        self.modD.deleteData.assert_called_once()

    def test_parse_load_data(self):
        self.modB.loadFile.return_value = ["Jane"]
        self.assertEqual(self.modA.parseLoad("testFilename.txt"), True)
        self.modB.loadFile.assert_called_once()

    def test_parse_load_no_data(self):
        self.modB.loadFile.return_value = None
        self.assertEqual(self.modA.parseLoad("testFilename.txt"), False)
        self.modB.loadFile.assert_called_once()

    def test_parse_add_with_data(self):
        self.modD.insertData.return_value = ["Jane"]
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseAdd("John", "1"), True)
        self.modD.insertData.assert_called_once()

    def test_parse_add_with_no_data(self):
        self.modD.insertData.return_value = None
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseAdd("John", "1"), False)
        self.modD.insertData.assert_called_once()

    def test_run_sort_with_data(self):
        self.modC.sortData.return_value = ["Jane"]
        self.assertEqual(self.modA.runSort(), True)
        self.modC.sortData.assert_called_once()

    def test_run_sort_with_no_data(self):
        self.modC.sortData.return_value = None
        self.assertEqual(self.modA.runSort(), False)
        self.modC.sortData.assert_called_once()

    def test_parse_update_with_data(self):
        self.modD.updateData.return_value = ["Data"]
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseUpdate(1, "John", "1"), True)
        self.modD.updateData.assert_called_once()

    def test_parse_update_with_no_data(self):
        self.modD.updateData.return_value = None
        self.modA._filename = "testFile"
        self.assertEqual(self.modA.parseUpdate(1, "John", "1"), False)
        self.modD.updateData.assert_called_once()

    def test_run_exit(self):
        with self.assertRaises(SystemExit) as cm:
            self.modA.runExit()
            self.assertEqual(cm.exception.code, 1)

    def test_data_getter(self):
        self.modA._data = "John"
        self.assertEqual(self.modA.data, "John")

    def test_data_setter(self):
        self.modA.data = "testdata"
        self.assertEqual(self.modA._f, "testdata")

    @patch('builtins.print')
    def test_unknown_command(self, mock_print):
        self.modA.run("")
        mock_print.assert_called_with("Unknown command, type 'help' for command list.")

    @patch('builtins.print')
    def test_no_command(self, mock_print):
        self.modA.run()
        mock_print.assert_called_with("No command passed!")

    @patch('builtins.print')
    def test_all_commands(self, mock_print):
        self.modA.displayHelp = Mock()
        self.modA.parseLoad = Mock()
        self.modA.parseAdd = Mock()
        self.modA.runSort = Mock()
        self.modA.parseUpdate = Mock()
        self.modA.parseDelete = Mock()
        self.modA.runExit = Mock()

        self.modA.run()
        mock_print.assert_called_with("No command passed!")

        self.modA.run("beep")
        mock_print.assert_called_with("Unknown command, type 'help' for command list.")

        self.modA.run("help")
        self.modA.displayHelp.assert_called_once()

        self.modA.run("load", "testFilename.txt")
        self.modA.parseLoad.assert_called_once()

        self.modA.run("update", 1, "John", "1")
        self.modA.parseUpdate.assert_called_once()

        self.modA.run("add", "John", "1")
        self.modA.parseAdd.assert_called_once()

        self.modA.run("delete", 1)
        self.modA.parseDelete.assert_called_once()

        self.modA.run("sort")
        self.modA.runSort.assert_called_once()

        self.modA.runExit()
        self.modA.runExit.assert_called_once()

    @patch('builtins.print')
    def test_all_commands_no_file(self, mock_print):
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

    @patch('builtins.print')
    def test_all_commands_index_error(self, mock_print):
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


if __name__ == '__main__':
    unittest.main()
