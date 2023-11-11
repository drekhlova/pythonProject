# squares = [x ** 2 for x in range(1, 6)]
# print(squares)  # Вывод: [1, 4, 9, 16, 25]
#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)  # Вывод: [2, 4, 6, 8, 10]
#
#
# # Создание множества, содержащего квадраты чисел от 1 до 5
# squares_set = {x ** 2 for x in range(1, 6)}
# print(squares_set)  # Вывод: {1, 4, 9, 16, 25}
#
#
# # Создание словаря, где ключами являются числа от 1 до 5, а значениями - их квадраты
# squares_dict = {x: x ** 2 for x in range(1, 6)}
# print(squares_dict)  # Вывод: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# # Генерация списка списков с числами от 1 до 3 в каждом внутреннем списке
# matrix = [[x for x in range(1, 4)] for _ in range(3)]
# print(matrix)


from functools import reduce

# Список студентов с баллами
students = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 78},
]

# Используем reduce для суммирования баллов студентов
total_score = reduce(lambda x, y: x + y["score"], students, 0)

print("Общий суммарный балл всех студентов:", total_score)