# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        dq = deque([root])
        levels = []
        while dq:
            level = 0
            lenDq = len(dq)
            for i in range(lenDq):
                node = dq.popleft()
                level += node.val
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            levels.append(level)
        
        maxLevel = max(levels)

        for i in range(len(levels)):
            if levels[i] == maxLevel:
                return i + 1