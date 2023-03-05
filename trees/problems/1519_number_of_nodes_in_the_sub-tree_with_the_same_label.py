# You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. 
# The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

# The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

# Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

# A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        res = [0] * n

        def dfs(node, prev):
            count = Counter()
            label = labels[node]
            count[label] = 1

            for child in adj[node]:
                if child != prev:
                    count += dfs(child, node)
            res[node] = count[label]
1            return count
        dfs(0, -1)
        return res