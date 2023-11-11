from pythonProject.seminar3HW.TicTacToe import TicTacToe

game = TicTacToe()
player1 = input("Как Вас зовут?: ")
opponent_choice = input("Выберите своего оппонента: 1 - игрок; 2 - компьютер")

# Игра с живым игроком
if opponent_choice == "1":
    player2 = input("Как зовут Вашего оппонента?")
    current_player = player1
    while True:
        game.print_board()
        move = int(input(f'{current_player}, Ваш ход (укажите поле: 0-8): '))
        if game.make_move(move, 'X' if current_player == player1 else 'O'):
            if game.check_winner('X' if current_player == player1 else 'O'):
                print(f'{current_player} сделал(а) игру!')
                break
            elif game.is_full():
                print('Ничья!')
                break
            else:
                current_player = player2 if current_player == player1 else player1
        else:
            print('Недопустимый ход! Попробуйте еще раз.')

# Игра с компьютером
elif opponent_choice == "2":
    current_player = player1
    computer = "Компьютер"
    while True:
        if current_player == player1:
            game.print_board()
            move = int(input(f'{current_player}, Ваш ход (укажите поле: 0-8): '))
            if game.make_move(move, 'X'):
                if game.check_winner('X'):
                    print(f'{current_player} сделал(а) игру!')
                    break
                elif game.is_full():
                    print('Ничья!')
                    break
                else:
                    current_player = computer
            else:
                print('Недопустимый ход! Попробуйте еще раз.')
        else:
            computer_move = game.get_computer_move()
            if game.make_move(computer_move, 'O'):
                game.print_board()
                if game.check_winner('O'):
                    print(f'{computer} одерживает победу!')
                    break
                elif game.is_full():
                    print('Ничья!')
                    break
                else:
                    current_player = player1