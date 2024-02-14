# You are given the root of a binary tree and a positive integer k.

# The level sum in the tree is the sum of the values of the nodes that are on the same level.

# Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

# Note that two nodes are on the same level if they have the same distance from the root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque(([root]))
        levels = []
        while q:
            levSum = 0
            lenQ = len(q)
            while lenQ:
                curr = q.popleft()
                levSum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                lenQ -= 1
            levels.append(levSum)
        return sorted(levels)[len(levels)-k] if len(levels) >= k else -1