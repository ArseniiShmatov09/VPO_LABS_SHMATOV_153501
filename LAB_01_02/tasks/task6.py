import os
import requests

# Функция для загрузки файла по URL и сохранения его в указанной папке
def download_file(url, save_directory):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Получаем имя файла из URL
            filename = url.split("/")[-1]

            # Собираем полный путь для сохранения
            save_path = os.path.join(save_directory, filename)

            # Сохраняем файл на локальный диск
            with open(save_path, 'wb') as f:
                f.write(response.content)
            
            print(f"Файл успешно скачан и сохранен по пути: {save_path}")
        else:
            print(f"Ошибка при загрузке файла. Статус код: {response.status_code}")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

# Получаем URL и путь к папке для сохранения от пользователя

# Функция для получения директории от пользователя
def get_directory(input_str):
    while True:
       search_directory = input(input_str)
       if not os.path.exists(search_directory) or not os.path.isdir(search_directory):
            print("The specified directory does not exist or is not a directory.")
       else:
            return search_directory 

if __name__=='__main__':

    save_directory = get_directory("Введите путь к папке для сохранения: ")
    url = input("Введите URL: ")

    # Вызываем функцию для загрузки и сохранения файла
    download_file(url, save_directory)
