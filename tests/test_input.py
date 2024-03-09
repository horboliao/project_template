import unittest
import pandas as pd
from unittest.mock import patch
from app.io.input import read_text_from_file, read_text_from_file_with_pandas
import os


class TestInputFunctions(unittest.TestCase):
    def setUp(self):
        self.temp_file_path = "temp.txt"
        with open(self.temp_file_path, "w") as temp_file:
            temp_file.write("Test content")

    def tearDown(self):
        os.remove(self.temp_file_path)

    def test_read_text_from_file(self):
        expected_text = "Test content"
        actual_text = read_text_from_file(self.temp_file_path)
        self.assertEqual(expected_text, actual_text)

    def test_read_text_from_file_with_pandas(self):
        mock_data = pd.DataFrame({
            'column1': [1, 2, 3],
            'column2': ['a', 'b', 'c']
        })

        with patch("pandas.read_csv") as mock_read_csv:
            mock_read_csv.return_value = mock_data
            expected_text = mock_data.to_string(index=False, header=False)
            actual_text = read_text_from_file_with_pandas("test.csv")
            self.assertEqual(expected_text, actual_text)


if __name__ == "__main__":
    unittest.main()
