# Функция для получения положительного числа с плавающей точкой
def get_positive_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print('Enter positive number.')  # Вывод сообщения об ошибке для отрицательных чисел
        except ValueError:
            print('Enter correct float number.')  # Вывод сообщения об ошибке для некорректных значений



def get_square(a, b):
    return a * b


if __name__ == '__main__':

    #Получаем ширину и высоту от пользователя с использованием функции
    a = get_positive_float_input('Enter width: ')
    b = get_positive_float_input('Enter height: ')

    # Вычисляем площадь и выводим результат
    print('Square is:', get_square(a, b))
