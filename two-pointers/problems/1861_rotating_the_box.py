# You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

# A stone '#'
# A stationary obstacle '*'
# Empty '.'

# The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. 
# Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. 
# Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

# It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

# Return an n x m matrix representing the box after the rotation described above.

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        rows, columns = len(box), len(box[0])
        
        for i in range(rows):
            for j in range(columns -1, -1, -1):
                if box[i][j] == '#':
                    empty = j + 1
                    while empty < columns and box[i][empty] == '.':
                        empty += 1
                    if empty < columns and box[i][empty] == '.':
                        box[i][empty] = box[i][j]
                        box[i][j] = '.'
                    elif empty - 1 < columns and box[i][empty - 1] == '.':
                        box[i][empty - 1] = box[i][j]
                        box[i][j] = '.'
                        
        k = rows - 1
        res = [[None for a in range(rows)] for b in range(columns)]
        
        for i in range(rows):
            for j in range(columns):
                res[j][k] = box[i][j]
            k -= 1
        return res