import unittest
from unittest.mock import Mock
from unittest.mock import mock_open
from unittest.mock import patch

from data.Entry import Entry
from modules.ModuleA import ModuleA
from modules.ModuleB import ModuleB
from modules.ModuleC import ModuleC
from modules.ModuleD import ModuleD
from modules.ModuleE import ModuleE


class TestModuleABCDE(unittest.TestCase):
    def setUp(self):
        # Stub 3rd layer
        self.modF = Mock()
        self.modG = Mock()

        # Test middle layer
        self.modB = ModuleB(self.modF)
        self.modC = ModuleC(self.modF)
        self.modD = ModuleD(self.modF, self.modG)
        self.modE = ModuleE()

        # Top layer
        self.modA = ModuleA(self.modB, self.modC, self.modD, self.modE)
        self.modA._data = ["Bill", "John"]

    def test_getters(self):
        self.modB._f = "yeet"
        self.assertEqual(self.modB.f, "yeet")
        self.modC._f = "yeet C"
        self.assertEqual(self.modC.f, "yeet C")
        self.modD._f = "Get f"
        self.assertEqual(self.modD.f, "Get f")
        self.modD._g = "Get g"
        self.assertEqual(self.modD.g, "Get g")

    def test_setters(self):
        self.modB.f = "yeet2"
        self.assertEqual(self.modB._f, "yeet2")
        self.modC.f = "yeet C"
        self.assertEqual(self.modC._f, "yeet C")
        self.modD.f = "Set f"
        self.assertEqual(self.modD._f, "Set f")
        self.modD.g = "Set g"
        self.assertEqual(self.modD._g, "Set g")

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

    def test_sort_data(self):
        test = [Entry("curry", "C"), Entry("desert", "D"), Entry("alpha", "A"), Entry("ben", "B")]
        expected = [("alpha", "A"), ("ben", "B"), ("curry", "C"), ("desert", "D")]
        actual = self.modC.sortData(test)

        for i in range(len(test)):
            expected_element = expected[i]
            actual_element = actual[i]
            self.assertEqual(actual_element.name, expected_element[0])
            self.assertEqual(actual_element.number, expected_element[1])

        self.modF.displayData.assert_called_once_with(actual)

    def test_insert_data(self):
        test = [Entry("curry", "C"), Entry("desert", "D"), Entry("alpha", "A"), Entry("ben", "B")]
        data = self.modD.insertData(test, "E", "5", "file_test.txt")
        self.assertEqual(len(data), 5)
        self.modF.displayData.assert_called_once_with(data=test)
        self.modG.updateData.assert_called_once_with("file_test.txt", test)

    def test_update_data(self):
        test = [Entry("curry", "C"), Entry("desert", "D"), Entry("alpha", "A"), Entry("ben", "B")]
        expected = [("curry", "C"), ("changed", "changed2"), ("alpha", "A"), ("ben", "B")]
        actual = self.modD.updateData(test, 2, "changed", "changed2", "file_test.txt")
        # we want it to update desert (since it is listed as item 2) but it updates ben

        self.assertEqual(len(actual), 4)

        for i in range(len(test)):
            expected_element = expected[i]
            actual_element = actual[i]
            self.assertEqual(actual_element.name, expected_element[0])
            self.assertEqual(actual_element.number, expected_element[1])

        self.modG.updateData.assert_called_once_with("file_test.txt", actual)
        self.modF.displayData.assert_called_once_with(actual)

    def test_delete_data(self):
        test = [Entry("curry", "C"), Entry("desert", "D"), Entry("alpha", "A"), Entry("ben", "B")]
        expected = [("desert", "D"), ("alpha", "A"), ("ben", "B")]
        actual = self.modD.deleteData(test, 1, "file_test.txt")
        # we want it to delete curry (since it is listed as item 1) but it actually deletes desert (item 2)

        self.assertEqual(len(actual), 3)

        for i in range(len(actual)):
            expected_element = expected[i]
            actual_element = actual[i]
            self.assertEqual(actual_element.name, expected_element[0])
            self.assertEqual(actual_element.number, expected_element[1])

        self.modF.displayData.assert_called_once_with(actual)
        self.modG.updateData.assert_called_once_with("file_test.txt", actual)

    def test_run_exit(self):
        with self.assertRaises(SystemExit) as e:
            self.modE.exitProgram()
            self.assertEqual(e.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
