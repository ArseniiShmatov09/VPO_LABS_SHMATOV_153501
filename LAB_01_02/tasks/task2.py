import re  # Импорт модуля re для работы с регулярными выражениями


# Определяем класс Person
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

# Функция для получения положительного целого числа
def get_number(input_str):
    while True:
        x = input(input_str)
        if x.isdigit() and int(x) > 0:  # Проверка, что введено положительное целое число
            return int(x)
        else:
            print("Try again, enter a positive number: ")  

# Функция для получения имени с использованием только латинских букв
def get_name(input_str):
    while True:
        name = input(input_str)
        if re.match("^[A-Za-z\s]+$", name):  # Проверка с использованием регулярного выражения
            return name
        else:
            print("Try again, use only letters: ")  
    
def input_person_data():

# Получаем количество людей, вводимое пользователем с помощью функции get_number()
    number_of_people = get_number('Enter count of people: ')

    # Создаем пустой список persons, в котором будут храниться объекты класса Person
    persons = []

    # Инициализируем переменные для анализа возрастов
    min_age = 0
    max_age = 0
    sum_of_all_ages = 0

    # В цикле пользователь вводит имя, фамилию и возраст для каждой персоны
    for i in range(0, number_of_people):

        # Получаем имя, проверяем на соответствие формату с помощью функции get_name()
        first_name = get_name('Enter name: ')

        # Получаем фамилию, проверяем на соответствие формату с помощью функции get_name()
        last_name = get_name('Enter surname: ')

        # Получаем возраст, проверяем на соответствие формату с помощью функции get_number()
        age = get_number('Enter age: ')

        # Анализируем возраст для определения минимального и максимального
        if age > max_age:
            max_age = age

        if age < min_age or i == 0:
            min_age = age

        # Создаем экземпляр класса Person и добавляем персону в список persons
        persons.append(Person(first_name, last_name, age))

    return persons, min_age, max_age, sum_of_all_ages

# Выводим финальные данные
def print_person_data(persons, min_age, max_age, sum_of_all_ages):
    print('\nSurname', 'Name', 'Age\n')

    for p in persons:
        sum_of_all_ages += p.age
        print(p.last_name, p.first_name, p.age)
    # Вычисляем средний возраст
    average_age = round(sum_of_all_ages / len(persons), 2)
    print(f'\nMin. Age = {min_age}, Max. Age = {max_age}, Average Age = {average_age}')


def main():
    persons, min_age, max_age, sum_of_all_ages = input_person_data()
    print_person_data(persons, min_age, max_age, sum_of_all_ages)

if __name__ == '__main__':
    main()