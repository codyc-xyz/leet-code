# Given a n-ary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        level = 0
        dq = deque([root])
        while dq:
            lenDq = len(dq)
            for i in range(lenDq):
                node = dq.popleft()
                for c in node.children:
                    dq.append(c)
            level += 1
        return level