# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        resP = []
        resQ = []

        def traverse(root, bias):
            if not root:
                if bias:
                    resP.append(root)
                else:
                    resQ.append(root)
                return
            traverse(root.left, bias)
            traverse(root.right, bias)
            if bias:
                resP.append(root.val)
            else:
                resQ.append(root.val)

        traverse(p, True)
        traverse(q, False)
        return resP == resQ

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
    
class Solution:
    def isSameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        def dfs(n):
            if n == None:
                return None
            if not n.left and not n.right:
                return [n.val]
            l = dfs(n.left)
            r = dfs(n.right)
            return [n.val] + [l] + [r]
            
        return dfs(s) == dfs(t)
  
        