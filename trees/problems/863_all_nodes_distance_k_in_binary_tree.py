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
    

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def add_parent(node, prev):
            node.parent = prev
            if node.left:
                add_parent(node.left, node)
            if node.right:
                add_parent(node.right, node)

        add_parent(root, None)
        ans = set()
        seen = set()
        def dfs(node, seenTarget, dist):
            if node == target:
                seenTarget = True
            if seenTarget:
                seen.add(node)
                if dist == k:
                    ans.add(node.val)
                elif dist < k:
                    if node.left and node.left not in seen:
                        dfs(node.left, seenTarget, dist + 1)
                    if node.right and node.right not in seen:
                        dfs(node.right, seenTarget, dist + 1)
                    if node.parent and node.parent not in seen:
                        dfs(node.parent, seenTarget, dist + 1)
            else:
                if node.left:
                    dfs(node.left, seenTarget, dist)
                if node.right:
                    dfs(node.right, seenTarget, dist)
        dfs(root, False, 0)
        return list(ans)

                    