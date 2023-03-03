# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        subTrees = set()
        dupes = set()
        dupeStr = set()

        def dfs(root):
            if not root:
                return 'null'
            string = '(' + str(root.val) + dfs(root.left) + dfs(root.right) + ')'
            
            if string in subTrees and string not in dupeStr:
                dupes.add(root)
                dupeStr.add(string)
            else:
                subTrees.add(string)
            return string 
        dfs(root)
        return dupes

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        subtrees = defaultdict(list)
        ans = set()
        def dfs(root):
            if not root:
                return 'null'
            res = ','.join([str(root.val), dfs(root.left), dfs(root.right)])
            if len(subtrees[res]) == 1:
                ans.add(root)
            subtrees[res].append(root)
            return res
        dfs(root)
        return ans