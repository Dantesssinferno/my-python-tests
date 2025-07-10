# Напишите код, который на входе принимает список с числами, через пробел.
# Выведите на печать первое отрицательное число в списке, используя оператор break.
# Используйте данную строчку для ввода данных, формирующих список:
# numbers = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for i in numbers:
    if i < 0:
        print(i)
        break
    else:
        continue

# Напишите код, который на входе принимает список с числами, через пробел.
# Выведите на печать только нечетные числа, используя оператор continue.
# Каждое значение необходимо выводить с новой строки.
# Используйте данную строчку для ввода данных, формирующих список:
# numbers = list(map(int, input().split()))

numbers = list(map(int, input().split()))

for i in numbers:
    if i % 2 != 0:
        print(i)
    else:
        continue

# Напишите код, который на входе принимает список с числами, через пробел.
# Подсчитайте количество положительных и отрицательных чисел в списке, и выведите на печать сперва количество положительных, затем отрицательных, используя операторы break и continue.
# Используйте данную строчку для ввода данных, формирующих список:
numbers = list(map(int, input().split()))
numbers = list(map(int, input().split()))

positive_count = 0
negative_count = 0

for num in numbers:
    if num == 0:
        continue
    elif num > 0:
        positive_count += 1
        continue
    elif num < 0:
        negative_count += 1
        continue
    else:
        break
print(positive_count)
print(negative_count)

# Напишите код, который на входе принимает список с числами, через пробел.
# Выведите на печать только те числа, которые кратны 3 или 5, используя оператор continue.
# Каждое значение необходимо выводить с новой строки.
# Используйте данную строчку для ввода данных, формирующих список:
numbers = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for i in numbers:
    if i % 3 != 0 and i % 5 != 0:
        continue
    print(i)

# Напишите код, который на входе принимает список с числами, через пробел.
# Выведите на печать второе по величине число в списке, используя оператор break.
# Используйте данную строчку для ввода данных, формирующих список:
numbers = list(map(int, input().split()))
numbers = list(map(int, input().split()))

unique_numbers = list(set(numbers)) # Удаляем дубликаты, если есть
unique_numbers.sort(reverse = True) # Сортируем по убыванию
for i in unique_numbers:
    second_big_num = unique_numbers[1]
    print(second_big_num)
    break

# Напишите код, который на входе принимает список с числами, через пробел.
# Выведите на печать все положительные элементы, используя оператор continue.
# Каждое значение необходимо выводить с новой строки.
# Используйте данную строчку для ввода данных, формирующих список:
numbers = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for i in numbers:
    if i > 0:
        print(i)
        continue
    if i <= 0:
        continue

# Напишите код, который на входе принимает список с числами, через пробел.
# Выведите на печать сумму всех положительных элементов, используя оператор break.
# Используйте данную строчку для ввода данных, формирующих список:
# numbers = list(map(int, input().split()))
numbers = list(map(int, input().split()))

sum_numbers = 0
for i in numbers:
    if i > 0:
        sum_numbers += i
        continue
    if i <= 0:
        continue
print(sum_numbers)




