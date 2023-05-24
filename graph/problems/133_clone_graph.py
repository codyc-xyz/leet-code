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
        while curr:
            currNode = curr.popleft()
            if currNode not in hm:
                hm[currNode] = Node(currNode.val)
            for n in currNode.neighbors:
                if n not in hm:
                    hm[n] = Node(n.val)
                    curr.append(n)
                hm[currNode].neighbors.append(hm[n])
        return hm[node]


