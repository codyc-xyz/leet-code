# Given the root of a binary tree, each node in the tree has a distinct value.

# After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

# Return the roots of the trees in the remaining forest. You may return the result in any order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        def dfs(root):
            if not root:
                return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val in to_delete:
                if root.left and root.left not in to_delete:
                    self.ans.append(root.left)
                if root.right and root.right not in to_delete:
                    self.ans.append(root.right)
                return None
            return root
        self.ans.append(dfs(root)) if root.val not in to_delete else dfs(root)
        return self.ans