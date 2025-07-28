# Напишите код, который принимает одно значение в виде строки.
# Создайте в коде файл с именем file.txt, запишите полученное от пользователя значение в файл, а затем прочитайте его из файла и выведите на печать.
# Используйте данную строчку для ввода данных:
# value_1 = input()
from os import write

value_1 = input()
fl = open('Docs/file.txt', 'w')
fl.write(value_1)
fl.close()
fl = open('Docs/file.txt', 'r')
content = fl.read()
print(content)

# Напишите код, который принимает два значения в виде строки.
# Создайте в коде файл с именем file.txt, запишите в него сперва первое значение, затем с новой строки второе значение.
# Выведите на печать содержимое файла построчно
# Используйте данные строчку для ввода данных:
# value_1 = input()
# value_2 = input()

value_1 = input()
value_2 = input()
content = f"{value_1}\n{value_2}"
fl = open('Docs/file.txt', 'w', encoding="utf-8")
fl.write(content)
fl.close()

fl = open('Docs/file.txt', 'r', encoding="utf-8")
for line in fl:
    print(line.strip())
fl.close()