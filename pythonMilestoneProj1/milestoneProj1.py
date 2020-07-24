#Define board layout w/ placeholders
board = ["-","-","-","-","-","-","-","-","-"]


#Function to call placeholders based on index position
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn():

    i = 0

    while i <= 9:
        i += 1
        position = input("Choose a position [1-9]: ")
        position = int(position) - 1
        if i % 2 == 0:
            board[position] = "X"
            display_board(board)
        else:
            board[position] = "O"
            display_board(board)


def play_game():

    #Displays initial board
    display_board(board)

    handle_turn()


play_game()

