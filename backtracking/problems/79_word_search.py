# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def findWord(i, j, idx, path):
            if (i, j) in path or i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or board[i][j] != word[idx]:
                return False
            idx += 1
            if idx == len(word):
                return True
            
            path.add((i, j))
            up = findWord(i + 1, j, idx, path)
            left = findWord(i, j - 1, idx, path)
            right = findWord(i, j + 1, idx, path)
            down = findWord(i - 1, j, idx, path)
            path.remove((i, j))
            return up or left or right or down

            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = findWord(i, j, 0, set())
                    if res == True:
                         return res
                    else: 
                        continue