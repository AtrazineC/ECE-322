import unittest
from unittest.mock import Mock

from data.Entry import Entry
from modules.ModuleC import ModuleC


class TestModuleC(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()
        self.modC = ModuleC(self.modF)

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

    def test_get_f(self):
        self.modC._f = "yeet C"
        self.assertEqual(self.modC.f, "yeet C")

    def test_set_f(self):
        self.modC.f = "yeet C"
        self.assertEqual(self.modC._f, "yeet C")


if __name__ == "__main__":
    unittest.main()
