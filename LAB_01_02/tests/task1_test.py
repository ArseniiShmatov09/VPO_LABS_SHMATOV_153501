import unittest
import sys
sys.path.append("/home/arsenii/VPO_LABS/LAB_01_02")
from tasks.task1 import task1

class TestTask1(unittest.TestCase):

    def test_output_format(self):
        output = task1()
        self.assertTrue(output.startswith('Hello, World!'))
        self.assertTrue('Andhiagain!' in output)

    def test_number_of_exclamation_range(self):
        output = task1()
        exclamation_count = output.count('!')
        exclamation_count -= 2
        self.assertTrue(5 <= exclamation_count <= 50)

    def test_exclamation_sequence(self):
        output = task1()
        self.assertTrue('!!!!!' in output)

    def test_return_type(self):
        output = task1()
        self.assertIsInstance(output, str)

    def test_no_exceptions(self):
        try:
            task1()
        except Exception as e:
            self.fail(f"Функция вызвала исключение: {str(e)}")

if __name__ == '__main__':
    unittest.main()
