import unittest
from unittest.mock import patch
import sys
import os
import tempfile
from io import StringIO


sys.path.append("/home/arsenii/VPO_LABS/LAB_01_02")
from tasks.task5 import get_directory, find_files_by_extension

class TestGetDirectory(unittest.TestCase):

    @patch('builtins.input', side_effect=['/home'])
    def test_valid_directory(self, mock_input):
        result = get_directory('Enter directory path: ')
        self.assertEqual(result, '/home')

    @patch('builtins.input', side_effect=['/path/to/nonexistent/directory', '/home/arsenii/VPO_LABS'])
    def test_invalid_directory_then_valid_directory(self, mock_input):
        result = get_directory('Enter directory path: ')
        self.assertEqual(result, '/home/arsenii/VPO_LABS')

    def test_find_files(self):
        # Создаем временную директорию с несколькими файлами разных расширений
        with tempfile.TemporaryDirectory() as temp_dir:
            # Создаем файлы с разными расширениями
            open(os.path.join(temp_dir, 'file1.txt'), 'w').close()
            open(os.path.join(temp_dir, 'file2.txt'), 'w').close()
            open(os.path.join(temp_dir, 'file3.md'), 'w').close()
            open(os.path.join(temp_dir, 'file4.txt'), 'w').close()
            
            # Ищем файлы с расширением '.txt'
            result = find_files_by_extension(temp_dir, 'txt')
            
            # Проверяем, что найдено 3 файла с расширением '.txt'
            self.assertEqual(len(result), 3)
            # Проверяем, что все файлы имеют правильное расширение
            self.assertTrue(all(file.endswith('.txt') for file in result))
            
    def test_no_files_found(self):
        # Создаем временную директорию без файлов
        with tempfile.TemporaryDirectory() as temp_dir:
            # Ищем файлы с расширением '.txt'
            result = find_files_by_extension(temp_dir, 'txt')
            
            # Проверяем, что результат пустой список
            self.assertEqual(result, [])

    def test_find_html_files(self):
        # Задаем путь к директории и расширение
        directory = '/home/arsenii/IGI_LABS/LAB_04'
        extension = 'html'

        # Вызываем функцию для поиска файлов
        found_files = find_files_by_extension(directory, extension)

        # Ожидаемое количество файлов
        expected_count = 20  # Убедитесь, что это число верное

        # Проверяем, что найдено правильное количество файлов
        self.assertEqual(len(found_files), expected_count)

        # Проверяем, что все файлы имеют нужное расширение
        for file_path in found_files:
            self.assertTrue(file_path.endswith('.html'))


if __name__ == '__main__':
    unittest.main()
