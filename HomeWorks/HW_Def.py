# Напишите функцию new_function(), которая запрашивает у пользователя одно число.
# Выведите на печать Good, если оно четное и Bad, если оно нечетное.

def new_function():
    num_1 = int(input())
    if num_1 % 2 == 0:
        print("Good")
    else:
        print("Bad")
new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя строку и возвращает ее в обратной последовательности.
# Выведите новое значение на печать.
# Данный код должен работать для любой строки, например:

def new_function(str_1):
    reversed_text = str_1[::-1]
    print(reversed_text)

new_function(str_1 = input())

# Напишите функцию new_function(), которая запрашивает у пользователя строку и выводит на печать количество гласных букв.

def new_function():
    user_input = input().lower() # переводим всю строку в нижний регистр
    vowels = set("аеёиоуыэюяaeiouy") # строчные буквы латиница и кириллица
    counter = 0 # счётчик гласных
    for i in user_input: # перебираем каждый символ строки
        if i in vowels:
            counter += 1 # прибавляем к счетчику каждую гласную, тем самым считаем
    print(counter)

new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя список чисел, затем выводит на печать второе по величине число.
# Если такого числа нет, то выводим на печать Bad.

def new_function():
    num_1 = [int(x) for x in input().split()] # превращаем ввод в список чисел
    uniq_num = list(set(num_1))               # убираем дубликаты
    if len(uniq_num) < 2:                     # если меньше двух чисел
        print("Bad")
        return
    uniq_num.sort(reverse=True)  # сортируем по убыванию
    second_big_num = uniq_num[1]                 # выводим второе по величине
    print(second_big_num)
new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя строку и складывает все цифры в ней.
# Далее выводит сумму на печать

def new_function():
    numbers = input()           # Получить ввод от пользователя
    total = 0                   # Счетчик суммы
    for char in numbers:        # Проходим по каждому символу
        if char.isdigit():      # Проверяем каждый символ, цифра или нет
            total += int(char)  # Если да, прибавляем ее к сумме
    print(total)                # Выводим результат

new_function()                  # Вызываем функцию

# Напишите функцию new_function(), которая запрашивает у пользователя список с элементами, а затем выводит на печать построчно все уникальные элементы.

def new_function():
    str_1 = input()         # Получить ввод от пользователя
    items = str_1.split()   # Разбиваем на элементы
    uniq_items = []         # Список для уникальных элементов

    for item in items:      # Проходим по элементам
        if item not in uniq_items:
            uniq_items.append(item)

    for element in uniq_items:
        print(element)      # Печатаем каждый построчно
new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя число, это радиус круга.
# Выведите на печать площадь круга.

def new_function():
    r = float(input())  # Запрашиваем радиус
    pi = 3.14           # Константа π
    area = pi * (r ** 2)# Площадь круга по формуле
    print(int(area))    # Выводим как целое число
new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя строку, которая является его именем, а затем к ней прибавляет " любит Python". Далее выведите на печать новую строку.
def new_function():
    str_1 = input()
    print(f'{str_1} любит Python')
new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя строку, удаляет в ней все пробелы и выводит на печать.
def new_function():
    user_input = input()
    print(user_input.replace(" ", ""))
new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя число и выводит на печать Good, если оно простое и Bad если не простое.
# Простое число - это число которое делится только на 1 и на само себя. Например 3, 5, 7, 11, 13.

def new_function():
    user_nam = int(input()) # 1. Запрашиваем у пользователя число и сразу приводим к int
    if user_nam < 2:
        print("Bad")
        return
    for i in range(2, int(user_nam ** 0.5) + 1):
        if user_nam % i == 0:
            print("Bad")
        return
    print("Good")
new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя строку, это email адрес.
# Необходимо проверить в нем наличие "@" и ".ru".
# Обязательно в такой последовательности.
# Если присутствует, то выводим на печать Good, если нет - Bad.

def new_function():
    email = input()

    if "@" in email:
        index_ch = email.index("@")     # находим позицию @
        if ".ru" in email[index_ch:]:    # проверяем, есть ли .ru после @
            print("Good")
            return
    print("Bad")

new_function()

def new_function():
    int_1 = int(input())
    int_2 = int(input())
    int_3 = int(input())
    if int_1 > int_3:
        print("Good")
    elif  int_1 <= int_3:
        print("Bad")
new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя число.
# Число может быть отрицательным, положительным или равным нулю.
# Преобразуйте данное число в положительное и выведите на печать.

def new_function():
    num_4 = int(input())
    print(abs(num_4)) # Применяем функцию abs() — она автоматически превращает отрицательное число в положительное, а ноль и положительные оставляет без изменений.
new_function()