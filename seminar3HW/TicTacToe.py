# Класс крестики-нолики
class TicTacToe:
    # Создаем игровое поле размером 3x3
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    # Печатаем игровое поле
    def print_board(self):
        for i in range(3):
            print('|'.join(self.board[i * 3:i * 3 + 3]))
            if i < 2:
                print('-----')

    # Ходы игрока
    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        else:
            return False

    # Определяем победителя
    def check_winner(self, player):
        # Проверяем горизонтали, вертикали и диагонали
        for i in range(3):
            if all([self.board[i * 3 + j] == player for j in range(3)]) or \
               all([self.board[i + 3 * j] == player for j in range(3)]):
                return True
        if all([self.board[4 * i] == player for i in range(3)]) or \
           all([self.board[2 * i] == player for i in range(1, 4, 2)]):
            return True
        return False

    # Проверяем, заполнено ли игровое поле
    def is_full(self):
        return all([cell != ' ' for cell in self.board])

    # Ходы компьютера
    def get_computer_move(self):
        import random
        available_moves = [i for i in range(9) if self.board[i] == ' '] # Находим доступные ходы для компьютера
        return random.choice(available_moves) # Выбираем случайный ход