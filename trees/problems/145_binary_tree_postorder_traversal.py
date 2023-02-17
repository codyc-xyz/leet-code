# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postOrder(root):
            if not root:
                return 
            postOrder(root.left)
            postOrder(root.right)
            ans.append(root.val)
        postOrder(root)
        return ans        

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        ans = deque()
        stack = [root]

        while stack:
            node = stack.pop()
            ans.appendleft(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans