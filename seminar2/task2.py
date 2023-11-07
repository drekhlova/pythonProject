# подсчет суммы от N до 10
# structural programming

N = 10
sum_of_nums = 0
for i in range(1, N+1):
    sum_of_nums += i
print("Сумма чисел от 1 до 10 равно", sum_of_nums)

# procedural programming

def sum_of_numbers(n):
    sum_of_nums = 0
    for i in range(1, N+1):
        sum_of_nums += i
        return sum_of_nums

n = 10
print("Сумма чисел от 1 до 10 равно", sum_of_nums)