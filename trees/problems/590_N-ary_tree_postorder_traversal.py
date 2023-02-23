# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        arr = deque()
        dq = deque([root])
        while dq:
            node = dq.popleft()
            arr.appendleft(node.val)
            lenChildren = len(node.children) 
            for i in range(lenChildren):
                dq.appendleft(node.children[i])
        return arr
        
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        def dfs(root):
            if not root:
                return
            for c in root.children:
                dfs(c)
            arr.append(root.val)
        dfs(root)
        return arr