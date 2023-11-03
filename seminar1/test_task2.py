N = 10
numbers = range(1, N + 1)
total = sum(numbers)
print("Сумма чисел от 1 до", N, "равна", total)

numbers = [5, 2, 9, 8, 3, 6]
result = []

# императивный
for num in numbers:
    if num % 2 == 0:  # Проверяем, является ли число четным.
        result.append(num)

result.sort(reverse=True)  # Сортируем по убыванию.
for i in range(len(result)):
    result[i] = result[i] ** 2  # Возводим в квадрат.

# декларативный
numbers = [5, 2, 9, 8, 3, 6]

# Декларативно выбираем четные числа, сортируем и возводим в квадрат.
result = sorted((x ** 2 for x in numbers if x % 2 == 0), reverse=True)