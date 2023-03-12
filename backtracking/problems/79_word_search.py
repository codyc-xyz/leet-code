# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.ans = False
        def findWord(i, j, idx, path):
            if [i, j] in path or i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return 
            if board[i][j] == word[idx]:
                idx += 1
            if idx == len(word):
                self.ans = True
                return
            
            path.append([i, j])
            right = findWord(i + 1, j, idx, path[:])
            down = findWord(i, j - 1, idx, path[:])
            up = findWord(i, j + 1, idx, path[:])
            left = findWord(i - 1, j, idx, path[:])

            
        def findFirstLetter(i, j):
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return 
            if board[i][j] == word[0]:
                findWord(i, j, 0, [])
            findFirstLetter(i + 1, j)
            findFirstLetter(i, j + 1)
        findFirstLetter(0, 0)
        return self.ans