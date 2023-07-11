# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return min(arr[i] - arr[i - 1] for i in range(1, len(arr)))

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float('inf')
        self.prev = None
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if self.prev:
                self.minDiff = min(self.minDiff, root.val - self.prev.val)
            self.prev = root
            dfs(root.right)
        dfs(root)
        return self.minDiff

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        stack = []
        curr = root
        prev = None
        res = float('inf')
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev:
                    res = min(res, curr.val - prev.val)
                prev = curr
                curr = curr.right
        return res
    
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        seen = []
        def dfs(node):
            seen.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        seen.sort()
        minDiff = float('inf')
        for i in range(1, len(seen)):
            minDiff = min(minDiff, seen[i] - seen[i - 1])

        return minDiff
