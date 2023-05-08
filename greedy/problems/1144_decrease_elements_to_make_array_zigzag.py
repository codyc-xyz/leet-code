# Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

# An array A is a zigzag array if either:

# Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
# OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
# Return the minimum number of moves to transform the given array nums into a zigzag array.

class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        oddMoves = evenMoves = 0
        oddArr = [float('-inf')] + nums + [float('-inf')]
        evenArr = [float('-inf')] + nums + [float('-inf')]

        for i in range(1, len(nums) + 1):
            if (i - 1) % 2:
               if oddArr[i] <= oddArr[i - 1] or oddArr[i] <= oddArr[i + 1]:
                    if oddArr[i] <= oddArr[i - 1]:
                       tmp = oddArr[i - 1]
                       oddArr[i - 1] = oddArr[i] - 1
                       oddMoves += tmp - oddArr[i - 1]
                    if oddArr[i] <= oddArr[i + 1]:
                        tmp = oddArr[i + 1]
                        oddArr[i + 1] = oddArr[i] - 1
                        oddMoves += tmp - oddArr[i + 1]
            else:
                if evenArr[i] <= evenArr[i - 1] or evenArr[i] <= evenArr[i + 1]:
                    if evenArr[i] <= evenArr[i - 1]:
                       tmp = evenArr[i - 1]
                       evenArr[i - 1] = evenArr[i] - 1
                       evenMoves += tmp - evenArr[i - 1]
                    if evenArr[i] <= evenArr[i + 1]:
                        tmp = evenArr[i + 1]
                        evenArr[i + 1] = evenArr[i] - 1
                        evenMoves += tmp - evenArr[i + 1]
               
        return min(evenMoves, oddMoves)