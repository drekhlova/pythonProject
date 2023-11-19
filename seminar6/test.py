import time # Модуль time предоставляет функции для работы со временем

a = time.time() # Получение текущего времени и сохранение его в переменную a
time.sleep(2) # Приостановка выполнения программы на 2 секунды
b = time.time() # Получение текущего времени после приостановки и сохранение его в переменную b
print(b - a) # Вывод разницы между временем b и временем a на экран