import unittest
import sys
from unittest.mock import patch
from io import StringIO
sys.path.append("/home/arsenii/VPO_LABS/LAB_01_02")
from tasks.task2 import get_number, get_name, Person, input_person_data, print_person_data

class TestTask2(unittest.TestCase):

    @patch('builtins.input', side_effect=["abc", "-5", "10"])
    def test_get_number(self, mock_input):
        # Перенаправляем стандартный вывод в строку
        output_buffer = StringIO()
        with patch('sys.stdout', output_buffer):
            result = get_number("Enter a positive number: ")

        # Получаем вывод в виде строки
        output_text = output_buffer.getvalue()

        # Ожидаемые строки в выводе
        expected_strings = [
            "Try again, enter a positive number:",
        ]

        # Проверяем, что ожидаемые строки содержатся в выводе
        for expected_string in expected_strings:
            self.assertIn(expected_string, output_text)

        # Проверяем, что функция возвращает правильное значение
        self.assertEqual(result, 10)

    @patch('builtins.input', side_effect=["-3", "-0l2d/", "Anna"])
    def test_get_name(self, mock_input):
        # Перенаправляем стандартный вывод в строку
        output_buffer = StringIO()
        with patch('sys.stdout', output_buffer):
            result = get_name("Enter name: ")

        # Получаем вывод в виде строки
        output_text = output_buffer.getvalue()

        # Ожидаемые строки в выводе
        expected_strings = [
            "Try again, use only letters: ",
        ]

        # Проверяем, что ожидаемые строки содержатся в выводе
        for expected_string in expected_strings:
            self.assertIn(expected_string, output_text)

        # Проверяем, что функция возвращает правильное значение
        self.assertEqual(result, 'Anna')


    @patch('builtins.input', side_effect=["2", "John", "Doe", "30", "Alice", "Smith", "25"])
    def test_input_person_data(self, mock_input):
        persons, min_age, max_age, sum_of_all_ages = input_person_data()

        self.assertIsInstance(persons, list)
        self.assertTrue(all(isinstance(p, Person) for p in persons))
        self.assertEqual(len(persons), 2)
        
        self.assertEqual(min_age, 25)
        self.assertEqual(max_age, 30)

    def setUp(self):
        # Перехватываем вывод stdout
        self.output_buffer = StringIO()
        sys.stdout = self.output_buffer

    def tearDown(self):
        # Восстанавливаем stdout после выполнения теста
        sys.stdout = sys.__stdout__
    def test_print_person_data(self):
        # Создаем список персон для теста
        persons = [Person('Иван', 'Петров', 77), Person('Мария', 'Иванова', 33),Person('Мария', 'Иванова', 40) ]
        min_age = 33
        max_age = 77
        sum_of_all_ages = 0

        # Вызываем функцию для вывода данных
        print_person_data(persons, min_age, max_age, sum_of_all_ages)

        # Получаем вывод функции из буфера
        output = self.output_buffer.getvalue()

        # Проверяем, что ожидаемая информация присутствует в выводе
        self.assertIn('Surname Name Age', output)
        self.assertIn('Петров Иван 77', output)
        self.assertIn('Иванова Мария 33', output)
        self.assertIn('Min. Age = 33', output)
        self.assertIn('Max. Age = 77', output)
        self.assertIn('Average Age = 50.0', output)
    
if __name__ == '__main__':
    unittest.main()
