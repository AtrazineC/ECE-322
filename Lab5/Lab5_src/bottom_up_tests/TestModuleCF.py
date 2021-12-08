import unittest
from unittest.mock import patch
from unittest.mock import call

from data.Entry import Entry
from modules.ModuleC import ModuleC
from modules.ModuleF import ModuleF


class TestModuleCF(unittest.TestCase):
    def setUp(self):
        self.modF = ModuleF()
        self.modC = ModuleC(self.modF)

    @patch("builtins.print")
    def test_sort_data(self, mock_print):
        test = [Entry("curry", "C"), Entry("desert", "D"), Entry("alpha", "A"), Entry("ben", "B")]
        expected = [("alpha", "A"), ("ben", "B"), ("curry", "C"), ("desert", "D")]

        # Sort the data
        actual = self.modC.sortData(test)

        # See if data was sorted correctly
        for i in range(len(test)):
            expected_element = expected[i]
            actual_element = actual[i]
            self.assertEqual(actual_element.name, expected_element[0])
            self.assertEqual(actual_element.number, expected_element[1])

        # Check output
        mock_print.assert_has_calls([
            call("Current Data:"),
            call("----------------------------------------------------------"),
            call("1 alpha, A"),
            call("2 ben, B"),
            call("3 curry, C"),
            call("4 desert, D"),
            call("----------------------------------------------------------")
        ])

    def test_get_f(self):
        self.modC._f = "yeet C"
        self.assertEqual(self.modC.f, "yeet C")

    def test_set_f(self):
        self.modC.f = "yeet C"
        self.assertEqual(self.modC._f, "yeet C")


if __name__ == '__main__':
    unittest.main()
