# Напишите код, который на входе принимает список из цифр, записанных в одну строчку через пробел.
# Создайте в коде файл с именем file.txt, запишите в него каждый элемент списка построчно.
# Затем прочтите содержимое файла и выведите на печать сумму всех элементов файла.
# Используйте данную строчку для ввода данных, формирующих список:
# numbers = list(map(int, input().split()))

# # Шаг 1: Принимаем список цифр в одну строку через пробел
# numbers = list(map(int, input().split()))
#
# # Шаг 2: Создание файла file.txt и запись
# with open('file.tst', 'w', encoding ='utf-8') as file:
#     for num in numbers:
#         content = file.write(f'{num}\n')
#
# # Шаг 3: ЧИТАЕМ ФАЙЛ И СЧИТАЕМ СУММУ
# total = 0
# with open('file.tst', 'r', encoding ='utf-8') as file:
#     for line in file:
#         total += int(line.strip()) # убираем \n и преобразуем в int
# # Шаг 4: Выводим сумму
# print(total)

# Напишите код, который на входе принимает список из цифр, записанных в одну строчку через пробел.
# Создайте в коде два файла с именем file_1.txt и file_2.txt.
# Запишите в file_1.txt каждый элемент списка построчно, затем скопируйте в file_2.txt каждую нечетную строку и выведите на печать содержимое file_2.txt.
# Используйте данную строчку для ввода данных:
# numbers = list(map(int, input().split()))

# # Шаг 1: Получаем список чисел с клавиатуры
# numbers = list(map(int, input().split()))
#
# # Шаг 2: Записываем каждое число в отдельную строку файла file_1.txt
# with open('file_1.txt', 'w') as f1:
#     for number in numbers:
#         f1.write(f"{number}\n")
#
# # Шаг 3: Читаем строки из file_1.txt
# with open('file_1.txt', 'r') as f1:
#     lines = f1.readlines()
#
# # Шаг 4: Записываем только нечетные строки (0-я, 2-я, 4-я и т.д.) в file_2.txt
# with open('file_2.txt', 'w') as f2:
#     for i in range(0, len(lines), 2):
#         f2.write(lines[i])
#
# # Шаг 5: Читаем и выводим содержимое file_2.txt
# with open('file_2.txt', 'r') as f2:
#     for line in f2:
#         print(line.strip())

# Напишите код, который на входе принимает список с названием фильмов, записанных в одну строчку через пробел.
# Создайте в коде два файла с именем file_1.txt и file_2.txt.
# Запишите в file_1.txt каждый элемент списка построчно, затем отсортируйте их по алфавиту и запишите в file_2.txt.
# Выведите на печать содержимое file_2.txt.
# Используйте данную строчку для ввода данных:
# films = input().split()

# Получаем список фильмов
films = input().split()

# Шаг 1: Записываем каждый фильм в новую строку файла file_1.txt
with open('file_1.txt', 'w', encoding='utf-8') as f1:
    for film in films:
        f1.write(film + '\n')

# Шаг 2: Читаем строки из file_1.txt
with open('file_1.txt', 'r', encoding='utf-8') as f1:
    film_lines = f1.readlines()

# Шаг 3: Сортируем фильмы по алфавиту
sorted_films = sorted([line.strip() for line in film_lines])

# Шаг 4: Записываем отсортированные фильмы в file_2.txt
with open('file_2.txt', 'w', encoding='utf-8') as f2:
    for film in sorted_films:
        f2.write(film + '\n')

# Шаг 5: Выводим содержимое file_2.txt
with open('file_2.txt', 'r', encoding='utf-8') as f2:
    for line in f2:
        print(line.strip())