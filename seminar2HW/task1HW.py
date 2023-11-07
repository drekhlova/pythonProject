# Таблица умножения. Домашнее задание
# Условие
# На вход подается число n.
# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

# Структурная парадигма
# Структурна парадигма ориентирована на создание программы, разбитой на отдельные функции или модули, что упрощает понимание и поддержку кода
def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}")
        print("\n")


n = int(input("Введите число n: "))
multiplication_table(n)

# Императивная парадигма
n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
