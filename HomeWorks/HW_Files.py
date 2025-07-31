# Напишите код, который принимает одно значение в виде строки.
# Создайте в коде файл с именем file.txt, запишите полученное от пользователя значение в файл, а затем прочитайте его из файла и выведите на печать.
# Используйте данную строчку для ввода данных:
# value_1 = input()

# value_1 = input()
# fl = open('Docs/file.txt', 'w')
# fl.write(value_1)
# fl.close()
# fl = open('Docs/file.txt', 'r')
# content = fl.read()
# print(content)

# Напишите код, который принимает два значения в виде строки.
# Создайте в коде файл с именем file.txt, запишите в него сперва первое значение, затем с новой строки второе значение.
# Выведите на печать содержимое файла построчно
# Используйте данные строчку для ввода данных:
# value_1 = input()
# value_2 = input()

# value_1 = input()
# value_2 = input()
# content = f"{value_1}\n{value_2}"
# fl = open('Docs/file.txt', 'w', encoding="utf-8")
# fl.write(content)
# fl.close()
#
# fl = open('Docs/file.txt', 'r', encoding="utf-8")
# for line in fl:
#     print(line.strip())
# fl.close()

# Напишите код, который на входе принимает строку со списком названий фильмов, записанных в одну строчку через пробел.
# Создайте в коде файл с именем file.txt, запишите в него каждый элемент списка построчно.
# Затем прочтите содержимое файла и выведите на печать количество строк
# Используйте данную строчку для ввода данных, формирующих список:
# films = input().split()

# # Вводим строку и преобразуем в список фильмов
# films = input().split()
#
# # Открываем файл в режиме записи ('w') — он создаётся автоматически, если не существует
# file = open('Docs/file_1.txt', 'w', encoding='utf-8')
# for film in films:
#     file.write(film + '\n') # Записываем каждый фильм с новой строки
# file.close()
#
# # Теперь читаем файл и считаем строки
# file = open('Docs/file_1.txt', 'r', encoding='utf-8')
# lines = file.readlines()
# print(len(lines))
# file.close()

# Напишите код, который принимает одно значение в виде строки.
# Создайте в коде два файла с именем file_1.txt и file_2.txt, запишите полученное от пользователя значение в файл file_1.txt, а затем скопируйте его содержимое в file_2.txt и выведите на печать содержимое file_2.txt.
# Используйте данную строчку для ввода данных:
# value_1 = input()

# value_1 = input()
#
# file_2 = open('Docs/file_2.txt', 'w', encoding='utf-8')
# lines = file_2.write(value_1)
# file_2.close()
#
# file_2 = open('Docs/file_2.txt', 'r', encoding='utf-8')
# content = file_2.read()
# file_2.close()
#
# file_3 = open('Docs/file_3.txt', 'w', encoding='utf-8')
# lines_3 = file_3.write(content)
# file_3.close()
#
# file_3 = open('Docs/file_3.txt', 'r', encoding='utf-8')
# print(file_3.read())
# file_3.close()

# Напишите код, который принимает два значения: список и строку.
# Первое - список, который будет записываться в файл построчно
# Второе - слово, по которому будет осуществляться поиск.
# Создайте в коде файл с именем file.txt, запишите полученное от пользователя первое значение в файл построчно, а затем выведите на печать номер строки, в которой будет содержаться второе значение.
# Используйте данные строчки для ввода данных, формирующих список и принимающая строковое значение:
# films = input().split()
# value_1 = input()

# # Шаг 1: Ввод данных
# films = input().split()
# value_1 = input()


# # Шаг 2: Запись данных из списка фильмов построчно в файл
# file_films = open('Docs/file.txt', 'w', encoding = 'utf-8')
# for film in films:
#     file_films.write(film + '\n')
# file_films.close()

# # Шаг 3: Чтение файла и поиск строки с нужным значением
# file_films = open('Docs/file.txt', 'r', encoding = 'utf-8')
# lines = file_films.readlines()
# file_films.close()
#
# # Шаг 4: поиск строки содержащей искомое
# for i, line in enumerate(lines, start=1):
#     if value_1.strip() == line.strip():
#         print(i)
#         break

# Напишите код, который на входе принимает строку со списком названий фильмов, записанных в одну строчку через пробел.
# Создайте в коде файл с именем file.txt, запишите в него каждый элемент списка построчно.
# Затем прочтите содержимое файла и выведите каждый элемент построчно, поместив между ними 5 символов *.
# Используйте данную строчку для ввода данных, формирующих список:
# films = input().split()

# # Шаг 1: Ввод данных
# films = input().split()
# # Шаг 2: Запись данных из списка фильмов построчно в файл
# fl = open('Docs/file.txt', 'w', encoding='utf-8')
# for film in films:
#     fl.write(film + '\n')
# fl.close()
# # Шаг 3: Чтение файла
# fl = open('Docs/file.txt', 'r', encoding='utf-8')
# lines = fl.readlines()
# fl.close()
# # Шаг 4: вывод 5 звездочек между фильмами
# for i in range(len(lines)):
#     print(lines[i].strip())
#     if i != len(lines) - 1:
#         print('*****')

# Самостоятельно попробовать работу с одним из  ключей в файлах и приложить скриншот или текстовую версию кода.
# Не используйте примеры из лекции и сторонних источников, постарайтесь разнообразить свое решение и задать ему логику.
# Ответ в виде скриншота или текста, прошу приложить в Решения

# Шаг 1. Запись в текстовый файл (вручную, как строку)
f = open('profile.txt', 'w', encoding='utf-8')
f.write('name: Max\nage: 33\ncity: Ribnitca\n')
f.close()

# Шаг 2. Чтение из файла и преобразование в словарь
f = open('profile.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

# Шаг 3. Парсинг строк в словарь
profile = {}
for line in lines:
    key, value = line.strip().split(": ")
    profile[key] = value

# Шаг 4. Обновление возраста
profile["age"] = str(30)  # преобразуем в строку, так как остальные значения тоже строки

# Шаг 5. Печать обновлённого возраста
print("Новый возраст:", profile["age"])

# (Опционально) Шаг 6. Запись обратно в файл
f = open('profile.txt', 'w', encoding='utf-8')
for k, v in profile.items():
    f.write(f"{k}: {v}\n")
f.close()