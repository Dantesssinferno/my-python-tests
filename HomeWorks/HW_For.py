def task_1_squares():
    for num in range(1, 11):
        print(num ** 2)

def task_2_sum_of_list(numbers):
    print(sum(numbers))

def task_3_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num)

def task_4_sum_of_even(numbers):
    print(sum(num for num in numbers if num % 2 == 0))

def task_5_print_films_with_index(films):
    for i, film in enumerate(films):
        print(f"Индекс {i}: {film}")

def task_6_total_letters_in_films(films):
    print(sum(len(film) for film in films))

def task_7_multiplication_table():
    for num in range(1, 11):
        print(num * 7)

def task_8_even_index_elements(numbers):
    for i in range(0, len(numbers), 2):
        print(numbers[i])

def task_9_average(numbers):
    if numbers:
        print(sum(numbers) / len(numbers))
    else:
        print(0)

def task_10_print_only_letters(a):
    for element in a:
        if element.isalpha():
            print(element)

def task_11_count_letter_occurrences(a, b):
    print(a.count(b))

def task_12_count_specific_letters(a):
    count = a.count('a') + a.count('b') + a.count('i')
    print(count)

def task_13_first_five_of_list():
    numbers = list(range(1, 11))
    for i in range(5):
        print(numbers[i])

def task_14_compare_two_lists(numbers1, numbers2):
    sum1 = sum(numbers1)
    sum2 = sum(numbers2)
    print(1 if sum1 > sum2 else 2)

# Пример запуска (можно раскомментировать нужное):
if __name__ == "__main__":
    # task_1_squares()
    # task_2_sum_of_list(list(map(int, input().split())))
    # task_3_even_numbers(list(map(int, input().split())))
    # task_4_sum_of_even(list(map(int, input().split())))
    # task_5_print_films_with_index(input().split())
    # task_6_total_letters_in_films(input().split())
    # task_7_multiplication_table()
    # task_8_even_index_elements(list(map(int, input().split())))
    # task_9_average(list(map(int, input().split())))
    # task_10_print_only_letters(input())
    # task_11_count_letter_occurrences(input(), input())
    # task_12_count_specific_letters(input())
    # task_13_first_five_of_list()
    # task_14_compare_two_lists(list(map(int, input().split())), list(map(int, input().split())))
    pass