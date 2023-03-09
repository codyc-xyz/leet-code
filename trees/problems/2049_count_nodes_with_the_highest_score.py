# There is a binary tree rooted at 0 consisting of n nodes. The nodes are labeled from 0 to n - 1. You are given a 0-indexed integer array parents representing the tree, where parents[i] is the parent of node i. 
# Since node 0 is the root, parents[0] == -1.

# Each node has a score. To find the score of a node, consider if the node and the edges connected to it were removed. The tree would become one or more non-empty subtrees. 
# The size of a subtree is the number of the nodes in it. The score of the node is the product of the sizes of all those subtrees.

# Return the number of nodes that have the highest score.

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        
        adj = defaultdict(list)

        for i, parent in enumerate(parents):
            adj[parent].append(i)

        n = len(parents)
        count = collections.Counter()

        def dfs(root):
            p, s = 1, 0
            for child in adj[root]:
                res = dfs(child)
                p *= res
                s += res
            p *= max(1, n - 1 - s)
            count[p] += 1
            return s + 1
        dfs(0)
        return count[max(count.keys())]
