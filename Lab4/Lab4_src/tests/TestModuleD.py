import unittest
from unittest.mock import Mock

from data.Entry import Entry
from modules.ModuleD import ModuleD


class TestModuleD(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()
        self.modG = Mock()
        self.modD = ModuleD(self.modF, self.modG)

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


if __name__ == "__main__":
    unittest.main()
