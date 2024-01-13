# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

# Two binary trees are considered leaf-similar if their leaf value sequence is the same.

# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1, res2 = [],[]
        stack1, stack2 = [root1], [root2]

        while stack1 or stack2:
            node1 = node2 = None
            if stack1:
                node1 = stack1.pop()
            if stack2:
                node2 = stack2.pop()
            if node1:
                if node1.left:
                    stack1.append(node1.left)
                if node1.right:
                    stack1.append(node1.right)
                if not node1.left and not node1.right:
                    res1.append(node1.val)
            if node2:
                if node2.left:
                    stack2.append(node2.left)
                if node2.right:
                    stack2.append(node2.right)
                if not node2.left and not node2.right:
                    res2.append(node2.val)

        return res1 == res2

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def constructLeaves(root):
            arr = []

            def traverse(root):
                if not root:
                    return 
                traverse(root.left)
                if not root.left and not root.right:
                    arr.append(root.val)
                traverse(root.right)

            traverse(root)
            return arr
            
        return constructLeaves(root1) == constructLeaves(root2)
    

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
            dfs(root.left, leaves)
            dfs(root.right, leaves)
            return leaves

        leaves1 = dfs(root1, [])
        leaves2 = dfs(root2, [])

        return leaves1 == leaves2
