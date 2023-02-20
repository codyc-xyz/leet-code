# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        dq = deque([(root, 0)])
        ans = []
        maxLevel = -1
        while dq:
            node, level = dq.popleft()
            if level > maxLevel:
                ans.append(node.val)
                maxLevel = level
            if node.right:
                dq.append((node.right, level + 1))
            if node.left:
                dq.append((node.left, level + 1))
        return ans