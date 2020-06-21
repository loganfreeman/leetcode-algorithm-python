solution = []
def isSafe(board, row, column):
    """
    This function returns a boolean value True if it is safe to place a queen there
    considering the current state of the board.
    Parameters :
    board(2D matrix) : board
    row ,column : coordinates of the cell on a board
    Returns :
    Boolean Value
    """
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board), 1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, row):
    """it creates a state space tree and calls the safe function until it receives a False
    and terminates and backtracks to the next possible solution branch
    """

    if row >= len(board):
        """if the row number exceeds N we have a successful combination
        and the combination is appeneded to the solution list"""
        solution.append(board)
        printboard(board)
        return
    for i in range(len(board)):
        """for every row it iterates through each column to check if it is possible to place a queen there
        """
        if isSafe(board, row, i):
            board[row][i] = 1
            solve(board, row+1)
            board[row][i] = 0
    return False

def printboard(board):
    """
    Prints the boards that have a successful combination.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

n = 8
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))