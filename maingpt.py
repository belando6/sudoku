import random

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def generate_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if random.randint(0, 1) > 0.5:
                num = random.randint(1, 9)
                while not valid(board, num, (i, j)):
                    num = random.randint(1, 9)
                board[i][j] = num
    return board

def play_sudoku():
    board = generate_board()
    print("Here's the Sudoku board:")
    print_board(board)

    while True:
        print_board(board)
        row = int(input("Enter row (0-8): "))
        col = int(input("Enter col (0-8): "))
        num = int(input("Enter number (1-9): "))
        if valid(board, num, (row, col)):
            board[row][col] = num
        else:
            print("Invalid move. Try again.")
        
        if not find_empty(board):
            print("Congratulations, you solved the Sudoku!")
            break

if __name__ == "__main__":
    play_sudoku()
