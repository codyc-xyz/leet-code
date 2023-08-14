# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def generate(left, right):
            if left == right:
                return [TreeNode(left)]
            if left > right:
                return [None]
            res = []
            for val in range(left, right + 1):
                for LeftTree in generate(left, val-1):
                    for RightTree in generate(val+1, right):
                        res.append(TreeNode(val, LeftTree, RightTree))

            return res

        return generate(1, n)
