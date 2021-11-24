import unittest
from unittest.mock import Mock

from data.Entry import Entry
from modules.ModuleC import ModuleC


class TestModuleC(unittest.TestCase):
    def setUp(self):
        self.modF = Mock()
        self.modC = ModuleC(self.modF)

    def test_sort_data(self):
        data = [
            Entry('C', '3'),
            Entry('D', '4'),
            Entry('A', '1'),
            Entry('B', '2'),
        ]
        expected = [
            ('A', '1'),
            ('B', '2'),
            ('C', '3'),
            ('D', '4'),
        ]
        result = self.modC.sortData(data)
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected[i][0])
            self.assertEqual(result[i].number, expected[i][1])
        self.modF.displayData.assert_called_once_with(result)

    def test_f_getter(self):
        self.modC._f = "Hello"
        self.assertEqual(self.modC.f, "Hello")

    def test_f_setter(self):
        self.modC.f = "Hello"
        self.assertEqual(self.modC._f, "Hello")


if __name__ == '__main__':
    unittest.main()
