import os
import random
import time

board = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' ',
}


def find_empty():
    for key, value in board.items():
        if value == ' ':
            return key
    return None


def check_draw():
    if board['1'] == board['2'] == board['3'] != ' ':
        return True
    elif board['4'] == board['5'] == board['6'] != ' ':
        return True
    elif board['7'] == board['8'] == board['9'] != ' ':
        return True
    elif board['1'] == board['4'] == board['7'] != ' ':
        return True
    elif board['2'] == board['5'] == board['8'] != ' ':
        return True
    elif board['3'] == board['6'] == board['9'] != ' ':
        return True
    elif board['1'] == board['5'] == board['9'] != ' ':
        return True
    elif board['3'] == board['5'] == board['7'] != ' ':
        return True


def check_cell(number):
    if board[number] == ' ':
        return True
    else:
        return False

which_turn = 1
game_is_on = True


def reset():
    os.system('cls')  # clear the screen
    global board, which_turn, game_is_on
    board = {
        '1': ' ',
        '2': ' ',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': ' ',
        '8': ' ',
        '9': ' ',
    }
    which_turn = 1
    game_is_on = True


def show_board():
    print()
    print(f"   {board['1']} | {board['2']} | {board['3']} ")
    print("  ───┼───┼───")
    print(f"   {board['4']} | {board['5']} | {board['6']} ")
    print("  ───┼───┼───")
    print(f"   {board['7']} | {board['8']} | {board['9']} ")
    print()


def animation():
    global board
    os.system('cls')  # clear the screen

    board = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
    }

    show_board()
    time.sleep(2)
    os.system('cls')  # clear the screen

    board = {
        '1': ' ',
        '2': ' ',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': ' ',
        '8': ' ',
        '9': ' ',
    }


def game():
    global board, game_is_on, which_turn
    while game_is_on:

        show_board()

        if check_draw():
            if which_turn == 1:
                print('You lose... :(')
                again = input('Do you want to play again? Y/N: ')
                if again.upper() == 'N':
                    game_is_on = False
                    break
                else:
                    reset()
                    animation()
                    game()
            else:
                print('You win! :)')
                again = input('Do you want to play again? Y/N: ')
                if again.upper() == 'N':
                    game_is_on = False
                    break
                else:
                    reset()
                    animation()
                    game()

        if find_empty():
            if which_turn == 1:
                your_move = input('Your X goes to: ')
                while not check_cell(your_move):
                    your_move = input('Nope. Type again: ')
                board[your_move] = 'X'
                which_turn = 2

            elif which_turn == 2:
                pc_move = find_empty()
                print("Computer's O goes to...")
                time.sleep(1)
                board[pc_move] = 'O'
                which_turn = 1

            os.system('cls')  # clear the screen

        else:
            print("It's a draw.")
            again = input('Do you want to play again? Y/N: ')
            if again.upper() == 'N':
                game_is_on = False
                break
            else:
                reset()
                animation()
                game()


reset()
animation()
game()
