import random


def display_board(board):

    print(board[7] + " | " + board[8] + " | " + board[9])
    print("----------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("----------")
    print(board[1] + " | " + board[2] + " | " + board[3])


def player_input():
    marker = ""
    while marker != "X" and marker != "O":
          marker = input("Player1, choose 'X' or 'O': ").upper()

    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark))


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return "Player1"
    else:
        return "Player2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):

    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Choose a position(1-9): "))

    return position


def replay():
    choice = input("Do you want to play again?(yes/no): ")

    return choice == "yes"



#----------------------------------------------------------------------------------
# Flujo del programa:

print("Welcome to Tic Tac Toe!")


while True:

    the_board = [" "] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn, "will go first")

    play_game = input("Ready to play? (y/n): ")
    if play_game == "y":
        game_on = True
    else:
        game_on = False

    # GAME PLAY:

    while game_on:

        if turn == "Player1":

            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player1 has won!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    break
                else:
                    turn = "Player2"

        else:
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player2 has won!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie game!")
                    break
                else:
                    turn = "Player1"



    if not replay():
        break