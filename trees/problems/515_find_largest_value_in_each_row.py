# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq = deque([root])
        ans = []
        while dq:
            lenDq = len(dq)
            maxVal = float('-inf')
            for i in range(lenDq):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                maxVal = max(maxVal, node.val)
            ans.append(maxVal)
        return ans
    

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        dq = deque()
        if root:
            dq.append(root)
        ans = []
        while dq:
            lenDq = len(dq)
            currMax = float('-inf')
            for _ in range(lenDq):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                currMax = max(currMax, node.val)
            ans.append(currMax)
        return ans
