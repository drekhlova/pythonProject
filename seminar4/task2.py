# Пример 1: Обработка данных с использованием функционального программирования

# Импортируем функции из модуля functools
from functools import reduce

# Функция для фильтрации студентов младше 22 лет
def filter_young_students(student):
    return student["age"] < 22

# Функция для вычисления среднего балла студентов
def calculate_average_score(students):
    total_score = reduce(lambda x, y: x + y, [student["score"] for student in students])
    return total_score / len(students)

# Отфильтровать студентов
students = [
    {"name": "Alice", "age": 22, "score": 95},
    {"name": "Bob", "age": 21, "score": 88},
    {"name": "Charlie", "age": 23, "score": 92},
    {"name": "David", "age": 22, "score": 78},
]

young_students = list(filter(filter_young_students, students))

# Вычислить средний балл
average_score = calculate_average_score(students)

print("Пример 1: Обработка данных с использованием функционального программирования")
print(young_students)
print(average_score)

# Пример 2: Работа с функциями высшего порядка

numbers = [1, 2, 3, 4, 5]

# Функция для применения серии функций к числу
def apply_operations(num, operations):
    result = num
    for operation in operations:
        result = operation(result)
    return result

# Операции, которые будут применены к числам
operations = [
    lambda x: x * 2,
    lambda x: x + 3,
    lambda x: x ** 2,
]

# Применить операции к числам
result = list(map(lambda x: apply_operations(x, operations), numbers))

print("\nПример 2: Работа с функциями высшего порядка")
print(result)