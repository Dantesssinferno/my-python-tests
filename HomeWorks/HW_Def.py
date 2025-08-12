# Напишите функцию new_function(), которая запрашивает у пользователя одно число.
# Выведите на печать Good, если оно четное и Bad, если оно нечетное.

# def new_function():
#     num_1 = int(input())
#     if num_1 % 2 == 0:
#         print("Good")
#     else:
#         print("Bad")
# new_function()

# Напишите функцию new_function(), которая запрашивает у пользователя строку и возвращает ее в обратной последовательности.
# Выведите новое значение на печать.
# Данный код должен работать для любой строки, например:

# def new_function(str_1):
#     reversed_text = str_1[::-1]
#     print(reversed_text)
#
# new_function(str_1 = input())

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