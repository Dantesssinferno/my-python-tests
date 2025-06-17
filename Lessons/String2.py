name = "Ivan"
name = "Max"
a = "Hello {}"
result = a.format(name)
print(result)

first_name = "Max"
last_name = "Star"
a = "{} {}"
result = a.format(first_name, last_name) # функция format позволяет поместить в переменную a данные first_name, last_name
print("My name is: " + result)

result2 = f"My name is: {first_name}, {last_name}"
print(result2)