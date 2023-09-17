import unittest
from unittest import mock
import sys
import os
import tempfile
import requests

sys.path.append("/home/arsenii/VPO_LABS/LAB_01_02")
from tasks.task6 import download_file

class TestDownloadFile(unittest.TestCase):

    def test_download_file_success(self):
        # Создаем временную директорию для сохранения файла
        with tempfile.TemporaryDirectory() as tmpdirname:
            url = 'https://github.com/ArseniiShmatov09/Python_Labs_Shmatov_Arsenii_153505/archive/refs/heads/master.zip'
            save_directory = tmpdirname

            with mock.patch('requests.get') as mock_get, \
                 mock.patch('builtins.open', mock.mock_open()) as mock_open:
                mock_get.return_value.status_code = 200
                mock_get.return_value.content = b'This is a test file content'

                download_file(url, save_directory)

                # Проверяем, что файл был загружен и сохранен
                filename = os.path.join(save_directory, 'master.zip')
                mock_get.assert_called_once_with(url)
                mock_open.assert_called_once_with(filename, 'wb')
                mock_open().write.assert_called_once_with(b'This is a test file content')

    def test_download_file_failure(self):
        # Подменяем requests.get для вызова ошибки
        def mock_requests_get(url):
            raise requests.exceptions.RequestException("Mocked error")

        # Создаем временную директорию для сохранения файла
        with tempfile.TemporaryDirectory() as tmpdirname:
            url = 'https://github.com/ArseniiShmatov09/Python_Labs_Shmatov_Arsenii_153505/archive/refs/heads/master.zip'
            save_directory = tmpdirname

            with mock.patch('requests.get', side_effect=mock_requests_get), \
                 mock.patch('builtins.open', mock.mock_open()):
                try:
                    download_file(url, save_directory)
                except Exception as e:
                    # Проверяем, что возникла ожидаемая ошибка
                    self.assertIsInstance(e, requests.exceptions.RequestException)

    def test_download_file_non_200_status_code(self):
        # Создаем временную директорию для сохранения файла
        with tempfile.TemporaryDirectory() as tmpdirname:
            url = 'https://github.com/ArseniiShmatov09/NonExistentFile.zip'
            save_directory = tmpdirname

            with mock.patch('requests.get') as mock_get:
                mock_get.return_value.status_code = 404  # Мы эмулируем статус 404 (Not Found)

                try:
                    download_file(url, save_directory)
                except Exception as e:
                    # Проверяем, что возникла ожидаемая ошибка
                    self.assertIsInstance(e, requests.exceptions.HTTPError)

if __name__ == '__main__':
    unittest.main()
