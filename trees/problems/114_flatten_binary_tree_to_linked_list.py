# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if 
        arr = []
        def dfs(root):
            if not root:
                return
            arr.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        for i in range(len(arr) - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]