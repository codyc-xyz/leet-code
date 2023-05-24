# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        hm = {}
        if not node:
            return node
        curr = collections.deque()
        curr.append(node)
        hm[node] = Node(node.val)
        while curr:
            currNode = curr.popleft()
            for n in currNode.neighbors:
                if n not in hm:
                    hm[n] = Node(n.val)
                    curr.append(n)
                hm[currNode].neighbors.append(hm[n])
        return hm[node]

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node
        hm = {}

        def dfs(node):
            if node in hm:
                return hm[node]
            hm[node] = Node(node.val)
            for n in node.neighbors:
                hm[node].neighbors.append(dfs(n))
            return hm[node]
        return dfs(node)




