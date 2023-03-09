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

        dq = deque([root])
        cont = True
        while dq and cont:
            lenDq = len(dq)
            firstNode = None
            lastNode = None
            cont = False
            for i in range(len(dq)):
                node = dq.popleft()
                if node and firstNode == None:
                    firstNode = i
                if node:
                    lastNode = i
                    dq.append(node.left)
                    dq.append(node.right)
                    cont = True
                else:
                    dq.append(None)
                    dq.append(None)
            if firstNode != None:
                maxWidth = max(maxWidth, lastNode - firstNode + 1)
        return maxWidth