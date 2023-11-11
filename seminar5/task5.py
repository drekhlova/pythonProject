from pyDatalog import pyDatalog
 # this task has to be modified to eliminate errors in output
pyDatalog.create_terms('X, Y, age, total_age, number_of_people')

+ age('Мария', 30)
+ age('Иван', 40)
+ age('Алексей', 20)

# Определение общего возраста
total_age[X] = sum(Y, for_each=age[X, Y])

# Определение количества людей
number_of_people[X] = count(Y, for_each=age[X, Y])

# Расчет среднего возраста
average_age[Y] = (total_age[X] / number_of_people[X])

# Запрос среднего возраста
print(average_age[Y])