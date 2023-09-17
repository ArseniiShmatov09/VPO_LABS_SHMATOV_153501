import unittest
import sys
from unittest.mock import patch
from io import StringIO
sys.path.append("/home/arsenii/VPO_LABS/LAB_01_02")
from tasks.task3 import get_positive_float_input, get_square

class TestTask3(unittest.TestCase):
    @patch('builtins.input', side_effect=["abc", "10.4"])
    def test_get_number_str(self, mock_input):
        # Перенаправляем стандартный вывод в строку
        output_buffer = StringIO()
        with patch('sys.stdout', output_buffer):
            result = get_positive_float_input("Enter a positive number: ")

        # Получаем вывод в виде строки
        output_text = output_buffer.getvalue()

        # Ожидаемые строки в выводе
        expected_strings = [
            "Enter correct float number."

        ]

        # Проверяем, что ожидаемые строки содержатся в выводе
        for expected_string in expected_strings:
            self.assertIn(expected_string, output_text)

        # Проверяем, что функция возвращает правильное значение
        self.assertEqual(result, 10.4)


    @patch('builtins.input', side_effect=["-4", "10.4"])
    def test_get_number_negative(self, mock_input):
        # Перенаправляем стандартный вывод в строку
        output_buffer = StringIO()
        with patch('sys.stdout', output_buffer):
            result = get_positive_float_input("Enter a positive number: ")

        # Получаем вывод в виде строки
        output_text = output_buffer.getvalue()

        # Ожидаемые строки в выводе
        expected_strings = [
            "Enter positive number."
        ]

        # Проверяем, что ожидаемые строки содержатся в выводе
        for expected_string in expected_strings:
            self.assertIn(expected_string, output_text)

        # Проверяем, что функция возвращает правильное значение
        self.assertEqual(result, 10.4)

    def test_get_square_positive_float_numbers(self):
        result = get_square(3.5, 2.0)
        self.assertEqual(result, 7.0)

    def test_get_square_simple_values(self):
        result = get_square(1.1, 10.5)
        self.assertEqual(result, 11.55)


if __name__ == '__main__':
    unittest.main()
