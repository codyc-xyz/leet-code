# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dq = deque()
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            dq.append(root.val)
            inorder(root.right)
        inorder(root)
        
        ans = dummy = TreeNode()
        for v in dq:
            dummy.right = TreeNode(v)
            dummy.left = None
            dummy = dummy.right

        return ans.right