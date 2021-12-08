import unittest
from unittest.mock import call
from unittest.mock import patch

from data.Entry import Entry
from modules.ModuleD import ModuleD
from modules.ModuleF import ModuleF
from modules.ModuleG import ModuleG


class TestModuleDFG(unittest.TestCase):
    def setUp(self):
        self.modF = ModuleF()
        self.modG = ModuleG()
        self.modD = ModuleD(self.modF, self.modG)

    @patch("builtins.open", side_effect=FileNotFoundError())
    @patch("builtins.print")
    def test_insert_data(self, mock_print, mock_file):
        test = [Entry("curry", "C"), Entry("desert", "D"), Entry("alpha", "A"), Entry("ben", "B")]

        # Insert test data
        data = self.modD.insertData(test, "E", "5", "test_file.txt")

        # Check length of array increased
        self.assertEqual(len(data), 5)

        # Check the file was written to
        mock_file.assert_called_once_with("test_file.txt", "w")

        # Check the correct stuff was printed
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 curry, C"),
            call("2 desert, D"),
            call("3 alpha, A"),
            call("4 ben, B"),
            call("5 E, 5"),
            call("----------------------------------------------------------")
        ])

    @patch("builtins.open", side_effect=FileNotFoundError())
    @patch("builtins.print")
    def test_update_data(self, mock_print, mock_file):
        test = [Entry("curry", "C"), Entry("desert", "D"), Entry("alpha", "A"), Entry("ben", "B")]
        expected = [("curry", "C"), ("changed", "changed2"), ("alpha", "A"), ("ben", "B")]

        # Modify data at position 2
        # ERROR: we want it to update desert (since it is listed as item 2) but it updates ben
        actual = self.modD.updateData(test, 2, "changed", "changed2", "test_file.txt")

        # Check length
        self.assertEqual(len(actual), 4)

        # Check each element
        for i in range(len(test)):
            expected_element = expected[i]
            actual_element = actual[i]
            self.assertEqual(actual_element.name, expected_element[0])
            self.assertEqual(actual_element.number, expected_element[1])

        # Check the file was written to
        mock_file.assert_called_once_with("test_file.txt", "w")

        # Check the correct stuff was printed
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 curry, C"),
            call("2 changed, changed2"),
            call("3 alpha, A"),
            call("4 ben, B"),
            call("----------------------------------------------------------")
        ])

    @patch("builtins.open", side_effect=FileNotFoundError())
    @patch("builtins.print")
    def test_delete_data(self, mock_print, mock_file):
        test = [Entry("curry", "C"), Entry("desert", "D"), Entry("alpha", "A"), Entry("ben", "B")]
        expected = [("desert", "D"), ("alpha", "A"), ("ben", "B")]

        # Delete data at position 1
        # ERROR: we want it to delete curry (since it is listed as item 1) but it actually deletes desert (item 2)
        actual = self.modD.deleteData(test, 1, "test_file.txt")

        # Check length
        self.assertEqual(len(actual), 3)

        # Check each element
        for i in range(len(actual)):
            expected_element = expected[i]
            actual_element = actual[i]
            self.assertEqual(actual_element.name, expected_element[0])
            self.assertEqual(actual_element.number, expected_element[1])

        # Check the file was written to
        mock_file.assert_called_once_with("test_file.txt", "w")

        # Check the correct stuff was printed
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 desert, D"),
            call("2 alpha, A"),
            call("3 ben, B"),
            call("----------------------------------------------------------")
        ])

    def test_getters(self):
        self.modD._f = "Get f"
        self.assertEqual(self.modD.f, "Get f")

        self.modD._g = "Get g"
        self.assertEqual(self.modD.g, "Get g")

    def test_setters(self):
        self.modD.f = "Set f"
        self.assertEqual(self.modD._f, "Set f")

        self.modD.g = "Set g"
        self.assertEqual(self.modD._g, "Set g")


if __name__ == '__main__':
    unittest.main()
