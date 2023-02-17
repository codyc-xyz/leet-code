# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        res = [[]]
        stack = [[root, root.val, 0]]
        while stack:
            node, val, level = stack.pop()
            if level >= len(res):
                res.append([])
            res[level].append(val)
            if node.left:
                stack.append([node.left, node.left.val, level + 1])
            if node.right:
                stack.append([node.right, node.right.val, level + 1])
            
        for i in range(len(res)):
            ans.append(sum(res[i]) / len(res[i]))
        return ans

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        vals, length = defaultdict(int), defaultdict(int)
   
        def dfs(node, level):
            if not node:
                return None
            vals[level] += node.val
            length[level] += 1
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)

        ans = []
        for i in range(len(vals)):
            ans.append(vals[i] / length[i])
        return ans