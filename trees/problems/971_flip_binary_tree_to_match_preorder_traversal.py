# You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.
# Any node in the binary tree can be flipped by swapping its left and right subtrees.

# Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.
# Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:

        self.i = 0
        self.res = []
        def dfs(root):
            if not root:
                return
            if root.val != voyage[self.i]:
                self.res = [-1]
                return
            self.i += 1

            if root.left and root.left.val != voyage[self.i]:
                self.res.append(root.val)
                dfs(root.right)
                dfs(root.left)
            else:
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.res if -1 not in self.res else [-1]