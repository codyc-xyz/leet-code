# On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one white king.

# You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni] represents the position of the ith black queen on the chessboard. You are also given an integer array king of length 2 where king = [xKing, yKing] represents the position of the white king.

# Return the coordinates of the black queens that can directly attack the king. You may return the answer in any order.

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        x, y = king
        queenSet = set()
        for qX, qY in queens:
            queenSet.add((qX, qY))
        
        dirs = {(1, 1), (-1, -1), (1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1)}
        ans = []
        for i, j in dirs:
            tmpX = x
            tmpY = y
            while tmpX + i >= 0 and tmpX + i < 8 and tmpY + j >= 0 and tmpY + j < 8:
                tmpX += i
                tmpY += j
                if (tmpX, tmpY) in queenSet:
                    ans.append([tmpX, tmpY])
                    break

        return ans