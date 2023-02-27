# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        ans = []
        while dq:
            lenDq = len(dq)
            curr = []
            for i in range(lenDq):
                node = dq.popleft()
                curr.append(node.val)
                for c in node.children:
                    dq.append(c)
            ans.append(curr)
        return ans