# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n % 2:
            return []

        memo = {0: [], 1: [TreeNode(0)]}
        def dfs(n):
            res = []
            if n not in memo:
                for l in range(n):
                    r = n - 1 - l
                    leftTrees, rightTrees = dfs(l), dfs(r)
                    for t1 in leftTrees:
                        for t2 in rightTrees:
                            res.append(TreeNode(0, t1, t2))
                memo[n] = res
            else:
                res.extend(memo[n])
            return res
        
        return dfs(n)
    

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        if not n % 2:
            return []

        memo = {0: [], 1: [TreeNode(0)]}

        def dfs(n):
            res = []

            if n not in memo:
                for i in range(n):
                    j = n - 1 - i
                    leftTrees, rightTrees = dfs(i), dfs(j)
                    for l in leftTrees:
                        for r in rightTrees:
                            res.append(TreeNode(0, l, r))
                memo[n] = res
            else:
                res.extend(memo[n])
            return res

        return dfs(n)
