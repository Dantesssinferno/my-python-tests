# Напишите функцию new_function(), которая запрашивает у пользователя одно число, от 1 до 6 включительно.
# Если число более 6, то выводим на печать Bad.
# Если 1 - 3, то выводим на печать четное число как слово, например пользователь ввел 2 - то на печать выводим Два, в остальных вариантах Bad.
# Если 4 - 6, то выводим на печать нечетное число как слово, в остальных вариантах Bad.
# Дополнительное пояснение:
# у нас есть 3 группы данных:
# 1. 1 -3 , это 1, 2, 3
# 2. 4-6, это 4, 5 ,6
# 3. иные
# в первой группе, если пользователь ввел четно число, то есть в данном случае это 2, то мы печатаем цифру словом, в остальных случаях BAD
# во второй группе, если пользователь ввел нечетное число, то есть 5, мы печатаем цифру словом, в остальных случая BAD
# в третьей группе всегда BAD

def new_function():
    n = int(input())

    if 1 <= n <= 3: # первая группа
        if n % 2 == 0: # если четное, то
            if n == 2:
                print("Два")
            else:
                print("Bad")
        else:
            print("Bad")
    elif 4 <= n <= 6:# вторая группа
        if n % 2 != 0: # если нечетное, то
            if n == 5:
                print("Пять")
            else:
                print("Bad")
        else:
            print("Bad")
    else:           # третья группа
        print("Bad")
new_function()

# Напишите функцию new_function(), которая принимает два значения в виде числа, ОДНО (первое) из которых запрашивает у пользователя, другое является константой и равно 7.
# Создайте код, который делит первое число на второе, если оно делится без остатка, то выводим на печать Good, в иной ситуации Bad.
# Данный код должен работать для любой строки, например:
# Входные данные	Решение
# 14	Good
# 6	Bad
# Sample Input:
# 14
# Sample Output:
# Good
def first_num():  # Функция которая запрашивает у юзера первое число
    num_1 = int(input())
    return num_1 # Функция возвращает первое число для дальнейшего использования в других функциях

def new_function(num_1, num_2 = 7): # Функция которая принимает первое и второе число
    division = num_1 / num_2 # Делим первое число на второе и на результат ссылаемся переменной
    if division % 2 == 0:    # проверяем, если четное, то печатаем Good
        print("Good")
    else:                    # Иначе, печатаем Bad
        print("Bad")
new_function(first_num())    # Вызываем функцию new_function и передаем позиционный аргумент

# Напишите 3 функции: logic(), even(), odd(). Примите от пользователя одно значение в виде числа.
#
# Функция logic() должна его отработать,
# если оно четное, то отправить в функцию even(), которая выведет сообщение "ЧЕТ",
# если нечетное, то odd() и "НЕЧЕТ"

def logic ():
    user_num = int(input()) # пользовательский ввод
    if user_num % 2 == 0:   # четное
        even(user_num)
    else:
        odd(user_num)
def even (user_num):        # если четное, то из logic() передается число в even()
    print("ЧЕТ")
def odd (user_num):         # # если нечетное, то из logic() передается число в odd()
    print("НЕЧЕТ")

logic()

# Напишите функцию new_function(), которая принимает одно значение в виде строки. Это Фамилия Имя Отчество.
# Создайте код который выведет на печать только имя пользователя.

def new_function():
    user_input = input().strip() # убираю лишние элементы
    parts_of_user_input = user_input.split() # создаем список
    print(parts_of_user_input[1])           # выводим второй элемент на печать
new_function()

# Напишите функцию new_function(), которая принимает одно значение в виде строки. Это Фамилия Имя Отчество.
# Создайте код который выведет на печать фамилию и инициалы.
# Например:
# Иванов Иван Иванович
# После обработки:
# Иванов И.И.

def new_function():
    user_input = input().strip() # пользовательский ввод, удаляем пробелы и лишние символы
    parts = user_input.replace('\t', ' ').split() # создаю новый список строк

    if not parts:
        print("")
        return
    surname = parts[0]

    if len(parts) == 1:
        print(surname)
        return

    name_initial = parts[1][0].upper() + "."
    patronymic_initial = parts[2][0].upper() + "." if len(parts) >= 3 and parts[2] else ""

    print(f"{surname} {name_initial}{patronymic_initial}")
new_function()

# Напишите функцию new_function(), которая принимает два значения: строку - это Имя и число - это год рождения.
# Текущий год по дефолту 2024
# Создайте код который выведет на печать "Меня зовут <Имя>, мне <возраст>."
# Например:
# Иван
# 1990
# После обработки:
# Меня зовут Иван, мне 34.

def new_function():
    user_name = input()
    user_birth_date = int(input())
    year_now = 2024
    user_age = year_now - user_birth_date
    print(f'Меня зовут {user_name}, мне {user_age}.')
new_function()

# Напишите 3 функции: logic(), russia(), england().
# Примите два значения в виде строк: первое - Имя, второе - Страна проживания.
# Функция logic() должна их отработать, если страна = Россия, то отрабатывает функция russia() и выводит на печать "Здравствуй <Имя>", если страна = England, то отрабатывает функция england() и выводит на печать "Hello <Имя>".

def logic():
    user_name = input()
    user_country = input()
    if user_country == "Россия":
        russia(user_name, user_country)
    elif user_country == "England":
        england(user_name, user_country)
    else:
        england(user_name, user_country)

def russia(user_name, user_country):
    print(f"Здравствуй {user_name}")

def england(user_name, user_country):
    print(f"Hello {user_name}")

logic()


# Напишите 3 функции: logic(), russia(), england().
# Примите два значения в виде строк: первое - Имя, второе - Страна проживания.
# Функция logic() должна их отработать, если страна = Россия, то отрабатывает функция russia(),
# которая создает файл russia.txt и записывает туда имя, если страна = England,
# то отрабатывает функция england(), которая создает файл england.txt и записывает туда имя.
# Затем выведите на печать содержимое файла куда была сделана запись.

# принимаем два аргумента name и country


# # Функция logic() принимает в качестве аргуметов данные из переменных user_name, user_country
def logic(name: str, country: str):
    if country.lower() in ("россия","russia"):
        russia(name)
    elif country.lower() in ("англия","england"):
        england(name)
#
# # Функция которая принимает значение россия и записывает в файл и выводит на печать содержимое
def russia(name: str):
    russian_file = "russia.txt"
    with open(russian_file, "w", encoding = "utf-8") as rus_file:
       rus_file.write(name)
    with open(russian_file, "r", encoding = "utf-8") as rus_file:
        rus_content = rus_file.read()
        print(rus_content)

# # Функция которая принимает значение england и записывает в файл и выводит на печать содержимое
def england(name: str):
    england_file = "england.txt"
    with open(england_file, "w", encoding = "utf-8") as en_file:
       en_file.write(name)
    with open(england_file, "r", encoding = "utf-8") as en_file:
        en_content = en_file.read()
        print(en_content)


# # Вызываю функцию logic и передаю два аргумента user_name, user_country
user_name = input()
user_country = input()
logic(user_name, user_country)

# Напишите функцию new_function(), которая принимает два значения в виде чисел. Первое - количество дней и оно может быть от 1 до 3,
# в противном случае выводит Bad.
# Второе - баланс на счете, не может быть меньше 30, в противном случае выводим Bad.
# Функция new_function() создает файл file.txt, затем производит списывание 7 рублей за каждый день и записывает в файл построчно строки, за каждый день списывания, по формату, далее вывести на печать содержимое файла:
# <Нумерация дня> день - баланс <Баланс> - списалось 7 - осталось <Баланс - Нумерация дня * 7>
# Например:
# пользователь ввел 2 и 100
# После обработки:
# 1 день - баланс 100 - списалось 7 - осталось 93
# 2 день - баланс 93 - списалось 7 - осталось 86


def new_function(days:int, balance:int):
    if not 1 <= days <= 3 or balance < 30:
        print("Bad")
        return
    file_name = "file.txt"
    current_balance = balance
    with open(file_name, "w", encoding="utf-8") as f:
        for day in range(1, days + 1):
            remained = current_balance - 7
            string_in_file = (f"{day} день - баланс {current_balance} - списалось 7 - осталось {remained}\n")
            f.write(string_in_file)
            current_balance = remained
    with open(file_name, "r", encoding="utf-8") as f:
        print(f.read())

days = int(input())
balance = int(input())
new_function(days, balance)

# Напишите функцию new_function(), которая принимает два значения в виде чисел.
# Первое - баланс на карте. Второе - сумма перевода.
# Если сумма перевод меньше баланса, то производи перевод и выводим на печать остаток на балансе.
# Если сумма перевода больше баланса, то выводим на печать "Не хватает денежных средств".
# Если суммы равны, то выводим "0"

def new_function(balance: int, sum_transaction:int):
    if sum_transaction < balance:
        current_balance = balance - sum_transaction
        print(current_balance)
    elif sum_transaction > balance:
        print("Не хватает денежных средств")
    else:
        print("0")

user_balance = int(input())
user_transaction = int(input())
new_function(user_balance, user_transaction)

# Напишите функцию new_function(), которая принимает два значения в виде чисел.
# Свадебный банкет,
# первое число - количество гостей которые будут есть,
# второе число - количество гостей которые будут пить чай.
# Второе число не может быть больше первого, иначе выводим Bad.
# Стоимость еды на одного человека - 3000
# Стоимость чая на одного человека - 500
# Произвести расчет суммы стоимости свадебно банкета из количества кушающих и пьющих чай гостей.
# Например:
# 10
# 5

def new_function(guest_eat:int,guest_tea:int):
    eat_coast = 3000
    tea_coast = 500
    if guest_tea > guest_eat:
        print("Bad")
    else:
        wedding_summ = (guest_eat * eat_coast) + (guest_tea * tea_coast)
        print(wedding_summ)

guest_eat = int(input())
guest_tea = int(input())
new_function(guest_eat, guest_tea)
