# Напишите код, который выведет на печать название файлов, размер которых более 100 MB
# Каждое значение необходимо выводить с новой строки.
# new_dict = {'file1.txt': 10, 'file2.txt': 100, 'file3.txt': 101, 'file4.txt': 200, 'file5.txt': 5, 'file6.txt': 305}


new_dict = {
    'file1.txt': 10,
    'file2.txt': 100,
    'file3.txt': 101,
    'file4.txt': 200,
    'file5.txt': 5,
    'file6.txt': 305}

for key, value in new_dict.items():
    if value > 100:
        print(key)

# Дан словарь, который содержит данные пользователя, необходимо скрыть личные данные пользователя, по определенным требованиями:
# Словарь:
# new_dict = {'Имя': 'Светлана', 'Пароль': 'qwer1234', 'Код': 1984}
# Каждый требуемый символ значения скрывается символом #
# 1)Имя - скрываются все символы, кроме первой буквы.
# Например:
# Alex - A###
# 2)Пароль - скрываются все символы
# 3)Код восстановления - скрываются все символы, кроме последней цифры.
# Каждое значение необходимо выводить с новой строки.

new_dict = {'Имя': 'Светлана',
            'Пароль': 'qwer1234',
            'Код': 1984}
for key, value in new_dict.items():
    if key == 'Имя':
        masked = value[0] + "#" * (len(value) - 1)
    elif key == 'Пароль':
        masked = "#" * len(value)
    elif key == 'Код':
        value = str(value)
        masked = "#" * (len(value) -1) + value[-1]
    print(masked)

# Напишите код, который объединяет два словаря. Если в обоих словарях есть одинаковые ключи, значения из второго словаря должны заменять значения из первого, необходимо вывести его содержимое по образцу:
# Ключ - Значение, обратите внимание, что с обеих сторон от тире идет пробел
# Например: a: 1 , после обработки a - 1
# Каждое значение необходимо выводить с новой строки.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

result = dict1.copy()
result.update(dict2)

for key, value in result.items():
    print(f"{key} - {value}")

# Напишите код, который инвертирует словарь, меняя местами ключи и значения.
# Предполагается, что значения уникальны. Необходимо вывести его содержимое по образцу:
# Ключ - Значение, обратите внимание, что с обеих сторон от тире идет пробел
# Например: a: 1 , после обработки: 1 - a
# Каждое значение необходимо выводить с новой строки.
# dict1 = {'a': 1, 'b': 2, 'c': 3}

dict1 = {'a': 1, 'b': 2, 'c': 3}
new_dict1 = {}

for key, value in dict1.items():
    new_dict1[value] = key

for key, value in new_dict1.items():
    print(f"{key} - {value}")


# Напишите код, который на входе принимает два множества с числами, через пробел.
# Выведите их пересечение, то есть значения которые есть в обоих множествах, в порядке возрастания.
# Каждое значение необходимо выводить с новой строки.
# Используйте данную строчку для ввода данных, формирующих множество:
# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))

numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))

intersection_num = numbers_1.intersection(numbers_2)
for num in sorted(intersection_num):
    print(num)

# Напишите код, который на входе принимает два множества с числами, через пробел.
# Объедините и выведите их на печать, в порядке возрастания.
# Каждое значение необходимо выводить с новой строки.
# Используйте данную строчку для ввода данных, формирующих множество:
# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))

num_1 = set(map(int, input().split()))
num_2 = set(map(int, input().split()))

unique_sorted_union = (num_1 | num_2)
for num in unique_sorted_union:
    print(num)

# Напишите код, который на входе принимает два множества с числами, через пробел.
# Проведите сверку двух множеств, если они имеют общие элементы, то выведите на печать Good, если нет, то Bad.
# Используйте данную строчку для ввода данных, формирующих множество:
# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))

numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))

common = numbers_1 & numbers_2

if common:
    print("Good")
else:
    print("Bad")

# Напишите код, который на входе принимает три множества с числами, через пробел.
# Проведите проверку данных множеств, в случае наличия элемента, который есть во всех трех множествах, то вывести на печать Good, если нет, то Bad.
# Используйте данную строчку для ввода данных, формирующих множество:
# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))
# numbers_3 = set(map(int, input().split()))

numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))

common = numbers_1 & numbers_2 & numbers_3

if common:
    print("Good")
else:
    print("Bad")

# Напишите код, который на входе принимает три множества с числами, через пробел.
# Выводите на печать элемент, который присутствует в первых двух, но отсутствует в третьем.
# Используйте данную строчку для ввода данных, формирующих множество
# numbers_1 = set(map(int, input().split()))
# numbers_2 = set(map(int, input().split()))
# numbers_3 = set(map(int, input().split()))

numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))

common_1_2 = numbers_1 & numbers_2
result = common_1_2 - numbers_3

for num in result:
        print(num)

