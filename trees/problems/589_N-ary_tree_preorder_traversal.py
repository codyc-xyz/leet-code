# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def dfs(root):
            if not root:
                return 
            ans.append(root.val)
            for i in range(len(root.children)):
                dfs(root.children[i])
        dfs(root)
        return ans

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        dq = deque([root])
        while dq:
            node = dq.popleft()
            ans.append(node.val)
            for c in node.children[::-1]:
                dq.appendleft(c)
        return ans