# Функции работы с файлами в Python позволяют читать и писать данные в файлы, а также управлять файлами на диске.
# В этой лекции Мы рассмотрим основные функции, которые позволяют работать с файлами.

# Функция open() используется для открытия файла для чтения или записи.
# Она принимает два обязательных параметра: имя файла и режим открытия.
# Давайте рассмотрим синтаксис:
# open(filename, mode)
# Где:
# filename - имя файла, который нужно открыть.
# mode - режим (ключ) открытия файла (например, 'r' для чтения, 'w' для записи, 'a' для добавления).
# Рассмотрим простой пример:
fw = open("Doc/file_2.txt", "w")
# Данный код создаст файл в нашем проекте и далее Мы уже можем с ним работать.

# Функция write() используется для записи данных в файл.
# Она принимает два обязательных параметра: файл и данные, которые нужно записать.
# Давайте рассмотрим синтаксис:
# file.write(data)
# Где:
# file - файл, в который нужно записать данные.
# data - данные, которые нужно записать.
# Рассмотрим пример:
file = open("Doc/file_2.txt", "w")
file.write('Hello, World!')
file.close()
# fl = open("Doc/file_2.txt", "r")
# text = fl.read()
# fl.close()
#
# print(text)
# Результат: в файле file_2.txt находится фраза 'Hello, World!'
# В этом примере Мы открываем файл file_2.txt для записи и записываем в него строку 'Hello, World!' .
# Если Мы, заменим текст в нашем коде и запустим его еще раз, то этот текст заменит содержимое файла, проще говоря затрет содержимое файла

file = open("Doc/file_2.txt", "w")
file.write('Hello!!!')
file.close()

# fl = open("Doc/file_2.txt", "r")
# text = fl.read()
# fl.close()
#
# print(text)

# Результат: в файле test.txt находится фраза 'Hello'

# Чтение файла
# Функция read() используется для чтения содержимого файла.
# Она принимает один обязательный параметр: файл, который нужно прочитать.
# Давайте рассмотрим синтаксис:
# file.read()
# Где:
# file - файл, который нужно прочитать.
# Рассмотрим пример:

file = open("Doc/file_2.txt", "r")
content = file.read()
print(content)

# Результат: Hello!!!
# В этом примере Мы открываем файл Doc/file_2.txt для чтения и читаем его содержимое.

# Добавление данных в файл

# Функция write() также может использоваться для добавления данных в файл, если файл уже существует. В этом случае данные будут добавлены в конец файла.
# Рассмотрим пример:
#
file = open('Doc/file_2.txt', 'a')
file.write('\nHi, World!\nMy Friends!\nYou visit these page ')
file.close()

# Результат: в файле test.txt
# Hello, World!
# Hi, World!

file = open('Doc/file_2.txt', 'r')
content = file.read()
print(content)
file.close()
# В этом примере Мы открываем файл test.txt для добавления и добавляем в него строку 'Hi, World!'.
# При этом обратите внимание, Мы поставили в начале текста \n, это перенос строки в файле, для того, чтобы наш новый текст записался именно с новой строки.
# Если бы Мы сделали вот такую запись file.write('Hi, World!'), то результат был бы иной:
# Hello, World!Hi, World!

# Закрытие файла
# Функция close() используется для закрытия файла после его использования. Это важно для правильного закрытия файла и освобождения ресурсов.
# Давайте рассмотрим синтаксис:
# file.close()

# Где:
# file - файл, который нужно закрыть.
# Рассмотрим пример:
file = open('Doc/test.txt', 'r')
content = file.read()
print(content)
file.close()
# В этом примере Мы открываем файл test.txt для чтения, читаем его содержимое и затем закрываем файл. Обязательно необходимо закрывать файл.

# Чтение файла построчно

# Файл может состоять из нескольких строк, например это может быть перечень сотрудников компании, оборудования, нумерация заявок и т.д.
# В ходе Нашей работы, Нам может потребоваться работать с данными строками и получать доступ к одной или нескольким строкам нашего файла.
# Метод readline() - используется для чтения одной строки из файла.
# Этот метод возвращает строку, включая символ новой строки ('\n'), если он присутствует в конце строки.
# Рассмотрим на примере:

file = open('Doc/file_2.txt', 'r') # Открываем файл
first_line = file.readline()  # Читаем первую строку
lines = file.readlines() # Читаем все строки
print(first_line)             # Выводит первую строку файла
print(lines)
file.close() # Закрываем файл

# Метод readlines() - читает все строки из файла и возвращает их в виде списка.
# Рассмотрим на примере:
file = open('Doc/file_2.txt', 'r') # Открываем файл для чтения
lines = file.readlines()           # Читаем все строки в список
file.close()                       # Закрываем файл
print(lines)                       # Выводим полученный список строк
# Результат: ['Первая строчка\n', 'Вторая строчка\n', 'Третья строчка\n', 'Четвертая строчка\n']
# Так же можно вывести на печать построчно данные строки
file = open('Doc/file_2.txt', 'r') # Открываем файл для чтения
lines = file.readlines()           # Читаем все строки в списке
file.close()                       # Закрываем файл

for i in range(len(lines)):       # Используем классическую форму цикла for для вывода строк
    print(lines[i].strip())       # Используем strip() для удаления символов новой строки

# Результат:
# Первая строчка
# Вторая строчка
# Третья строчка
# Четвертая строчка
# Различия между двумя данными методами:
# 1)readline возвращает объект с типом str (строка), а readlines с типом list (список)
# 2)readline требует меньшее количество памяти, так как не требует загрузки всего файла целиком, readlines наоборот, так как загружает все строки в память сразу.