# You are given two integers m and n, which represent the dimensions of a matrix.

# You are also given the head of a linked list of integers.

# Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

# Return the generated matrix.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        ans = [[-1 for i in range(n)] for j in range(m)]
        curr = head
        top,bottom,left,right = 0, m, 0, n
        while left < right and top < bottom:
            for i in range(left, right):
                if not curr:
                    break
                ans[top][i] = curr.val
                curr = curr.next
            top += 1
            for i in range(top, bottom):
                if not curr:
                    break
                ans[i][right - 1] = curr.val
                curr = curr.next
            right -= 1
            for i in range(right -1, left - 1, -1):
                if not curr:
                    break
                ans[bottom - 1][i] = curr.val
                curr = curr.next
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                if not curr:
                    break
                ans[i][left] = curr.val
                curr = curr.next
            left += 1
        return ans