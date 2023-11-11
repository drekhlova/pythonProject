import friend
from pyDatalog import pyDatalog
pyDatalog.create_terms('X, Y, Z, friend, is_friend')

+ friend('Алексей', 'Игорь')
+ friend('Игорь', 'Светлана')
+ friend('Светлана', 'Алексей')
+ friend('Игорь', 'Ваня')

is_friend(X, Y) <= friend(X, Y)
is_friend(X, Y) <= friend(Y, X)


# Запрос: кто является другом для Игоря?
print(is_friend('Игорь', X))