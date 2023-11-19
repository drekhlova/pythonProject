import time # Модуль time предоставляет функции для работы со временем

# Домашнее задание: исправить ошибки подсчета времени, доделать/поправить/исправить код, добавить комментарии, указать, какую парадигму использовали.
# Исправлена ошибка в 44 строке кода

'''
В данном коде использована парадигма объектно-ориентированного программирования (ООП).  Класс Stopwatch 
определяет состояние и поведение объекта "Секундомер". Он содержит методы для запуска, паузы, возобновления, 
остановки и получения времени работы секундомера. Основной блок кода создает экземпляр класса Stopwatch и 
предоставляет пользователю возможность управлять секундомером в цикле.
'''

# Создается класс "Секундомер"
class Stopwatch:
    # Инициализируются переменные
    def init(self):
        self.start_time = None  # Время запуска секундомера
        self.bool_pause_time = False  # Флаг паузы
        self.pause_start_time = None  # Время начала паузы
        self.total_paused_time = 0  # Общее время пауз

    # Запуск секундомера
    def start(self):
        if not self.start_time:  # Если секундомер не был запущен
            self.start_time = time.time()  # Устанавливается текущее время
        elif self.bool_pause_time:  # Если секундомер был на паузе
            self.total_paused_time += time.time() - self.pause_start_time  # Добавляется время паузы к общему времени
            self.bool_pause_time = False  # Снимается пауза

    # Постановка секундомера на паузу
    def pause(self):
        if self.start_time and not self.bool_pause_time:  # Если секундомер был запущен и не был на паузе
            self.bool_pause_time = True  # Устанавливается пауза
            self.pause_start_time = time.time()  # Устанавливается время начала паузы

    # Возобновление работы секундомера после паузы
    def resume(self):
        if self.bool_pause_time:  # Если секундомер был на паузе
            self.bool_pause_time = False  # Снимается пауза
            self.total_paused_time += time.time() - self.pause_start_time  # Добавляется время паузы к общему времени

    # Остановка секундомера
    def stop(self):
        self.start_time = None  # Обнуляется время запуска
        self.bool_pause_time = False  # Снимается пауза // Исправленная ошибка
        self.pause_start_time = None  # Обнуляется время начала паузы
        self.total_paused_time = 0  # Обнуляется общее время пауз

    # Получение текущего времени секундомера
    def get_time(self):
        if self.start_time:  # Если секундомер был запущен
            if self.bool_pause_time:  # Если секундомер находится на паузе
                return self.pause_start_time - self.start_time - self.total_paused_time  # Возвращается время, прошедшее с момента запуска с учетом паузы
            else:
                return time.time() - self.start_time - self.total_paused_time  # Возвращается время, прошедшее с момента запуска без учета паузы

    # Получение форматированного текущего времени секундомера
    def get_time_format(self):
        time = int(self.get_time())  # Получение текущего времени в секундах
        min = time // 60  # Получение минут из текущего времени
        sec = time % 60  # Получение секунд из текущего времени
        return f"{min:02}: {sec:02}"  # Возвращение времени в формате "мм:сс"


if name == "main":  #
    name = Stopwatch()  # Создание экземпляра класса "Секундомер"
    while True:  # Вывод на экран доступных команд
        print("1 - start")
        print("2 - pause")
        print("3 - continue")
        print("4 - stop")
        print("5 - exit")

        choice = input("Choose number: ")  # Получение ввода пользователя
        if choice == "1":
            name.start()
        elif choice == "2":
            name.pause()
        elif choice == "3":
            name.resume()
        elif choice == "4":
            name.stop()
        elif choice == "5":
            print("Exit")
            break

    # Вывод на экран текущего времени после завершения работы секундомером
    total = name.get_time_format()
    print("time", total)