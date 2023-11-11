from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, likes')

+ likes('Вася', 'чай')
+ likes('Маша', 'кофе')
+ likes('Вася', 'кофе')

# Запрос: кто любит кофе?
print(likes(X, 'кофе'))