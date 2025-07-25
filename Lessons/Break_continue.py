# Операторы break и continue используются для управления потоком выполнения циклов.
# Они позволяют изменять поведение цикла, чтобы выполнить определенные действия, когда это необходимо.

# Оператор break

# Оператор break используется для принудительного выхода из цикла, даже если условие цикла все еще истинно.
# Он прекращает выполнение цикла и переходит к следующей инструкции после цикла.
# Рассмотрим простой пример с циклом for:
list = [0, 1, 2, 3, 4, 5]

for i in list:
    print(i)
# Результат:
# 0
# 1
# 2
# 3
# 4
# 5

# С каждой итерацией Мы выводим на печать элемент списка. Давайте чуть видоизменим наш код
list = [0, 1, 2, 3, 4, 5]

for i in list:
    if i == 3:
        break
    print(i)
# Результат:
# 0
# 1
# 2

# В этом примере Мы используем цикл for для итерации по числам от 0 до 5.
# Когда i становится равным 3, Мы используем оператор break, чтобы прекратить выполнение цикла и перейти к следующей инструкции.
# Несмотря на то, что в списке еще есть элементы, оператор break останавливает его работу.
# Если ни один из элементов списка не будет равен условию, то список отработает полностью.
# Рассмотрим этот момент на примере, когда в списки элементы находятся от 0 до 5, а оператор break отрабатывает, когда i == 6:
list = [0,1,2,3,4,5]

for i in list:
    if i == 6:
        break
    print(i)

# Результат:
# 0
# 1
# 2
# 3
# 4
# 5

# Теперь рассмотрим пример оператора break с циклом while:
login = input("Введите Ваше имя: ")

while True:
    if login == "Alex":
        print("Вы ввели верный логин")
        password = input("Введите Ваш пароль: ")

    else:
        print("Вы ввели неверный пароль")
        break
# Цикл while будет работать пока условие равно истине, Мы запрашиваем у пользователе ввести логин, если он равен тому, который Мы ожидаем, то программа продолжает дальнейшую логику, в противном случае Мы переходим в блок else, где получаем сообщение что логин некорректен и далее срабатывает оператор break, который останавливает программу.
# Рассмотрим другой пример:
i = 0
while i < 5:
    i += 1
    if i == 3:
        break
    print(i)

# Результат:
# 1
# 2

# В этом примере Мы используем цикл while для итерации по числам от 0 до 4. Когда i становится равным 3, Мы используем оператор break, чтобы прекратить выполнение цикла и перейти к следующей инструкции.

# Оператор continue
# Оператор continue используется для пропуска текущей итерации цикла и перехода к следующей.
# Он позволяет пропустить выполнение текущей итерации и продолжить выполнение цикла с следующей итерацией.
# Рассмотрим простой пример с циклом for:
list = [0,1,2,3,4,5]

for i in list:
    if i % 2 == 0:
        continue
    print(i)

# Результат:
# 1
# 3
# 5

# В этом примере Мы используем цикл for для итерации по списку от 0 до 5.
# Когда i является четным числом, Мы используем оператор continue, чтобы пропустить вывод этого числа и перейти к следующей итерации.
# Теперь рассмотрим пример оператора continue в циклах while.
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Результат:
# 1
# 3
#

# В этом примере Мы используем цикл while для итерации по числам от 0 до 4.
# Когда i является четным числом, Мы используем оператор continue, чтобы пропустить вывод этого числа и перейти к следующей итерации.
# Операторы break и continue позволяют управлять потоком выполнения циклов, чтобы выполнить определенные действия, когда это необходимо.
# Они могут быть использованы в циклах for и while для создания более гибких и адаптируемых циклических конструкций.

