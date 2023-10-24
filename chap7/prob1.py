import random
print("Welcome to the greatest intellenctual callenge of all time : Tic-Tac-Toe")
print("This will be a showdown btween your human brain and my silicon processor.")
print("\nYou will make your move known by entering a number, 1-9. the number")
print("will correspond to the voard position as illustrated: ")
print(" 1 | 2 | 3 ")
print("------------")
print(" 4 | 5 | 6 ")
print("------------")
print(" 7 | 8 | 9 ")
print("Prepare yourself, human. The ultimate battle is about to begin.")



    
def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def computer_move(board):
    # Check if there's a row with two X's and one empty cell
    for i in range(3):
        if board[i].count("X") == 2 and board[i].count(" ") == 1:
            j = board[i].index(" ")
            return i, j

    # Check if there's a column with two X's and one empty cell
    for j in range(3):
        column = [board[i][j] for i in range(3)]
        if column.count("X") == 2 and column.count(" ") == 1:
            i = column.index(" ")
            return i, j

    # Check diagonals
    if board[0][0] == board[1][1] == "X" and board[2][2] == " ":
        return 2, 2
    if board[0][0] == board[2][2] == "X" and board[1][1] == " ":
        return 1, 1
    if board[1][1] == board[2][2] == "X" and board[0][0] == " ":
        return 0, 0
    if board[0][2] == board[1][1] == "X" and board[2][0] == " ":
        return 2, 0
    if board[0][2] == board[2][0] == "X" and board[1][1] == " ":
        return 1, 1
    if board[1][1] == board[2][0] == "X" and board[0][2] == " ":
        return 0, 2

    # If no winning move is available, choose a random empty cell
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        if current_player == "X":
            cell = int(input(f"Where whill you move? <1-9>: ")) - 1
            print(f"Fine...")
            row, col = cell // 3, cell % 3
        else:
            print(f"Computer ({current_player}) is making a move...")
            row, col = computer_move(board)
        
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            if current_player == "X":
                print(f"Player {current_player} wins!")
            else:
                print("Computer (O) wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()


