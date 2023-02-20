# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = deque([(root, 0)])
        ans = [[]]
        while dq:
            node, level = dq.popleft()
            while level >= len(ans):
                ans.append([])
            ans[level].append(node.val)
            if node.left:
                dq.append([node.left, level + 1])
            if node.right:
                dq.append([node.right, level + 1])
        return ans