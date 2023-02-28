# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        parent = {}

        def dfs(root, prev):
            if not root:
                return
            parent[root] = prev
            prev = root
            dfs(root.left, prev)
            dfs(root.right, prev)
        dfs(root, None)
        
        dq = deque( [(target, 0)] )
        seen = { target }
        ans = []
        while dq:
            node, depth = dq.popleft()
            if depth == k:
                ans.append(node.val)
            for n in (node.left, node.right, parent[node]):
                if n and n not in seen:
                    seen.add(n)
                    dq.append([n, depth + 1])
        return ans