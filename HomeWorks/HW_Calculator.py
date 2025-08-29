ALLOWED_OPS = {'+', '-', '*', '/'}
def to_number(text:str) -> float:
    return float(text.strip().replace(",",".")) # нормализую число, разделитель точка

def summ(a:float, b:float) -> float:
    return a + b

def difference(a:float, b:float) -> float:
    return a - b

def multiplication(a:float, b:float) -> float:
    return a * b

def division(a:float, b:float) -> float:
    return a / b # будем ловить exception деления на 0

def logic(user_operator:str, num_1:float, num_2:float) -> float:
    # Определяю операцию по введеному знаку
    if user_operator == '+':
        return summ(num_1, num_2)
    elif user_operator == '-':
        return difference(num_1, num_2)
    elif user_operator == '*':
        return multiplication(num_1, num_2)
    elif user_operator == '/':
        return division(num_1, num_2)

user_operator = input("Введите арифметический оператор: +, -, *, / ").strip()

if user_operator not in ALLOWED_OPS:
    print("Ошибка: разрешены только '+', '-', '*', '/'")
else:
    row_1 = input("Введите первое число: ").strip()
    row_2 = input("Введите второе число: ").strip()
    try:
        # заменяем запятую на точку и сразу преобразуем к float
        num1 = float(row_1.replace(",", "."))
        num2 = float(row_2.replace(",", "."))
        result = logic(user_operator, num1, num2)
    except ValueError:
        print("Ошибка: ожидалось число. Например: 3,25 или 5.69")
    except ZeroDivisionError:
        print("Ошибка: на ноль делить нельзя")
    else:
        print(result)




