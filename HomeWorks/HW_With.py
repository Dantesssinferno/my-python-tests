# Напишите код, который на входе принимает список из цифр, записанных в одну строчку через пробел.
# Создайте в коде файл с именем file.txt, запишите в него каждый элемент списка построчно.
# Затем прочтите содержимое файла и выведите на печать сумму всех элементов файла.
# Используйте данную строчку для ввода данных, формирующих список:
# numbers = list(map(int, input().split()))

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

