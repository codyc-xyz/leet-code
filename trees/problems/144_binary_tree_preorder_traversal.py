# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        arr = []
        def preorder(root):
            if not root:
                return
            arr.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return arr

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ans = []
        stack = deque([root])
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                if node.right:
                    stack.append(node.right)
                stack.append(node.left)
                continue
            if node.right:
                stack.append(node.right)
        return ans          