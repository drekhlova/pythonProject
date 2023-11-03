# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

# Сортировка в декларативном стиле
def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True) # Сортировка по убыванию

# Пример использования
numbers = [0, -3, 5, 1, 7, 9]
sorted_numbers = sort_list_declarative(numbers)
print(sorted_numbers) # [9, 7, 5, 1, 0, -3]

numbers = [0, -3, 5, 1, 7, 9]
numbers.sort(reverse=True) # Сортировка по убыванию
print(numbers)  # [9, 7, 5, 1, 0, -3]