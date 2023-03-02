# You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

# Return the number of good leaf node pairs in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [1]
            left = dfs(root.left)
            right = dfs(root.right)

            for i in left:
                for j in right:
                    if i + j <= distance:
                        self.ans += 1
            return [i+1 for i in left+right if i <= distance]
        dfs(root)
        return self.ans