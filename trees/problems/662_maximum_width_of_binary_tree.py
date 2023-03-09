# Given the root of a binary tree, return the maximum width of the given tree.

# The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

# It is guaranteed that the answer will in the range of a 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxWidth = -1

        dq = deque([(root, 1)])

        while dq:
            lNode, leftIdx = dq[0]
            rNode, rightIdx = dq[-1]
            lenDq = len(dq)
            for i in range(lenDq):
                node, idx = dq.popleft()
                if node.left: dq.append((node.left, idx*2))
                if node.right: dq.append((node.right, idx*2 + 1))
            maxWidth = max(maxWidth, rightIdx - leftIdx + 1)
        return maxWidth