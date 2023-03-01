# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = deque()
        dq = deque([root])

        while dq:
            lenDq = len(dq)
            level = []
            for i in range(lenDq):
                node = dq.popleft()
                level.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            levels.appendleft(level)
        return levels