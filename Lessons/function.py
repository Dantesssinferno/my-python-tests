# num_1 = 10
# num_2 = 20
# result = num_1 + num_2
# print(result)
#
# num_1 = 30
# num_2 = 40
# result = num_1 + num_2
# print(result)

def summ(num_1, num_2):
    result = num_1 + num_2
    print(result)

summ(10, 20)
summ(30, 40)
summ(50, 60)
summ(60, 70)
summ(80, 90)
summ(100, 110)
summ(120, 130)
summ(140.00, 150.99)  # float
summ("Hellow", "World") # string
summ(num_2="Hellow", num_1="World") #

name = input()
age = input()

def hi(name, age):
    result = f"Hi, i'm {name}, i have {age} years old"
    return result


h = hi(name, age)
print(h)