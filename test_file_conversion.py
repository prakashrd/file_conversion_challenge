import unittest
from file_conversion import *


class TestFileConversion(unittest.TestCase):

    def test_parse_row(self):
        row = 'testDataFooBar'
        offsets = [4, 4, 3, 3]
        expected = ['test', 'Data', 'Foo', 'Bar']
        self.assertEqual(expected, parse_row(row, offsets))

    def test_parse_row_with_empty_values(self):
        row = 'test Data   123'
        offsets = [4, 5, 6]
        expected = ['test', 'Data', '123']
        self.assertEqual(expected, parse_row(row, offsets))

    def test_parse_spec_data(self):
        specs_file = './test_data/spec.json'
        expected = (
            ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10'],
            ['5', '12', '3', '2', '13', '7', '10', '13', '20', '13'],
            'windows-1252',
            'True',
            'utf-8'
        )
        self.assertEqual(expected, parse_for_specs(specs_file))

    def test_parse_and_generate_output(self):
        output = './test_output/delimited_output.csv'
        parse_and_generate_output(
            './test_data/spec_test.json',
            './test_data/fixed_width.dat',
            output
        )

        with open(output, 'r', encoding='utf-8') as csv_file:
            lines = csv_file.readlines()
            self.assertEqual(4, len(lines))
            self.assertEqual('f1;f2;f3', lines[0].strip())
            self.assertEqual('£row;11Seven;77 3', lines[1].strip())
            self.assertEqual('£row;21Seven;77 3', lines[2].strip())
            self.assertEqual('£row;31Seven;77 3', lines[3].strip())

    def test_invalid_encoding_exception(self):
        self.assertRaises(LookupError, lambda: parse_and_generate_output(
            './test_data/spec_invalid_encoding_test.json',
            './test_data/fixed_width.dat',
            './test_output/delimited_output.csv')
        )

    def test_parse_spec_data_for_exception(self):
        # assert Raises takes a callback function
        self.assertRaises(KeyError, lambda: parse_for_specs('./test_data/spec_exception.json'))


if __name__ == '__main__':
    unittest.main()