class Solution(object):
    """[summary]

  Given a 2D board and a word, find if the word exists in the grid.

  The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

  Example:

  board =
  [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
  ]

  Given word = "ABCCED", return true.
  Given word = "SEE", return true.
  Given word = "ABCB", return false.
    """

    def exist(self, board, word):
        if not board:
            return False
        h, w = len(board), len(board[0])

        def search(d, x, y):
            if x < 0 or x == w or y < 0 or y == h or word[d] != board[y][x]:
                return False
            if d == len(word) - 1:
                return True
            cur = board[y][x]
            board[y][x] == '#'
            found = search(d+1, x+1, y) or search(d+1, x - 1,
                                                  y) or search(d+1, x, y-1) or search(d+1, x, y+1)
            board[y][x] = cur
            return found

        return any(search(0, j, i) for i in range(h) for j in range(w))

    def wordSearch(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if(self.dfs(i, j, board, word[1:])):
                        return True

        return False

    def dfs(self, x, y, board, word):
        temp = board[x][y]
        if len(word) == 0:
            return True
        if x > 0 and board[x-1][y] == word[0]:
            board[x][y] == '#'
            if(self.dfs(x-1, y, board, word[1:])):
                return True

            board[x][y] = temp

        if x < len(board) - 1 and board[x+1][y] == word[0]:
            board[x][y] == '#'
            if(self.dfs(x+1, y, board, word[1:])):
                return True

            board[x][y] = temp
        if y > 0 and board[x][y-1] == word[0]:
            board[x][y] == '#'
            if(self.dfs(x, y-1, board, word[1:])):
                return True

            board[x][y] = temp
        if y < len(board) - 1 and board[x][y+1] == word[0]:
            board[x][y] == '#'
            if(self.dfs(x, y+1, board, word[1:])):
                return True

            board[x][y] = temp

        return False


obj = Solution()
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(obj.exist(board, word))
