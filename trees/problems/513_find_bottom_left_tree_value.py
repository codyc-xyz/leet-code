# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        arr = []
        while dq:
            arr.append(dq[0].val)
            lenDq = len(dq)
            for i in range(lenDq):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return arr[-1]

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dq = deque([root])
        while dq:
            node = dq.popleft()
            if node.right: dq.append(node.right)
            if node.left: dq.append(node.left)
        return node.val
    
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        dq = deque(([root]))

        while dq:
            lenDq = len(dq)
            while lenDq:
                curr = dq.popleft()
                ans = curr.val
                if curr.right:
                    dq.append(curr.right)
                if curr.left:
                    dq.append(curr.left)
                lenDq -= 1
        return ans

