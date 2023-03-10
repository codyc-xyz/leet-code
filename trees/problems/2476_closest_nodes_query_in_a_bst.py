# You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

# Find a 2D array answer of size n where answer[i] = [mini, maxi]:

# mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
# maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
# Return the array answer.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:

        arr = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)
        dfs(root)

        ans = []
        for q in queries:
            l, r = 0, len(arr) - 1
            while l < len(arr) - 1 and arr[l + 1] <= q:
                l += 1
            while r > 0 and arr[r - 1] >= q:
                r -= 1
            l = arr[l] if arr[l] <= q else -1
            r = arr[r] if arr[r] >= q else -1
            
            ans.append([l, r])
        return ans