from typing import List, Tuple

def get_valid_pos(position: Tuple[int], n: int) -> List[Tuple[int]]:
    """Find all valid poistions a knight can move to from current position
    """

    y, x = position
    positions = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1)
    ]
    permissible_positions = []

    for position in positions:
        y_test, x_test = position
        if 0 <= y_test < n and 0 <= x_test < n:
            permissible_positions.append(position)

    return permissible_positions

def is_complete(board: List[List[int]]) -> bool:
    """Check if the board has been completed filled with non-zero values
    """

    return not any(elem == 0 for row in board for elem in row)

def helper(board: List[List[int]], pos: Tuple[int], curr: int) -> bool:
    if is_complete(board):
        return True
    for position in get_valid_pos(pos, len(board)):
        y, x = position
        if board[y][x] == 0:
            board[y][x] = curr + 1
            if helper(board, position, curr + 1):
                return True
            board[y][x] = 0
    return False

def open_knight_tour(n: int) -> List[List[int]]:
    board = [ [0]* n for j in range(n)]
    for i in range(n):
        for j in range(n):
            board[i][j] = 1
            if helper(board, (i, j), 1):
                return board
            board[i][j] = 0
    raise ValueError(f"Open Kight Tour cannot be performed on a board of size {n}")