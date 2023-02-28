# Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the highest frequency in any order.

# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        subSums = {}
        def dfs(root, subSum):
            if not root:
                return 0
            subSum = root.val + dfs(root.left, subSum) + dfs(root.right, subSum)
            subSums[subSum] = subSums.get(subSum, 0) + 1
            return subSum
            
        dfs(root, 0)
        maxCount = max(subSums.values())
        ans = []
        for s in subSums:
            if subSums[s] == maxCount:
                ans.append(s)
        return ans