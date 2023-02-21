# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        dq = deque([(root, root.val)])
        ans = 0
        while dq:
            node, maxVal = dq.popleft()
            if node.val >= maxVal:
                ans += 1
            if node.left:
                dq.append((node.left, max(node.left.val, maxVal)))
            if node.right:
                dq.append((node.right, max(node.right.val, maxVal)))
        return ans