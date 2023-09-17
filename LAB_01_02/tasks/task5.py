import os

# Функция для поиска файлов с заданным расширением в указанной директории и ее подпапках
def find_files_by_extension(directory, extension):
    found_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith("." + extension):
                file_path = os.path.join(root, file)
                found_files.append(file_path)
    
    return found_files

# Функция для получения директории от пользователя
def get_directory(input_str):
    while True:
       search_directory = input(input_str)
       if not os.path.exists(search_directory) or not os.path.isdir(search_directory):
            print("The specified directory does not exist or is not a directory.")
       else:
            return search_directory 
       

if __name__ == '__main__':       
       
    # Получаем директорию от пользователя
    search_directory = get_directory('Enter directory: ')

    # Получаем расширение файла от пользователя
    file_extension = input('Enter extension: ')

    # Ищем файлы с указанным расширением в указанной директории и ее подпапках
    found_files = find_files_by_extension(search_directory, file_extension)

    # Выводим результаты
    if not found_files:
        print(f"No files with extension '.{file_extension}' were found in the specified directory or its subdirectories.")
    else:
        print(f"Found files with the extension '.{file_extension}':")
        for file_path in found_files:
            print(file_path)
