# Напишите код, который на входе принимает список из цифр, записанных в одну строчку через пробел.
# Создайте в коде файл с именем file.txt, запишите в него каждый элемент списка построчно.
# Затем прочтите содержимое файла и выведите на печать сумму всех элементов файла.
# Используйте данную строчку для ввода данных, формирующих список:
# numbers = list(map(int, input().split()))
from collections import Counter

# Шаг 1: Принимаем список цифр в одну строку через пробел
numbers = list(map(int, input().split()))

# Шаг 2: Создание файла file.txt и запись
with open('file.tst', 'w', encoding ='utf-8') as file:
    for num in numbers:
        content = file.write(f'{num}\n')

# Шаг 3: ЧИТАЕМ ФАЙЛ И СЧИТАЕМ СУММУ
total = 0
with open('file.tst', 'r', encoding ='utf-8') as file:
    for line in file:
        total += int(line.strip()) # убираем \n и преобразуем в int
# Шаг 4: Выводим сумму
print(total)

# Напишите код, который на входе принимает список из цифр, записанных в одну строчку через пробел.
# Создайте в коде два файла с именем file_1.txt и file_2.txt.
# Запишите в file_1.txt каждый элемент списка построчно, затем скопируйте в file_2.txt каждую нечетную строку и выведите на печать содержимое file_2.txt.
# Используйте данную строчку для ввода данных:
# numbers = list(map(int, input().split()))

# Шаг 1: Получаем список чисел с клавиатуры
numbers = list(map(int, input().split()))

# Шаг 2: Записываем каждое число в отдельную строку файла file_1.txt
with open('file_1.txt', 'w') as f1:
    for number in numbers:
        f1.write(f"{number}\n")

# Шаг 3: Читаем строки из file_1.txt
with open('file_1.txt', 'r') as f1:
    lines = f1.readlines()

# Шаг 4: Записываем только нечетные строки (0-я, 2-я, 4-я и т.д.) в file_2.txt
with open('file_2.txt', 'w') as f2:
    for i in range(0, len(lines), 2):
        f2.write(lines[i])

# Шаг 5: Читаем и выводим содержимое file_2.txt
with open('file_2.txt', 'r') as f2:
    for line in f2:
        print(line.strip())

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


# Напишите код, который на входе принимает список из цифр, записанных в одну строчку через пробел.
# Создайте в коде два файла с именем file_1.txt и file_2.txt.
# Запишите в file_1.txt каждый элемент списка построчно, затем отсортируйте их по убыванию и запишите в file_2.txt.
# Выведите на печать содержимое file_2.txt.
# Используйте данную строчку для ввода данных:
# numbers = list(map(int, input().split()))

# Принять список из цифр
numbers = list(map(int, input().split()))
# Записать каждую цифру построчно в file_1.txt
with open('file_1.txt', 'w', encoding='utf-8') as f1:
    for num in numbers:
        f1.write(f'{num}\n')
# Сортировка по убыванию
sorted_numbers = sorted(numbers, reverse= True)
# Запись в файл file_2.txt
with open('file_2.txt', 'w', encoding = 'utf-8') as f2:
    for num in sorted_numbers:
        f2.write(f'{num}\n')
# Чтение и вывод на печать содержимого файла
with open('file_2.txt', 'r', encoding ='utf-8') as f2:
    for line in f2:
        print(line.strip())

# Напишите код, который на входе принимает список с названием фильмов, записанных в одну строчку через пробел.
# Создайте в коде файл с именем file_1.txt.
# Запишите в file_1.txt каждый элемент списка построчно.
# Напишите программу, которая считывает строки из файла и подсчитывает частоту каждого слова.
# Результаты выводятся по образцу, отсортированного по частоте слов в порядке убывания.
# Ключ - Значение, обратите внимание, что с обеих сторон от тире идет пробел
# Например: Скала - 1
# Используйте данную строчку для ввода данных:
# films = input().split()

# Ввод списка фильмов
films = input().split()
# Шаг 1: Запись в file_1.txt
with open('file_1.txt', 'w', encoding='utf-8') as f1:
    for film in films:
        f1.write(f'{film}\n') # Записываем каждый фильм построчно
# Шаг 2: Читаем file_1.txt и подсчитываем частоту
with open('file_1.txt', 'r', encoding='utf-8') as f1:
    words = [line.strip() for line in f1] # Убираем переносы строк

# Шаг 3: Считаем частоту
counter = Counter(words)

# Шаг 4: Вывод отсортированного по частоте слов и в порядке убывания
for word, count in counter.most_common():
    print(f'{word} - {count}')

# Напишите код, который принимает два значения в виде строки.
# Создайте в коде три файла с именем file_1.txt, file_2.txt и file_3.txt, запишите полученное от пользователя первое значение в файл file_1.txt, второе значение в файл file_2.txt, а затем скопируйте его содержимое обоих файлов в file_3.txt и выведите его содержимое на печать.
# Используйте данную строчку для ввода данных:
# value_1 = input()

# Прием значений
value_1 = input()
value_2 = input()
# Запись в file_1.txt первого значения от пользователя
with open('file_1.txt', 'w', encoding='utf-8') as f1:
    f1.write(value_1)
# Запись в file_2.txt второго значения от пользователя
with open('file_2.txt', 'w', encoding='utf-8') as f2:
    f2.write(value_2)
# Чтение обоих файлов
with open('file_1.txt', 'r', encoding='utf-8') as f1:
    line_1 = f1.read()
with open('file_2.txt', 'r', encoding='utf-8') as f2:
    line_2 = f2.read()
# Запись в file_3.txt значений первых двух файлов
with open('file_3.txt', 'w', encoding='utf-8') as f3:
    f3.write(line_1 + '\n' + line_2)
# Вывод на печать
with open('file_3.txt', 'r', encoding='utf-8') as f3:
    print(f3.read())