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
        l = r = 0
        for q in queries:
            l, r = 0, len(arr) - 1
            while l < r:
                m = (l + r) // 2
                if arr[m] < q:
                    l = m + 1
                elif arr[m] > q:
                    r = m 
                else:
                    l = r = m
                    break
            if l > 0 and arr[l] > q:
                l -= 1
            left = arr[l] if arr[l] <= q else -1
            right = arr[r] if arr[r] >= q else - 1
            ans.append([left, right])
        return ans