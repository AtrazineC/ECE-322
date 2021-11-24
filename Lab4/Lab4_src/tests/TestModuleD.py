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
        data = [
            ('A', '1'),
            ('B', '2'),
            ('C', '3'),
            ('D', '4'),
        ]

        result = self.modD.insertData(data, 'E', '5', 'fileName.txt')
        self.assertEqual(len(result), 5)
        self.modF.displayData.assert_called_once_with(data=data)
        self.modG.updateData.assert_called_once_with('fileName.txt', data)

    def test_update_data(self):
        data = [
            Entry('A', '1'),
            Entry('B', '2'),
            Entry('C', '3'),
            Entry('D', '4'),
        ]

        expected = [
            ('A', '1'),
            ('B', '2'),
            ('Z', '22'),
            ('D', '4'),
        ]

        result = self.modD.updateData(data, 2, 'Z', '22', 'fileName.txt')
        self.assertEqual(len(result), 4)
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected[i][0])
            self.assertEqual(result[i].number, expected[i][1])
        self.modF.displayData.assert_called_once_with(result)
        self.modG.updateData.assert_called_once_with('fileName.txt', result)

    def test_delete_data(self):
        data = [
            Entry('A', '1'),
            Entry('B', '2'),
            Entry('C', '3'),
            Entry('D', '4'),
        ]

        expected = [
            ('A', '1'),
            ('B', '2'),
            ('D', '4'),
        ]

        result = self.modD.deleteData(data, 2, 'fileName.txt')
        self.assertEqual(len(result), 3)
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected[i][0])
            self.assertEqual(result[i].number, expected[i][1])
        self.modF.displayData.assert_called_once_with(result)
        self.modG.updateData.assert_called_once_with('fileName.txt', result)

    def test_f_getter(self):
        self.modD._f = "Hello"
        self.assertEqual(self.modD.f, "Hello")

    def test_f_setter(self):
        self.modD.f = "Hello"
        self.assertEqual(self.modD._f, "Hello")

    def test_g_getter(self):
        self.modD._g = "Hello"
        self.assertEqual(self.modD.g, "Hello")

    def test_g_setter(self):
        self.modD.g = "Hello"
        self.assertEqual(self.modD._g, "Hello")


if __name__ == '__main__':
    unittest.main()
