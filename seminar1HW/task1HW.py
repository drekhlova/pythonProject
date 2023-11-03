# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


# Сортировка в императивном стиле
def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]: # Сортировка по убыванию
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

# Пример использования
numbers = [0, -3, 5, 1, 7, 9]
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers) # [9, 7, 5, 1, 0, -3]

