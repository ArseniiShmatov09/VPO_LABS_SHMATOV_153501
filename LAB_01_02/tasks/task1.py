from random import randint  # Импорт функции randint из модуля random

def task1():
# Генерируем случайное количество восклицательных знаков от 5 до 50
    number_of_exclamation = randint(5, 50)

    exclamation = ""  # Создаем пустую строку для хранения восклицательных знаков
    for e in range(0, number_of_exclamation):
        exclamation += '!'  # Добавляем восклицательный знак к строке

    # Выводим сообщение с восклицательными знаками
    return(f'Hello, World!\nAndhiagain!\n{exclamation}')

if __name__ == '__main__':
    print(task1())